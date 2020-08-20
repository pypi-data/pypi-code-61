# coding: utf8
# contract_gen 2020-06-03 11:34:39.494947


__all__ = ["CalculationParams"]

from ...instrument import InstrumentCalculationParams
from . import CapFloorMarketDataRule


class CalculationParams(InstrumentCalculationParams):

    def __init__(
            self,
            market_data_rule=None,
            market_value_in_deal_ccy=None,
            skip_first_cap_floorlet=None,
            valuation_date=None
    ):
        super().__init__()
        self.market_data_rule = market_data_rule
        self.market_value_in_deal_ccy = market_value_in_deal_ccy
        self.skip_first_cap_floorlet = skip_first_cap_floorlet
        self.valuation_date = valuation_date

    @property
    def market_data_rule(self):
        """
        :return: object CapFloorMarketDataRule
        """
        return self._get_object_parameter(CapFloorMarketDataRule, "marketDataRule")

    @market_data_rule.setter
    def market_data_rule(self, value):
        self._set_object_parameter(CapFloorMarketDataRule, "marketDataRule", value)

    @property
    def market_value_in_deal_ccy(self):
        """
        MarketValueInDealCcy to override and that will be used as pricing analysis input to compute VolatilityPercent.
        Optional. No override is applied by default. Note that Premium takes priority over Volatility input.
        :return: float
        """
        return self._get_parameter("marketValueInDealCcy")

    @market_value_in_deal_ccy.setter
    def market_value_in_deal_ccy(self, value):
        self._set_parameter("marketValueInDealCcy", value)

    @property
    def skip_first_cap_floorlet(self):
        """
        Indicates whether to take in consideration the first caplet
        :return: bool
        """
        return self._get_parameter("skipFirstCapFloorlet")

    @skip_first_cap_floorlet.setter
    def skip_first_cap_floorlet(self, value):
        self._set_parameter("skipFirstCapFloorlet", value)

    @property
    def valuation_date(self):
        """
        The valuation date for pricing. 
        Optional. If not set the valuation date is equal to MarketDataDate or Today. For assets that contains a settlementConvention, the default valuation date  is equal to the settlementdate of the Asset that is usually the TradeDate+SettlementConvention.
        :return: str
        """
        return self._get_parameter("valuationDate")

    @valuation_date.setter
    def valuation_date(self, value):
        self._set_parameter("valuationDate", value)
