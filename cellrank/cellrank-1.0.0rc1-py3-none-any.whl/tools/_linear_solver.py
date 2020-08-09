# -*- coding: utf-8 -*-
"""Module containing anything related to linear solvers."""
from typing import List, Tuple, Union, TypeVar, Optional
from functools import singledispatch

import numpy as np
from scipy.linalg import solve
from scipy.sparse import eye as speye
from scipy.sparse import (
    issparse,
    spmatrix,
    csc_matrix,
    csr_matrix,
    isspmatrix_csc,
    isspmatrix_csr,
)
from scipy.sparse.linalg import inv as sinv
from scipy.sparse.linalg import gmres, lgmres, gcrotmk, bicgstab

from cellrank import logging as logg
from cellrank.utils._utils import _get_n_cores
from cellrank.utils._parallelize import parallelize

_DEFAULT_SOLVER = "gmres"
_PETSC_ERROR_MSG_SHOWN = False
_PETSC_ERROR_MSG = (
    "Unable to import petsc4py. "
    "For installation, please refer to: https://petsc4py.readthedocs.io/en/stable/install.html.\n"
    "Defaulting to `{!r}` solver."
)
_AVAIL_ITER_SOLVERS = {
    "gmres": gmres,
    "lgmres": lgmres,
    "bicgstab": bicgstab,
    "gcrotmk": gcrotmk,
}

LinSolver = TypeVar("LinSolver")
PETScMat = TypeVar("PETScMat")
Queue = TypeVar("Queue")


def _create_petsc_matrix(mat, as_dense: bool = False) -> PETScMat:
    from petsc4py import PETSc

    if issparse(mat) and as_dense:
        mat = mat.toarray()

    A = PETSc.Mat().create()
    if issparse(mat):
        if not isspmatrix_csr(mat):
            mat = csr_matrix(mat)
        A.createAIJ(size=mat.shape, csr=(mat.indptr, mat.indices, mat.data))
    else:
        A.createDense(mat.shape, array=mat)

    return A


def _create_solver(
    mat_a: Union[np.ndarray, spmatrix],
    solver: Optional[str],
    preconditioner: Optional[str],
    tol: float,
):
    from petsc4py import PETSc

    A = _create_petsc_matrix(mat_a)

    ksp = PETSc.KSP().create()
    ksp.setTolerances(rtol=tol)
    ksp.setType(solver if solver is not None else PETSc.KSP.Type.GMRES)
    if preconditioner is not None:
        ksp.getPC().setType(preconditioner)

    ksp.setOperators(A)

    x, b = A.getVecs()

    return ksp, x, b


@singledispatch
def _solve_many_sparse_problems_petsc(
    mat_b: csc_matrix,
    mat_a: Union[np.ndarray, spmatrix],
    solver: Optional[str] = None,
    preconditioner: Optional[str] = None,
    tol: float = 1e-5,
    queue: Optional[Queue] = None,
) -> Tuple[np.ndarray, int]:
    """
    Solver many problems using :module:`petsc4py` solver.

    Parameters
    ----------
    mat_b
        Matrix of shape `n x m`, with m << n.
    mat_a
        Matrix of shape `n x n`. We make no assumptions on `mat_a` being symmetric or positive definite.
    solver
        Solver to use. One of `petsc4py.PETSc.KSP.Type`. By default, use `PETSc.KSP.Type.GMRES`.
    preconditioner
        Preconditioner to use. If `None`, don't use any.
    tol
        Relative tolerance.
    queue
        Queue used to signal when a solution has been computed.

    Returns
    -------
    :class:`numpy.ndarray`
        Matrix of shape `n x m`. Each column in `mat_x` corresponds to the solution of one of the sub-problems
    int
        Number of converged solution.
    """
    raise NotImplementedError(f"Not implemented for type `{type(mat_b).__name__!r}`.")


@_solve_many_sparse_problems_petsc.register(np.ndarray)
def _(
    mat_b: np.ndarray,
    mat_a: Union[np.ndarray, spmatrix],
    solver: Optional[str] = None,
    preconditioner: Optional[str] = None,
    tol: float = 1e-5,
    _queue: Optional[Queue] = None,
) -> Tuple[np.ndarray, int]:
    if mat_b.ndim not in (1, 2) or (mat_b.ndim == 2 and mat_b.shape[1] != 1):
        raise ValueError(
            f"Expected either a vector or a matrix with 1 column, got `{mat_b.shape}`."
        )

    if solver == "direct":  # this can sometimes happen
        solver = None

    ksp, x, b = _create_solver(mat_a, solver, preconditioner=preconditioner, tol=tol)
    b.setArray(mat_b.squeeze())

    ksp.solve(b, x)

    return x.getArray().copy().squeeze(), int(ksp.converged)


@_solve_many_sparse_problems_petsc.register(csc_matrix)
def _(
    mat_b: csc_matrix,
    mat_a: Union[np.ndarray, spmatrix],
    solver: Optional[str],
    preconditioner: Optional[str],
    tol: float,
    queue: Queue,
) -> Tuple[np.ndarray, int]:
    from petsc4py import PETSc

    A = _create_petsc_matrix(mat_a)

    ksp = PETSc.KSP().create()
    ksp.setTolerances(rtol=tol)
    ksp.setType(solver if solver is not None else PETSc.KSP.Type.GMRES)
    if preconditioner is not None:
        ksp.getPC().setType(preconditioner)

    ksp.setOperators(A)

    ksp, x, b = _create_solver(mat_a, solver, preconditioner=preconditioner, tol=tol)
    xs, converged = [], 0

    for value in mat_b:
        x.set(1)  # reset the solution

        b.set(0)
        b.setValues(value.indices, value.data)

        ksp.solve(b, x)

        xs.append(x.getArray().copy().squeeze())
        converged += ksp.converged
        queue.put(1)

    queue.put(None)

    return np.stack(xs, axis=1), converged


def _solve_many_sparse_problems(
    mat_b: spmatrix, mat_a: spmatrix, solver: LinSolver, tol: float, queue: Queue,
) -> Tuple[np.ndarray, int]:
    """
    Solve `mat_a * x = mat_b` efficiently using an iterative solver.

    This is a utility function which is optimized for the case of `mat_a` and `mat_b` being sparse,
    and columns in `mat_b` being related. In that case, we can treat each column of `mat_b` as a
    separate linear problem and solve that efficiently using iterative solvers that exploit sparsity.

    Parameters
    ----------
    mat_b
        Matrix of shape `n x m`, with m << n.
    mat_a
        Matrix of shape `n x n`. We make no assumptions on `mat_a` being symmetric or positive definite.
    solver
        Solver to use for the linear problem. Valid options can be found in :func:`scipy.sparse.linalg`.
    tol
        Convergence threshold.
    queue
        Queue used to signal when a solution has been computed.

    Returns
    -------
    :class:`numpy.ndarray`
        Matrix of shape `n x m`. Each column in `mat_x` corresponds to the solution of one of the sub-problems
        defined via columns in `mat_b`.
    int
        Number of converged solutions.
    """

    # initialise solution list and info list
    x_list, n_converged = [], 0
    kwargs = {} if solver is not gmres else {"atol": "legacy"}  # get rid of the warning

    for b in mat_b:
        # actually call the solver for the current sub-problem
        x, info = solver(mat_a, b.toarray().flatten(), tol=tol, x0=None, **kwargs)

        # append solution and info
        x_list.append(x)
        n_converged += info == 0

        queue.put(1)

    queue.put(None)

    return np.stack(x_list, axis=1), n_converged


def _invert_matrix(mat, use_petsc: bool = True, **kwargs) -> np.ndarray:
    if use_petsc:
        try:
            import petsc4py  # noqa
        except ImportError:
            global _PETSC_ERROR_MSG_SHOWN
            if not _PETSC_ERROR_MSG_SHOWN:
                _PETSC_ERROR_MSG_SHOWN = True
                logg.warning(_PETSC_ERROR_MSG.format(_DEFAULT_SOLVER))
            kwargs["solver"] = _DEFAULT_SOLVER
            use_petsc = False

    if use_petsc:
        return _solve_lin_system(mat, speye(mat.shape[0]), use_petsc=True, **kwargs)

    return sinv(mat).toarray() if issparse(mat) else np.linalg.inv(mat)


def _petsc_mat_solve(
    mat_a: Union[np.ndarray, spmatrix],
    mat_b: Optional[Union[spmatrix, np.ndarray]] = None,
    tol: float = 1e-5,
    **kwargs,
) -> np.ndarray:
    from petsc4py import PETSc

    if mat_b is None:
        if mat_a.shape[0] != mat_a.shape[1]:
            raise ValueError("Matrix `A` is not square, unable to invert.")
        # matrix inversion
        B = PETSc.Mat().create()
        B.setSizes(mat_a.shape)
        B.setType(PETSc.Mat.Type.DENSE)
        B.setFromOptions()
        B.setUp()

        start, end = B.getOwnershipRange()
        for i in range(start, end):
            B[i, i] = 1
        B.assemble()
    else:
        if mat_b.ndim == 1 or (mat_b.ndim == 2 and mat_b.shape[1] == 1):
            if issparse(mat_b):
                mat_b = mat_b.toarray()

            res, converged = _solve_many_sparse_problems_petsc(
                mat_b, mat_a=mat_a, tol=tol, **kwargs
            )
            if not converged:
                logg.warning(
                    f"The solution for system "
                    f"`A{list(mat_a.shape)} * x[{mat_b.shape[0]}] = b[{mat_b.shape[0]}]` "
                    f"did not converge"
                )

            return res

        B = _create_petsc_matrix(mat_b, as_dense=True)

    A = _create_petsc_matrix(mat_a)

    x = PETSc.Mat().create()
    x.setSizes((A.getSize()[1], B.getSize()[1]))
    x.setType(PETSc.Mat.Type.DENSE)
    x.setFromOptions()
    x.setUp()
    x.assemble()

    ksp = PETSc.KSP().create()
    ksp.setType(PETSc.KSP.Type.PREONLY)
    ksp.setTolerances(rtol=tol)
    ksp.setOperators(A, A)

    pc = ksp.getPC()
    pc.setType(PETSc.PC.Type.LU)
    # TODO: investigate why it's slow and find best solver type
    # pc.setFactorSolverType(PETSc.Mat.SolverType.MUMPS)
    pc.setFromOptions()
    pc.setUp()

    ksp.setFromOptions()
    ksp.setUp()

    factored_matrix = pc.getFactorMatrix()

    # solve
    factored_matrix.matSolve(B, x)

    res = np.array(x.getDenseArray(), copy=True)

    if not ksp.converged:
        logg.warning(
            f"The solution for system "
            f"`A{list(A.getSize())} * X{list(x.getSize())} = B{list(B.getSize())}` "
            f"did not converge"
        )

    return res


def _solve_lin_system(
    mat_a: Union[np.ndarray, spmatrix],
    mat_b: Union[np.ndarray, spmatrix],
    solver: str = _DEFAULT_SOLVER,
    use_petsc: bool = False,
    preconditioner: Optional[str] = None,
    n_jobs: Optional[int] = None,
    backend: str = "multiprocessing",
    tol: float = 1e-5,
    use_eye: bool = False,
) -> np.ndarray:
    """
    Solve `mat_a * x = mat_b` efficiently using either iterative or direct methods.

    This is a utility function which is optimized for the case of `mat_a` and `mat_b` being sparse,
    and columns in `mat_b` being related. In that case, we can treat each column of `mat_b` as a
    separate linear problem and solve that efficiently using iterative solvers that exploit sparsity.

    If the columns of `mat_b` are related, we can use the solution of the previous problem as an
    initial guess for the next problem. Further, we parallelize the individual problems for each
    column in `mat_b` and solve them on separate kernels.

    In case `mat_a` is either not sparse, or very small, or `mat_b` has very many columns, it makes
    sense to use a direct solver instead which computes a matrix factorization and thereby solves all
    sub-problems at the same time.

    Parameters
    ----------
    mat_a
        Matrix of shape `n x n`. We make no assumptions on `mat_a` being symmetric or positive definite.
    mat_b
        Matrix of shape `n x m`, with m << n.
    solver
        Solver to use for the linear problem. Options are `['direct', 'gmres', 'lgmres', 'bicgstab', 'gcrotmk']`
        when :paramref:`use_petsc` or one of `petsc4py.PETSc.KPS.Type` otherwise.

        Information on the :module:`scipy` iterative solvers can be found in :func:`scipy.sparse.linalg` or
        for the :module:`petsc4py` solver in https://www.mcs.anl.gov/petsc/documentation/linearsolvertable.html.
    use_petsc
        Whether to use solvers from :module:`petsc4py` instead of :module:`scipy`. Recommended for large problems.
    preconditioner
        Preconditioner to use when :paramref:`use_petsc` `=True`.
        For available preconditioners, see `petsc4py.PETSc.PC.Type`.
    n_jobs
        Number of parallel jobs to use when :paramref:`use_petsc` `=True`. For small, quickly-solvable problems,
        we recommend high number (>=8) of cores in order to fully saturate them.
    backend
        Which backend to use for multiprocessing. See :class:`joblib.Parallel` for valid options.
    tol
        Convergence threshold.
    use_eye
        Solve `(I - mat_a) * x = mat_b` instead.

    Returns
    --------
    :class:`numpy.ndarray`
        Matrix of shape `n x m`. Each column corresponds to the solution of one of the sub-problems
        defined via columns in `mat_b`.
    """

    def extractor(
        res_converged: List[Tuple[np.ndarray, int]]
    ) -> Tuple[np.ndarray, int]:
        res, converged = zip(*res_converged)
        return np.hstack(res), sum(converged)

    n_jobs = _get_n_cores(n_jobs, n_jobs=None)

    if use_petsc:
        try:
            from petsc4py import PETSc  # noqa
        except ImportError:
            global _PETSC_ERROR_MSG_SHOWN
            if not _PETSC_ERROR_MSG_SHOWN:
                _PETSC_ERROR_MSG_SHOWN = True
                logg.warning(_PETSC_ERROR_MSG.format(_DEFAULT_SOLVER))
            solver = _DEFAULT_SOLVER
            use_petsc = False

    if use_eye:
        if issparse(mat_a):
            mat_a = speye(mat_a.shape[0]) - mat_a
        else:
            mat_a = np.eye(mat_a.shape[0]) - mat_a

    if solver == "direct" or n_jobs == 1:
        logg.debug("Solving the linear system using direct matrix factorization")

        if use_petsc:
            return _petsc_mat_solve(
                mat_a, mat_b, solver=solver, preconditioner=preconditioner, tol=tol
            )

        if issparse(mat_a):
            logg.debug("Densifying `A` for scipy direct solver")
            mat_a = mat_a.toarray()
        if issparse(mat_b):
            logg.debug("Densifying `B` for scipy direct solver")
            mat_b = mat_b.toarray()

        return solve(mat_a, mat_b)

    if use_petsc:
        if not isspmatrix_csr(mat_a):
            mat_a = csr_matrix(mat_a)

        mat_b = mat_b.T
        if not isspmatrix_csc(mat_b):
            mat_b = csc_matrix(mat_b)

        # as_array causes an issue, because it's called like this np.array([(NxM), (NxK), ....]
        # in the end, we want array of shape Nx(M + K + ...) - this is ensured by the extractor
        logg.debug(
            f"Solving the linear system using `PETSc` solver `{('gmres' if solver is None else solver)!r}` "
            f"on `{n_jobs}` core(s) with {'no' if preconditioner is None else preconditioner} preconditioner and "
            f"`tol={tol}`"
        )

        # can't pass PETSc matrix - not pickleable
        mat_x, n_converged = parallelize(
            _solve_many_sparse_problems_petsc,
            mat_b,
            n_jobs=n_jobs,
            backend=backend,
            as_array=False,
            extractor=extractor,
        )(mat_a, solver=solver, preconditioner=preconditioner, tol=tol)
    elif solver in _AVAIL_ITER_SOLVERS:
        if not issparse(mat_a):
            logg.debug("Sparsifying `A` for iterative solver")
            mat_a = csr_matrix(mat_a)

        mat_b = mat_b.T
        if not issparse(mat_b):
            logg.debug("Sparsifying `B` for iterative solver")
            mat_b = csr_matrix(mat_b)

        logg.debug(
            f"Solving the linear system using `scipy` solver `{solver!r}` on `{n_jobs} cores(s)` "
            f"with `tol={tol}`"
        )

        mat_x, n_converged = parallelize(
            _solve_many_sparse_problems,
            mat_b,
            n_jobs=n_jobs,
            backend=backend,
            as_array=False,
            extractor=extractor,
        )(mat_a, solver=_AVAIL_ITER_SOLVERS[solver], tol=tol)

    else:
        raise NotImplementedError(f"The solver `{solver!r}` was not found.")

    if n_converged != mat_b.shape[0]:
        logg.warning(f"`{mat_b.shape[0] - n_converged}` solution(s) did not converge")

    return mat_x
