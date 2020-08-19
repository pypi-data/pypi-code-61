
from ChosenAPI.function.common import CommonFunction


class RealTimeData(object):
    def __init__(self, classify):
        self.classify = classify

    def get_data(self):
        """
        :return:
        """
        obj = {"classify": self.classify}
        func = "real_time_trade"
        data = CommonFunction.send_data_by_post(obj, func)
        return data