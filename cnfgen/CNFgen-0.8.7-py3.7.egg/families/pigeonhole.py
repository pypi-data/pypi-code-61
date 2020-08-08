#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Implementation of the pigeonhole principle formulas
"""

from cnfgen.cnf import CNF
from cnfgen.graphs import bipartite_sets

from cnfgen.graphs import neighbors
from itertools import combinations, product


def PigeonholePrinciple(pigeons, holes, functional=False, onto=False):
    """Pigeonhole Principle CNF formula

    The pigeonhole  principle claims  that no M  pigeons can sit  in N
    pigeonholes  without collision  if M>N.   The  counterpositive CNF
    formulation  requires  such mapping  to  be  satisfied. There  are
    different  variants of this  formula, depending  on the  values of
    `functional` and `onto` argument.

    - PHP: pigeon can sit in multiple holes
    - FPHP: each pigeon sits in exactly one hole
    - onto-PHP: pigeon can  sit in multiple holes, every  hole must be
                covered.
    - Matching: one-to-one bijection between pigeons and holes.

    Arguments:
    - `pigeon`: number of pigeons
    - `hole`:   number of holes
    - `functional`: add clauses to enforce at most one hole per pigeon
    - `onto`: add clauses to enforce that any hole must have a pigeon

    >>> print(PigeonholePrinciple(4,3).dimacs(export_header=False))
    p cnf 12 22
    1 2 3 0
    4 5 6 0
    7 8 9 0
    10 11 12 0
    -1 -4 0
    -1 -7 0
    -1 -10 0
    -4 -7 0
    -4 -10 0
    -7 -10 0
    -2 -5 0
    -2 -8 0
    -2 -11 0
    -5 -8 0
    -5 -11 0
    -8 -11 0
    -3 -6 0
    -3 -9 0
    -3 -12 0
    -6 -9 0
    -6 -12 0
    -9 -12 0
    """
    def var_name(p, h):
        return 'p_{{{0},{1}}}'.format(p, h)

    if functional:
        if onto:
            formula_name = "Matching"
        else:
            formula_name = "Functional pigeonhole principle"
    else:
        if onto:
            formula_name = "Onto pigeonhole principle"
        else:
            formula_name = "Pigeonhole principle"

    description = "{0} formula for {1} pigeons and {2} holes".format(
        formula_name, pigeons, holes)
    php = CNF(description=description)

    if pigeons < 0 or holes < 0:
        raise ValueError(
            "Number of pigeons and holes must both be non negative")

    mapping = php.unary_mapping(range(1, pigeons + 1),
                                range(1, holes + 1),
                                var_name=var_name,
                                injective=True,
                                functional=functional,
                                surjective=onto)

    for v in mapping.variables():
        php.add_variable(v)

    for c in mapping.clauses():
        php.add_clause_unsafe(c)

    return php


def GraphPigeonholePrinciple(graph, functional=False, onto=False):
    """Graph Pigeonhole Principle CNF formula

    The graph pigeonhole principle CNF formula, defined on a bipartite
    graph G=(L,R,E), claims that there is a subset E' of the edges such that
    every vertex on the left size L has at least one incident edge in E' and
    every edge on the right side R has at most one incident edge in E'.

    This is possible only if the graph has a matching of size |L|.

    There are different variants of this formula, depending on the
    values of `functional` and `onto` argument.

    - PHP(G):  each left vertex can be incident to multiple edges in E'
    - FPHP(G): each left vertex must be incident to exaclty one edge in E'
    - onto-PHP: all right vertices must be incident to some vertex
    - matching: E' must be a perfect matching between L and R

    Arguments:
    - `graph` : bipartite graph
    - `functional`: add clauses to enforce at most one edge per left vertex
    - `onto`: add clauses to enforce that any right vertex has one incident edge


    Remark: the graph vertices must have the 'bipartite' attribute
    set. Left vertices must have it set to 0 and the right ones to
    1. A KeyException is raised otherwise.

    """
    def var_name(p, h):
        return 'p_{{{0},{1}}}'.format(p, h)

    if functional:
        if onto:
            formula_name = "Graph matching"
        else:
            formula_name = "Graph functional pigeonhole principle"
    else:
        if onto:
            formula_name = "Graph onto pigeonhole principle"
        else:
            formula_name = "Graph pigeonhole principle"

    description = "{0} formula on {1}".format(formula_name, graph.name)
    gphp = CNF(description=description)

    Left, Right = bipartite_sets(graph)

    mapping = gphp.unary_mapping(Left,
                                 Right,
                                 sparsity_pattern=graph,
                                 var_name=var_name,
                                 injective=True,
                                 functional=functional,
                                 surjective=onto)

    for v in mapping.variables():
        gphp.add_variable(v)

    for c in mapping.clauses():
        gphp.add_clause_unsafe(c)

    return gphp


def BinaryPigeonholePrinciple(pigeons, holes):
    """Binary Pigeonhole Principle CNF formula

    The pigeonhole principle claims that no M pigeons can sit in
    N pigeonholes without collision if M>N. This formula encodes the
    principle using binary strings to identify the holes.

    Parameters
    ----------
    pigeon : int
       number of pigeons
    holes : int
       number of holes
    """

    description = "Binary Pigeonhole Principle for {0} pigeons and {1} holes".format(
        pigeons, holes)
    bphp = CNF(description=description)

    if pigeons < 0 or holes < 0:
        raise ValueError(
            "Number of pigeons and holes must both be non negative")

    bphpgen = bphp.binary_mapping(range(1, pigeons + 1),
                                  range(1, holes + 1),
                                  injective=True)

    for v in bphpgen.variables():
        bphp.add_variable(v)

    for c in bphpgen.clauses():
        bphp.add_clause_unsafe(c)

    return bphp
