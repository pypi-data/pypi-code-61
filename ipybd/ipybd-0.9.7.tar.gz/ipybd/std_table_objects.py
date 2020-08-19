from ipybd.core import RestructureTable
from ipybd.std_table_terms import *


class OccurrenceRecord(RestructureTable):
    def __init__(self, io):
        self.new_columns = OccurrenceTerms
        super(OccurrenceRecord, self).__init__(io)


class KingdoniaPlant(RestructureTable):
    def __init__(self, io):
        self.new_columns = KingdoniaPlantTerms
        super(KingdoniaPlant, self).__init__(io, fcol = True)
        self.meger_mult_idents()

    # Kingdonia 系统可以同时导入多个鉴定，每个鉴定及其相关信息组成一个json array
    # [['Murdannia undulata', '洪德元', '1974-01-01 00:00:01', 'type']]
    def meger_mult_idents(self):
        self.df['identifications'] = list(map(lambda v:[v], self.df['identifications']))
