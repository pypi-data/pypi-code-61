"""Generation of Chains and their characterization

(Chain: a subset of the set of objects, mutually comparable)
"""


class Chain:
    """CHAIN calculation

    (Chain: a subset of the set of objects, mutually comparable)

    """

    def __init__(self, csv, matrix, cov):
        """
        :param matrix: reduced data matrix derived from csv
        :type matrix: object of class Matrix

        :param csv: source data with all informations
        :type csv: object of Class CSV
        """

        self.matrix = matrix
        self.matrix.obj = matrix.obj  # 14.07.2020  Das ist falsch!!!!
        self.csv = csv
        self.cov = cov
        self.gr = {}

    def connectivity(self, firstobjidx, secondobjidx):
        """Central method of class chain
        :param csv: instance of inputclass
        :param cov: cover matrix no care how oriented
        :param firstobject: label of first object
        :param secondobject: label of second object
        :return npathtest: =[] if there is no connection,
                           else: a list of lists
        :return flagch: =0 if no connection, else 1
        """
        graph = self.generate_dict_of_graph()
        flagch = 1
        npathtest = self.find_all_paths(
            graph, firstobjidx, secondobjidx
        )  # inserted graph
        if npathtest == []:
            npathtest = self.find_all_paths(graph, secondobjidx, firstobjidx)
            # 13.05.2020 the idea is that
            # both orientations are to be checked
            if npathtest == []:
                flagch = 0
        return npathtest, flagch

    def generate_dict_of_graph(self):
        """A dictionary is generated from a cover matrix
        (row < column-label then 1 else 0)
        :param cov: cover-matrix
        :param r: dimension of the square matrix covd
        :var gr: dictionary , needed for the find_path routines
        :return: gr
        :rtyp: dictionary
        """
        r = self.matrix.rows  # 15.07.2020
        for i1 in range(0, r):
            li = []
            for i2 in range(0, r):
                if self.cov[i1][i2] == 1:
                    li.append(i2)
            self.gr[i1] = li
        return self.gr

    def find_all_paths(
        self, graph, startobjidx, sinkobjidx, path=None
    ):  # graph inserted
        """Finds all paths between start and sink of a directed graph
         Python-course 2007: find shortest path in a directed graph
        :param graph: dictionary with the incidences of cover matrix
        :param startobjidx: starting vertex index
        :param sinkobjidx: endpoint indexof the path
        :param path: encapsulated list of paths
        """
        if not path:
            path = []
        # 13.05.2020 Comment elim
        path = path + [startobjidx]
        if startobjidx == sinkobjidx:
            return [path]
        if startobjidx not in self.gr:
            return []
        paths = []
        for node in self.gr[startobjidx]:
            if node not in path:
                newpaths = self.find_all_paths(
                    graph, node, sinkobjidx, path
                )  # graph inserted
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def searchlongchains(self, list1ofelements, list2ofelements):
        """ From the 'list1ofelements' and
        'list2ofelements' those elements are identified which
        have 'long' chains
        :param list1ofelements: Most often the maximal elements
        :param list2ofelements: Most often the minimal elements
        :param candidates: (Return) First element startelement,\
                                second element sinkelement,\
                                third element length of chain
        """
        chainheighttest = []
        for elem1 in list1ofelements:
            # names --> idx
            elem1idx = self.matrix.obj.index(elem1)
            for elem2 in list2ofelements:
                # names --> idx
                elem2idx = self.matrix.obj.index(elem2)
                npathtest, flagch = self.connectivity(elem1idx, elem2idx)
                for inp in range(0, len(npathtest)):
                    chainheighttest.append((len(npathtest[inp]), elem1, elem2))
        lch = len(chainheighttest)
        mwchainheight = 0
        for i in range(0, lch):
            mwchainheight += chainheighttest[i][0]
        if lch != 0:  # new 13.07.2020
            mwchainheight = 1.0 * mwchainheight / (1.0 * lch)
            mwchheight = round(mwchainheight, 3)
        else:
            mwchainheight = (
                # if  there is no chain of length >= 1 then
                # length=0 and mwch = 0 too
                0
            )
            mwchheight = 0
        candidatepairs = []
        for i in range(0, lch):
            if chainheighttest[i][0] >= mwchainheight:
                candidatepairs.append(
                    (
                        chainheighttest[i][1],
                        chainheighttest[i][2],
                        chainheighttest[i][0],
                    )
                )

        return candidatepairs, mwchheight

    def search_statistics(self, list1ofelements,
                          list2ofelements, candidatepairs):
        """ candidatepairs will be scanned to get
        pairs of objects with long chains
        :param list1ofelements: Most often the
                maximal elements
        :param list2ofelements: most often the
                minimal elements
        :param candidatepairs: outcome of 'searchlongchains'
         """
        countelementpairs = []
        for elem1 in list1ofelements:
            for elem2 in list2ofelements:
                countpairs = 0
                for i in range(0, len(candidatepairs)):
                    if (elem1 == candidatepairs[i][0]) and (
                        elem2 in candidatepairs[i][1]
                    ):
                        countpairs += 1
                countelementpairs.append((elem1, elem2, countpairs))
        return countelementpairs

    def chainheight(self, startobjidx, sinkobjidx, maxch):
        """ Calculates chain of height 'maxch'
        :param r:number of representants (in actual calls: rred)
        :param cov: cover.matrix  (from Order)
        :param startobjidx: label of a vertex in Hasse diagram
        :param sinkobjidx: label of a vertex in Hasse diagram
        :param maxch: input by the user. Required height of chains
        :param chset: sets of elements of chains with height = maxch
        :param matrix.obj: list of representants (object-short-names)
        :var paths: an encapsulated field of chains between startpoint
                     and sinkpoint
        :var count_of_chains: how many chains of length maxch
        :var length_of_chains: = maxch
        """
        self.maxch = maxch
        paths, flch = self.connectivity(startobjidx, sinkobjidx)
        chset = []
        if flch != 0:
            # lp is the number of all paths
            # between start- and sinkpoint (labels)
            lp = len(paths)
            # Not all paths are of interest,
            # only such having the height maxch
            countpath = []
            for i in range(0, lp):
                if len(paths[i]) == self.maxch:
                    countpath.append(i)
            lcp = len(countpath)
            # lcp is the number of chains with the length maxch
            # having the length = maxch(maxch: user input)
            # countpath is a vector of the chain-numbers
            # ...having the length = maxch
            # sets of elements of chains of height maxch, "chset"
            zahl = 0
            for i in countpath:
                chset.append(set([]))
                for j in range(0, maxch):
                    chset[zahl].add(self.matrix.obj[paths[i][j]])
                zahl += 1
                # count_of_chains: an important result
            count_of_chains = zahl  # 15.07.2020 not zahl+1 but just zahl
        else:
            count_of_chains = 0
            lcp = 0
        return count_of_chains, lcp, chset

    def chainsimilarity(self, chset, lcp):
        """the results of chainheight will be used to calculate

        the similarity between any two chains.
        similarity analysis by construction of a
        similarity matrix whose entries are
        Tanimoto-like coefficients
        :param chset: the set of chains with a certain length
        :param lcp:
        """

        chainm = []
        for i1 in range(0, lcp):
            chainm.append(0)
            chainm[i1] = []
            for i2 in range(0, lcp):
                tmp = (
                    1.0
                    * len(chset[i1] & chset[i2])
                    / (1.0 * len(chset[i1] | chset[i2]))
                )
                chainm[i1].append(round(tmp, 3))
                # a representation as a text and as a histogram would be useful

        return chainm

    def chain_graphics(self, count_of_chains, chainm):
        """Interface to graphics and textual - output

        There are coc rows of (in most general case) different lengths
        the symmetric matrix chainm will be reformulated as...
        ... a vector of length lcp*(lcp - 1)/2
        coc: count of chains, given a start and a sink point

        Two outputs:
        a) Id.no of chain and the chain: self.chset
        b) bar diagram with values taken from  self.vec_chainm
           ... Ordinate = chain_similarity
           ... Abscissa the Pairs in self.vec_chainm
        """
        coc = count_of_chains
        vec_chainm = []
        chainlist = []
        for i1 in range(0, coc):
            for i2 in range(i1 + 1, coc):
                vec_chainm.append(chainm[i1][i2])
                chainlist.append((i1, i2))
        name_of_ordinate = "chain-similarity"
        return (coc, name_of_ordinate, vec_chainm, chainlist)
