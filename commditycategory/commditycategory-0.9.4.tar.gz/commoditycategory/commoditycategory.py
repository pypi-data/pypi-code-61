# Copyright (c) 2020-present, bywin, Inc.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from gensim.models.fasttext import FastText as FT_gensim

class CommodityCategory():
    """

    Attributes
    ----------


    """

    def __init__(self):
        self.model = FT_gensim.load("allwancibiao_tb_FT")

    def get_model(self):
        return self.model

    def most_similar(self, str):
        return self.model.most_similar(str)