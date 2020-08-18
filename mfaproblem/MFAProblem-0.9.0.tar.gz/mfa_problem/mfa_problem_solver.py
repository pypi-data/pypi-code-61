import time
import cvxpy as cvx
import numpy as np
from numpy import ndarray
from scipy.sparse import spdiags, csc_matrix, csr_matrix, vstack

import mfa_problem_matrices
try:
    from . import su_trace
except Exception:
    import su_trace

DATA, SIGMA, LB, UB = 0, 1, 2, 3


def classify_with_matrix_reduction(
    AConstraintReordered: csc_matrix,
    nb_measured: int
):
    '''
    This function determines which variables are redundant, measured, determinable or free
    (undetermined)
    It is necessary to identify the free variables before undertaking the MonteCarlo
    simulations
    '''

    # Theoritical details available in chapter 7 of Book by Veverka and Madron (1997),
    # "MATERIAL AND ENERGY BALANCING IN THE PROCESS INDUSTRIES"
    # Ai_eq is called C in chapter 7 of Book by Veverka and Madron (1997)
    # We put it into canonical form in order to classify variables
    # We start by separating Ai into B + A where B contains unmeasured vars
    # and A contains measured vars

    tk0 = time.time()
    su_trace.logger.debug(
        'start classif (matrix_reduction)' +
        str(time.strftime("%T", time.localtime(tk0)))
    )
    su_trace.logger.info(
        'PERF (classify) size of the problem AConstraintReordered: ' +
        f'{AConstraintReordered.shape}'
    )

    tk3 = time.time()
    AEqReorderedRef = mfa_problem_matrices.to_reduced_row_echelon_form(
        AConstraintReordered
    )
    non_null_rows = AEqReorderedRef[:, :AConstraintReordered.shape[1]-2].getnnz(1) > 0
    # null_rows = AEqReorderedRef[:, :AConstraintReordered.shape[1]-2].getnnz(1) == 0
    # non_null_cols = (AEqReorderedRef[null_rows].getnnz(0)).nonzero()[0]  # check non conflict must be 0
    AEqReorderedRef = AEqReorderedRef[non_null_rows]

    tk1 = time.time()
    su_trace.logger.info('PERF (matrix_reduction) matrix reduction done ' + str(round(tk1-tk0, 2)))
    # If a row of B_second has only one non-null value then the corresponding variable
    # is determinable (= observable).
    # All other variables are free (= indeterminable = non-observable).
    nb_unmeasured = AConstraintReordered.shape[1]-nb_measured-2
    B_second = AEqReorderedRef[:, 0:nb_unmeasured]
    B_second = B_second[B_second.getnnz(1) > 0]
    [determinable_vars, determinable_rows] = mfa_problem_matrices.extract_determinable_variables(
        B_second, 1e-6, True
    )
    determinable_var2col = dict(zip(determinable_vars, determinable_rows))
    L = B_second.shape[0]
    # rank of matrix B_second = number of rows <= number of determinable + number of free (Sous déterminé)
    M = len(non_null_rows) - L

    tk2 = time.time()
    su_trace.logger.info('PERF (matrix_reduction) check unique row done ' +
                         str(round(tk2-tk1, 2)) + ' / ' + str(round(tk2-tk0, 2)))

    # All non-null columns of matrix A_prime correspond to redundant variables
    # Null columns of matrix A_prime correspond to just-measured = non-redundant variables.
    measured_null_cols = AEqReorderedRef[L:, nb_unmeasured:nb_unmeasured+nb_measured].getnnz(0) == 0
    non_redundant = measured_null_cols.nonzero()[0]+nb_unmeasured
    redundant = np.logical_not(measured_null_cols).nonzero()[0]+nb_unmeasured

    determinable = np.array(determinable_vars)
    nb_free_vars = 0
    if nb_unmeasured != 0:
        free = np.empty(nb_unmeasured)
        free.fill(True)
        if len(determinable) != 0:
            free[determinable] = False
        free = free.nonzero()[0]
        nb_free_vars = len(free)

    vars_type = np.empty(nb_unmeasured+nb_measured, dtype=object)
    vars_type[redundant] = 'redondant'  # non fiable
    vars_type[non_redundant] = 'mesuré'  # fiable
    if nb_unmeasured != 0:
        if len(determinable) != 0:
            vars_type[determinable] = 'déterminé'
        if len(free) != 0:
            vars_type[free] = 'libre'

    # NB :
    # - if L < M (H > 0), measured variables cannot be arbitrary
    # - if L < J, non-unique solution for unmeasured variables.
    if L < M:
        su_trace.logger.debug('Some measured variables are redundant. Reconciliation is needed.')
    else:
        su_trace.logger.debug('No redundancy. The measured variables are not modified.')
    if L < nb_unmeasured:
        su_trace.logger.debug('There are free variables with a range of solution.')
    else:
        su_trace.logger.debug('All unmeasured variables are determinated.')
    su_trace.logger.debug('    Degree of redundancy (H = M - L): ' + str(M-L))
    su_trace.logger.debug('    Nb redundant vars (I-I0): ' + str(len(redundant)))
    su_trace.logger.debug('    Nb just-measured vars (I0): ' + str(len(non_redundant)))
    su_trace.logger.debug('    Nb determinable vars (L0): ' + str(len(determinable)))
    su_trace.logger.debug('    Nb free vars (L-L0): ' + str(nb_free_vars))
    tk4 = time.time()
    su_trace.logger.info('Output (matrix_reduction) : ' + str(round(tk4-tk3, 2)) + ' / ' + str(round(tk4-tk0, 2)))

    return AEqReorderedRef, determinable_var2col, non_redundant, vars_type, L


def Cvx_minimize(
    Aconstraint: csc_matrix,
    AIneq: csc_matrix,
    ter_vectors: np.ndarray,
    nb_determinated: int
):
    pb_vector_size = ter_vectors.shape[1]
    # definition of obj function
    ter_vectors[SIGMA] = np.where(ter_vectors[SIGMA] > 0, ter_vectors[SIGMA], 1)
    coef = np.divide(np.ones(pb_vector_size), np.sqrt(ter_vectors[SIGMA]))
    coef[:nb_determinated] = 0

    coef_diag = cvx.Constant(spdiags(coef, [0], pb_vector_size, pb_vector_size))

    X = cvx.Variable(pb_vector_size)
    obj = cvx.Minimize(cvx.sum_squares(coef_diag@(X-ter_vectors[DATA])))

    const = []
    const.append(X >= ter_vectors[LB])
    const.append(X <= ter_vectors[UB])

    if AIneq.shape[0] != 0:
        AIneqCvx = cvx.Constant(AIneq[:, :pb_vector_size])  # AIneqCvx is already sparse
        li = AIneq.getcol(pb_vector_size).toarray().flatten()
        ui = AIneq.getcol(pb_vector_size+1).toarray().flatten()
        const.append(AIneqCvx @ X >= li)
        const.append(AIneqCvx @ X <= ui)

    # definition of constraints
    if Aconstraint.shape[0] != 0:
        Ai = cvx.Constant(Aconstraint[:, :pb_vector_size])  # Ai is already sparse
        leq = Aconstraint.getcol(pb_vector_size).toarray().flatten()
        const.append(Ai @ X == leq)

    # Problem
    prob = cvx.Problem(obj, const)
    obj = prob.solve(solver=cvx.OSQP, verbose=False)
    su_trace.logger.debug('Solve_scmfa prob.solve with generic parameters done.')
    if prob.status in ["infeasible", "unbounded"]:
        su_trace.logger.info('Problem is ' + prob.status)
        return None
    ares = [a for a in X.value.tolist()]
    return ares


def compute_initial_value_pp_variables(
    full_ter_vectors: ndarray,
    solved_vector: ndarray,
    AConstraintEq: csr_matrix,
    AConstraintIneq: csr_matrix,
    post_process: ndarray,
    nb_measured: int,
    free_intervals: ndarray,
):
    ter_size = full_ter_vectors.shape[1]

    eq = AConstraintEq[:, ter_size].toarray().flatten()

    non_pp_vars = np.full(ter_size, True)
    non_pp_vars[post_process] = False
    AeqNonPP = AConstraintEq[:, non_pp_vars]
    AeqPP = AConstraintEq[:, post_process]
    non_pp_solved_vector = solved_vector[non_pp_vars]

    # equalities constraint
    eq_bound_correction = AeqNonPP.dot(non_pp_solved_vector)
    new_eq = eq - eq_bound_correction

    # Extract sub matrice of AEqReorderedRef with columns corresponding to free variables not already computed
    # and the correspondings rows where these variables are involved.
    pp_rows = (AeqPP.getnnz(1) > 0).nonzero()[0]
    # AEqFree.eliminate_zeros()
    AeqPP = AeqPP[pp_rows, :]
    new_eq = new_eq[pp_rows]

    # option tout en même temps
    X = cvx.Variable(AeqPP.shape[1])
    AEqFree = cvx.Constant(AeqPP)

    lb = free_intervals[post_process, 0]
    ub = free_intervals[post_process, 1]

    prob = cvx.Problem(
        cvx.Minimize(cvx.Constant(0)),
        [
            AEqFree @ X == new_eq,
            X >= lb,
            X <= ub
        ]
    )
    try:
        prob.solve(solver=cvx.OSQP, verbose=False)
    except Exception:
        pass
    if X.value is not None:
        solved_vector[post_process] = X.value.tolist()


def compute_intervals_of_free_variables(
    ter_vectors: ndarray,
    solved_vector: ndarray,
    AEqReorderedRef: csr_matrix,
    AIneq: csr_matrix,
    already_computed_vars: ndarray,
    nb_measured: int
):
    ter_size = len(solved_vector)

    eq = AEqReorderedRef[:, ter_size].toarray().flatten()
    li = AIneq[:, ter_size].toarray().flatten()
    ui = AIneq[:, ter_size+1].toarray().flatten()

    AeqNotFree = AEqReorderedRef[:, already_computed_vars]
    AIneqNotFree = AIneq[:, already_computed_vars]

    already_computed_solved_vector = solved_vector[already_computed_vars]

    # equalities constraint
    eq_bound_correction = AeqNotFree.dot(already_computed_solved_vector)
    new_eq = eq - eq_bound_correction

    # inequalities constraints
    ineq_bound_correction = AIneqNotFree.dot(already_computed_solved_vector)
    new_li = li - ineq_bound_correction
    new_ui = ui - ineq_bound_correction

    # new_li = np.around(new_li, decimals=2)
    # new_ui = np.around(new_ui, decimals=2)

    # Computes indices of free variables not already computed
    free_indices = np.full(ter_size, True)
    free_indices[already_computed_vars] = False
    free_indices = free_indices.nonzero()[0]

    # Extract sub matrice of AEqReorderedRef with columns corresponding to free variables not already computed
    # and the correspondings rows where these variables are involved.
    AEqFree = AEqReorderedRef[:, free_indices]
    free_rows = (AEqFree.getnnz(1) > 0).nonzero()[0]
    AEqFree.eliminate_zeros()
    AEqFree = AEqFree[free_rows, :]
    new_eq = new_eq[free_rows]

    # In the inequalites constrains matrices keep rows and cols where the free variables not already computed
    # are involved
    AIneqFree = AIneq[:, free_indices]
    free_rows = (AIneqFree.getnnz(1) > 0).nonzero()[0]
    AIneqFree.eliminate_zeros()
    AIneqFree = AIneqFree[free_rows, :]
    new_li = new_li[free_rows]
    new_ui = new_ui[free_rows]

    intervals = np.copy(ter_vectors[2:4, :].transpose())

    new_intervals = mfa_problem_matrices.ineq_red(
        intervals[free_indices],
        vstack((AEqFree, AIneqFree)),
        np.hstack((new_eq, new_li)),
        np.hstack((new_eq, new_ui)),
    )
    intervals[free_indices] = new_intervals

    return intervals


def resolve_reduced_mfa_problem(
    rank_unmeasured: int,
    AEqReorderedRef: csc_matrix,
    AIneq: csc_matrix,
    nb_measured: int,
    ter_vectors_reordered: ndarray,
    determinable_col2row: dict
):
    ter_size = ter_vectors_reordered.shape[1]
    nb_unmeasured = ter_size-nb_measured
    ok = False

    # 1. There are two types of free variables
    # - Those which are in relation with measured variables
    # - Those which are in relation only with unmeasured variables (free or determinable)
    # For the equalities constraint we keep only the first type as they are the only one influencing
    # the optimisation result.
    # AUnmesauredRowMeasuredCol = AEqReorderedRef[:rank_unmeasured, nb_unmeasured:ter_size]
    # free_to_add_rows = (AUnmesauredRowMeasuredCol.getnnz(1) > 0).nonzero()[0]
    # determinate_rows = np.array(list(determinable_col2row.values()))
    # free_to_add_rows = np.setdiff1d(free_to_add_rows, determinate_rows)
    # free_to_post_process = (AUnmesauredRowMeasuredCol.getnnz(1) == 0).nonzero()[0]
    # su_trace.logger.debug(
    #     'There are ' + str(len(free_to_post_process)) + ' free variables out of ' +
    #     str(nb_free) + ' which can be post processed'
    # )
    # AFreeToAdd = AEqReorderedRef[free_to_add_rows, :][:, :nb_unmeasured]
    # free_to_add_cols = (AFreeToAdd.getnnz(0) > 0).nonzero()[0]
    free_to_add_cols = np.setdiff1d(
        np.array(range(nb_unmeasured), dtype=int),
        np.array(list(determinable_col2row.keys()), dtype=int)
    )
    free_to_add_rows = np.setdiff1d(
        np.array(range(rank_unmeasured), dtype=int),
        np.array(list(determinable_col2row.values()))
    )

    # 2. Initially the determinable variables to inject in the optimisation problem are
    # those which are implicated in inequality constraints
    determinable_to_add_rows = np.array([], dtype=int)
    determinable_to_add_cols = np.array([], dtype=int)
    determinable_cols = np.array(list(determinable_col2row.keys()), dtype=int)

    ineq_cols_to_add = (AIneq[:, :nb_unmeasured].getnnz(0) > 0).nonzero()[0]
    determinable_to_add_cols = np.intersect1d(ineq_cols_to_add, determinable_cols)
    determinable_to_add_rows = np.array(
        [determinable_col2row[determinate_col] for determinate_col in determinable_to_add_cols], dtype=int
    )

    # 3. add free variables wich are involved in inequalities constraint and not yet in the constraint matrix
    # as these variables are also involved in the equality constraint matrix we also add the corresponding rows and
    # col for this row
    # other_free_to_add_cols = np.setdiff1d(ineq_cols_to_add, determinable_to_add_cols)
    # other_free_to_add_rows = (AEqReorderedRef[:, other_free_to_add_cols].getnnz(1) > 0).nonzero()[0]
    # AFreeToAdd = AEqReorderedRef[other_free_to_add_rows, :][:, :nb_unmeasured]
    # free_to_add_cols = np.sort(np.unique(
    #     np.hstack((
    #         (AFreeToAdd.getnnz(0) > 0).nonzero()[0],
    #         other_free_to_add_cols,
    #         free_to_add_cols
    #     ))
    # ))

    # reordered_vars_type[free_to_add_cols] = 'libre*'  # to distinguish from those who are post processed

    reordered_solved_vector = np.empty(ter_size)
    reordered_solved_vector.fill(-1)

    # As all the determinable variables which are not involved in inequalities constraint are not
    # involved in the optimisation constraint they may have negative values. In this case they rare reinjected
    # in the problem and the optimisation is redone.
    while not ok:
        constrained_row_Aindices = np.unique(np.hstack([
            free_to_add_rows, determinable_to_add_rows,
            np.array([rank_unmeasured+i for i in range(AEqReorderedRef.shape[0]-rank_unmeasured)], dtype=int)
        ]))
        # Indices of variables in the optimisation process.
        # Size: free_to_add_cols + determinable_to_add_cols + nb_measured
        constrained_col_Aindices = np.unique(np.hstack([
            free_to_add_cols,
            determinable_to_add_cols,
            np.array([nb_unmeasured+i for i in range(nb_measured)])
        ]))
        SubConstraintEq = AEqReorderedRef[constrained_row_Aindices].transpose()[
            np.hstack((constrained_col_Aindices, [ter_size, ter_size+1]))
        ].transpose()
        SubConstraintIneq = AIneq[:, np.hstack((constrained_col_Aindices, [ter_size, ter_size+1]))]

        sub_ter_vectors_reordered = ter_vectors_reordered[:, constrained_col_Aindices]
        tk = time.time()

        # 4 Reconciliation on
        # 4.1 Computes measured redundant
        sub_reconciled_vector = Cvx_minimize(
            SubConstraintEq,
            SubConstraintIneq,
            sub_ter_vectors_reordered,
            len(free_to_add_cols)+len(determinable_to_add_cols)
        )
        su_trace.logger.info('Optimization problem SOLVED in ' + str(round(time.time()-tk, 2)) + ' sec')
        if sub_reconciled_vector is None:
            su_trace.logger.critical('Reconciliation failed')
            break

        # 4.2 Computes unknown observables
        determinate_col_Aindices, determinate_row_Aindices = \
            list(determinable_col2row.keys()), list(determinable_col2row.values())
        ADeterminableRowMeasuredCol = AEqReorderedRef[determinate_row_Aindices, :][:, -nb_measured-2:]
        rhs = ADeterminableRowMeasuredCol[:, -2].toarray().flatten()
        mul = ADeterminableRowMeasuredCol[:, :-2].dot(sub_reconciled_vector[-nb_measured:])
        observables = rhs-mul
        observables_lb = ter_vectors_reordered[LB][determinate_col_Aindices]
        diff_lb = observables-observables_lb
        tmp = np.where(diff_lb < -0.01, 1, 0)
        tmp = tmp.nonzero()[0]
        if len(tmp) != 0:
            determinable_to_add_cols = np.hstack((determinable_to_add_cols, np.array(determinate_col_Aindices)[tmp]))
            determinable_to_add_rows = np.array(
                [determinable_col2row[determinate_col] for determinate_col in determinable_to_add_cols]
            )
        else:
            ok = True
            reordered_solved_vector[constrained_col_Aindices] = sub_reconciled_vector
            reordered_solved_vector[determinate_col_Aindices] = observables
    return reordered_solved_vector, free_to_add_cols


def resolve_mfa_problem(
    rank_unmeasured: int,
    AEqReorderedRef: csc_matrix,
    AIneqReordered: csc_matrix,
    nb_measured: int,
    ter_vectors_reordered: ndarray,
    determinable_col2row: dict,
    reordered_vars_type: list,
    post_process: ndarray,
    full_ter_size: int,
    full_ter_vectors: ndarray,
    AConstraintEq: csc_matrix,
    AConstraintIneq: csc_matrix,
    mask_is_measured: ndarray,
    mask_is_not_measured: ndarray
):
    tk3 = time.time()
    # 3 Resolves MFA problem
    # if performance:
    reordered_solved_vector, free_solved_cols = resolve_reduced_mfa_problem(
        rank_unmeasured, AEqReorderedRef, AIneqReordered, nb_measured, ter_vectors_reordered,
        determinable_col2row
    )
    # reordered_solved_vector = np.around(reordered_solved_vector,decimals=2)
    # else:
    #     reordered_solved_vector = mfa_problem_solver.Cvx_minimize(
    #         AEqReorderedRef,
    #         ter_vectors_reordered,
    #         nb_unmeasured
    #     )
    ter_size = len(ter_vectors_reordered[0])
    nb_unmeasured = ter_size - nb_measured
    # 3 Computes unknown unobservables (free)  intervals
    if len(determinable_col2row)+nb_measured < ter_size:
        reordered_intervals = compute_intervals_of_free_variables(
            ter_vectors_reordered,
            reordered_solved_vector,
            AEqReorderedRef,
            AIneqReordered,
            np.sort(np.hstack((
                np.array(list(determinable_col2row.keys())),
                np.array(list(range(nb_unmeasured, ter_size)))
            ))),
            nb_measured
        )
    else:
        reordered_intervals = np.empty((ter_size, 2))
        reordered_intervals.fill(0)

    tk4 = time.time()
    su_trace.logger.info('------ Reconciliation done, took ' + str(round((tk4-tk3), 2)) + ' s ------')

    # full solved vectors: add post process variables (determinable or free)
    solved_vector = np.empty(full_ter_size)
    solved_vector[post_process] = -1
    solved_vector[mask_is_not_measured] = reordered_solved_vector[0:nb_unmeasured]
    solved_vector[mask_is_measured] = reordered_solved_vector[nb_unmeasured:]
    if len(post_process) > 0:
        intervals = np.copy(full_ter_vectors[2:4, :].transpose())
        compute_initial_value_pp_variables(
            full_ter_vectors,
            solved_vector,
            AConstraintEq,
            AConstraintIneq,
            post_process,
            nb_measured,
            intervals
        )

    tmp1, determinable_col2row, tmp3, new_vars_type, tmp4 = classify_with_matrix_reduction(
        AConstraintEq, sum(mask_is_measured)
    )
    intervals = compute_intervals_of_free_variables(
        full_ter_vectors,
        solved_vector,
        AConstraintEq,
        AConstraintIneq,
        np.sort(np.hstack((
            np.array(list(determinable_col2row.keys()), dtype=int),
            np.array(list(range(full_ter_size-nb_measured, full_ter_size)))
        ))),
        nb_measured
    )

    vars_type = np.empty(full_ter_size, dtype='object')
    vars_type[mask_is_not_measured] = reordered_vars_type[0:nb_unmeasured]
    vars_type[mask_is_measured] = reordered_vars_type[nb_unmeasured:]
    vars_type[post_process] = new_vars_type[post_process]

    # intervals = np.empty((full_ter_size, 2))
    intervals[mask_is_not_measured] = reordered_intervals[0:nb_unmeasured]
    intervals[mask_is_measured] = reordered_intervals[nb_unmeasured:ter_size]
    # intervals[post_process] = pp_intervals[post_process]

    return solved_vector, vars_type, intervals


def montecarlo(
    # reduced
    rank_unmeasured: int,
    AEqReorderedRef: csc_matrix,
    AIneqReordered: csc_matrix,
    nb_measured: int,
    ter_vectors_reordered: ndarray,
    determinable_col2row: dict,
    reordered_vars_type: list,
    # full
    post_process: ndarray,
    full_ter_size: int,
    full_ter_vectors: ndarray,
    AConstraintEq: csc_matrix,
    AConstraintIneq: csc_matrix,
    mask_is_measured: ndarray,
    mask_is_not_measured: ndarray,
    nb_realizations: int,
    sigmas_floor: float,
    downscale: bool,  # parameters
    montecarlo_upperlevel_results: dict
):
    t0 = time.time()

    mc_ter_vectors_reordered = np.copy(ter_vectors_reordered)
    mc_full_ter_vectors = np.copy(full_ter_vectors)
    reduced_ter_size = mc_ter_vectors_reordered.shape[1]

    mc_results = {
        'nb_simu': nb_realizations,
        'in': [],
        'out': [],
        'base_out': [],
        'mini': [],
        'maxi': []
    }

    su_trace.logger.info(f'Starts {nb_realizations} Montecarlo realizations')
    for nb in range(nb_realizations):
        tk1 = time.time()
        # self.mfa = cp.deepcopy(mfa)
        # if downscale:
        # replace geographical constraints with FR simu
        # self.mfa.cons = self.mfa.cons_without_geo
        # rd = np.random.randint(0, montecarlo_upperlevel_results['nb_simu']-1)
        # for fr_id, reg_ids in self.mfa.fr_compute_sym.items():
        #     Ai_row = {}
        #     for id in reg_ids:
        #         Ai_row[id] = 1
        #     li = montecarlo_upperlevel_results['base_out'][rd][fr_id] - self.mfa.tol
        #     ui = montecarlo_upperlevel_results['base_out'][rd][fr_id] + self.mfa.tol
        #     self.mfa.append_Ai(Ai_row, li=li, ui=ui, type='agg geo')
        # self.mfa.cons['Ai'].resize((len(self.mfa.cons['li']), self.scmfa.size))
        nb_reduced_unmeasured = full_ter_size - nb_measured
        for i in range(nb_reduced_unmeasured, reduced_ter_size):
            mc_ter_vectors_reordered[DATA][i] = truncated_gaussian_draw(
                ter_vectors_reordered[DATA][i], ter_vectors_reordered[SIGMA][i], 3
            )
        if sigmas_floor is not None:
            # floor for small sigmas
            mc_ter_vectors_reordered[SIGMA] = [
                s if s > sigmas_floor else sigmas_floor for s in mc_ter_vectors_reordered[SIGMA]
            ]

        mc_solved_vector, vars_type, mc_intervals = resolve_mfa_problem(
            rank_unmeasured,
            AEqReorderedRef,
            AIneqReordered,
            nb_measured,
            mc_ter_vectors_reordered,
            determinable_col2row,
            reordered_vars_type,
            post_process,
            full_ter_size,
            mc_full_ter_vectors,
            AConstraintEq,
            AConstraintIneq,
            mask_is_measured,
            mask_is_not_measured
        )

        mc_results['in'].append(mc_full_ter_vectors[DATA])
        mc_results['out'].append(mc_solved_vector.tolist())
        # mc_results['base_out'].append(solved_vector if not downscale else [])
        mc_results['mini'].append(mc_intervals[:, 0])
        mc_results['maxi'].append(mc_intervals[:, 1])

        if ((nb % int(nb_realizations / 10)) == 0):
            tk3 = time.time()
            su_trace.logger.info(f'Realisation {nb} done in ' + str(round(tk3-tk1, 2)) + ' / ' + str(round(tk3-t0, 2)))

    su_trace.logger.info('Montecarlo done')
    return mc_results


def truncated_gaussian_draw(
    mu: int,
    sigma: int,
    nb_sigmas: int
):
    draw = np.random.normal(mu, sigma)
    if abs(mu-draw) > nb_sigmas * sigma or draw <= 0:
        draw = truncated_gaussian_draw(mu, sigma, nb_sigmas)
    return draw
