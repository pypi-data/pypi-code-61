
import hashlib
from datetime import date
from typing import Any, Callable, Sequence, Dict

import pyotp
import requests

from .avanza_socket import AvanzaSocket
from .constants import (ChannelType, HttpMethod, InstrumentType, ListType,
                        OrderType, Route, TimePeriod)

BASE_URL = 'https://www.avanza.se'
MIN_INACTIVE_MINUTES = 30
MAX_INACTIVE_MINUTES = 60 * 24


class Avanza:
    def __init__(self, credentials):
        self._authenticationTimeout = MAX_INACTIVE_MINUTES
        self._session = requests.Session()

        response_body, credentials = self.__authenticate(credentials)

        self._credentials = credentials
        self._authentication_session = response_body['authenticationSession']
        self._push_subscription_id = response_body['pushSubscriptionId']
        self._customer_id = response_body['customerId']

        self._socket = AvanzaSocket(
            self._push_subscription_id,
            self._session.cookies.get_dict()
        )

    def __authenticate(self, credentials):
        if not MIN_INACTIVE_MINUTES <= self._authenticationTimeout <= MAX_INACTIVE_MINUTES:
            raise ValueError(f'Session timeout not in range {MIN_INACTIVE_MINUTES} - {MAX_INACTIVE_MINUTES} minutes')

        data = {
            'maxInactiveMinutes': self._authenticationTimeout,
            'username': credentials['username'],
            'password': credentials['password']
        }

        response = self._session.post(
            f'{BASE_URL}{Route.AUTHENTICATION_PATH.value}',
            json=data
        )

        response.raise_for_status()

        response_body = response.json()

        # No second factor required, continue with normal login
        if response_body.get('twoFactorLogin') is None:
            return response_body, credentials

        tfa_method = response_body['twoFactorLogin'].get('method')

        if tfa_method != 'TOTP':
            raise ValueError(
                f'Unsupported two factor method {tfa_method}'
            )

        return self.__validate_2fa(credentials)

    def __validate_2fa(self, credentials):
        totp = pyotp.TOTP(credentials['totpSecret'], digest=hashlib.sha1)
        totp_code = totp.now()

        if totp_code is None:
            raise ValueError('Failed to get totp code')

        response = self._session.post(
            f'{BASE_URL}{Route.TOTP_PATH.value}',
            json={
                'method': 'TOTP',
                'totpCode': totp_code
            }
        )

        response.raise_for_status()

        self._security_token = response.headers.get('X-SecurityToken')

        response_body = response.json()

        return response_body, credentials

    def __call(self, method: HttpMethod, path: str, options=None):
        method_call = {
            HttpMethod.GET: self._session.get,
            HttpMethod.POST: self._session.post,
            HttpMethod.PUT: self._session.put,
            HttpMethod.DELETE: self._session.delete
        }.get(method)

        if method_call is None:
            raise ValueError(f'Unknown method type {method}')

        response = method_call(
            f'{BASE_URL}{path}',
            json=options,
            headers={
                'X-AuthenticationSession': self._authentication_session,
                'X-SecurityToken': self._security_token
            }
        )

        response.raise_for_status()

        # Some routes like add/remove instrument from a watchlist
        # only returns 200 OK with no further data about if the operation succeded
        if len(response.content) == 0:
            return None

        return response.json()

    async def subscribe_to_id(
        self,
        channel: ChannelType,
        id: str,
        callback: Callable[[str, dict], Any]
    ):
        await self.subscribe_to_ids(channel, [id], callback)

    async def subscribe_to_ids(
        self,
        channel: ChannelType,
        ids: Sequence[str],
        callback: Callable[[str, dict], Any]
    ):
        if not callable(callback):
            raise ValueError('callback parameter has to be a function!')

        if not self._socket._connected:
            await self._socket.init()

        await self._socket.subscribe_to_ids(
            channel,
            ids,
            callback
        )

    def get_overview(self):
        """ Get overview for all accounts

        Returns:
            {
                'accounts': [{
                    'accountId': str,
                    'accountPartlyOwned': bool,
                    'accountType': str,
                    'active': bool,
                    'attorney': bool,
                    'buyingPower': float,
                    'depositable': bool,
                    'interestRate': float,
                    'name': str,
                    'ownCapital': float,
                    'performance': float,
                    'performancePercent': float,
                    'totalBalance': float,
                    'totalBalanceDue': float,
                    'totalProfit': float,
                    'totalProfitPercent': float,
                    'tradable': bool
                }],
                'numberOfDeals': int,
                'numberOfIntradayTransfers': int,
                'numberOfOrders': int,
                'numberOfTransfers': int,
                'totalBalance': float,
                'totalBuyingPower': float,
                'totalOwnCapital': float,
                'totalPerformance': float,
                'totalPerformancePercent': float
            }
        """
        return self.__call(HttpMethod.GET, Route.OVERVIEW_PATH.value)

    def get_account_overview(self, account_id: str):
        """ Get overview for a specific account

        Returns:
            {
                'accountId': str,
                'accountType': str,
                'accountTypeName': str,
                'accruedInterest': float,
                'allowMonthlySaving': bool,
                'availableSuperLoanAmount': float,
                'buyingPower': float,
                'clearingNumber': str,
                'courtageClass': str,
                'creditAfterInterest': float,
                'creditLimit': float,
                'currencyAccounts': [{
                    'balance': float,
                    'currency': str
                }],
                'depositable': bool,
                'forwardBalance': float,
                'instrumentTransferPossible': bool,
                'interestRate': float,
                'internalTransferPossible': bool,
                'jointlyOwned': bool,
                'numberOfDeals': int,
                'numberOfIntradayTransfers': int,
                'numberOfOrders': int,
                'numberOfTransfers': int,
                'overMortgaged': bool,
                'overdrawn': bool,
                'ownCapital': float,
                'performance': float,
                'performancePercent': float,
                'performanceSinceOneMonth': float,
                'performanceSinceOneMonthPercent': float,
                'performanceSinceOneWeek': float,
                'performanceSinceOneWeekPercent': float,
                'performanceSinceOneYear': float,
                'performanceSinceOneYearPercent': float,
                'performanceSinceSixMonths': float,
                'performanceSinceSixMonthsPercent': float,
                'performanceSinceThreeMonths': float,
                'performanceSinceThreeMonthsPercent': float,
                'performanceSinceThreeYears': float,
                'performanceSinceThreeYearsPercent': float,
                'reservedAmount': float,
                'sharpeRatio': float,
                'standardDeviation': float,
                'totalBalance': float,
                'totalCollateralValue': float,
                'totalPositionsValue': float,
                'totalProfit': float,
                'totalProfitPercent': float,
                'withdrawable': bool
            }
        """
        return self.__call(
            HttpMethod.GET,
            Route.ACCOUNT_OVERVIEW_PATH.value.format(
                account_id
            )
        )

    def get_watchlists(self):
        """ Get your "Bevakningslistor"

        Returns:
            [{
                'editable': bool,
                'id': str,
                'name': str,
                'orderbooks': List[str]
            }]
        """
        return self.__call(HttpMethod.GET, Route.WATCHLISTS_PATH.value)

    def add_to_watchlist(
        self,
        instrument_id: str,
        watchlist_id: str
    ) -> None:
        """ Add an instrument to the specified watchlist

            This function returns None if the request was 200 OK,
            but there is no guarantee that the instrument was added to the list,
            verify this by calling get_watchlists()
        """
        return self.__call(
            HttpMethod.PUT,
            Route.WATCHLISTS_ADD_DELETE_PATH.value.format(
                watchlist_id,
                instrument_id
            )
        )

    def remove_from_watchlist(
        self,
        instrument_id: str,
        watchlist_id: str
    ) -> None:
        """ Remove an instrument to the specified watchlist

            This function returns None if the request was 200 OK,
            but there is no guarantee that the instrument was removed from the list,
            verify this by calling get_watchlists()
        """
        return self.__call(
            HttpMethod.DELETE,
            Route.WATCHLISTS_ADD_DELETE_PATH.value.format(
                watchlist_id,
                instrument_id
            )
        )

    def get_fund_info(
        self,
        fund_id: str
    ):
        """ Get info about a fund

        Returns:
            {
                'NAV': float,
                'NAVLastUpdated': str,
                'administrators': str,
                'autoPortfolio': bool,
                'buyFee': float,
                'buyable': bool,
                'capital': float,
                'changeSinceOneDay': float,
                'changeSinceOneMonth': float,
                'changeSinceOneWeek': float,
                'changeSinceOneYear': float,
                'changeSinceSixMonths': float,
                'changeSinceThreeMonths': float,
                'changeSinceTurnOfTheYear': float,
                'description': str,
                'domicile': str,
                'fundCompany': {
                    'homePage': str,
                    'name': str
                },
                'hasInvestmentFees': bool,
                'id': str,
                'isin': str,
                'loanFactor': float,
                'managementFee': float,
                'name': str,
                'normanAmount': float,
                'numberOfOwners': int,
                'numberOfPriceAlerts': int,
                'otherFees': str,
                'positions': [{
                    'accountId': str,
                    'accountName': str,
                    'accountType': str,
                    'acquiredValue': float,
                    'averageAcquiredPrice': float,
                    'profit': float,
                    'profitPercent': float,
                    'value': float,
                    'volume': float
                }],
                'positionsTotalValue': float,
                'prospectus': str,
                'relatedFunds': [{
                    'changeSinceOneYear': float,
                    'id': str,
                    'name': str
                }],
                'risk': int,
                'riskLevel': str,
                'sellFee': float,
                'sellable': bool,
                'startDate': str,
                'subCategory': str,
                'tradingCurrency': str,
                'type': str
            }
        """

        return self.get_instrument(
            InstrumentType.FUND,
            fund_id
        )

    def get_stock_info(
        self,
        stock_id: str
    ):
        """ Returns info about a stock

        Returns:
            {
                'annualMeetings': [
                    {
                        'eventDate': str,
                        'extra': bool
                    }
                ],
                'brokerTradeSummary': {
                    'items': [
                        {
                            'brokerCode': str,
                            'buyVolume': int,
                            'netBuyVolume': int,
                            'sellVolume': int
                        }
                    ],
                    'orderbookId': str
                },
                'buyPrice': float,
                'change': float,
                'changePercent': float,
                'company': {
                    'CEO': str,
                    'chairman': str,
                    'description': str,
                    'id': str,
                    'marketCapital': int,
                    'marketCapitalCurrency': str,
                    'name': str,
                    'sector': str,
                    'stocks': [
                        {
                            'name': str,
                            'totalNumberOfShares': int
                        }
                    ],
                    'totalNumberOfShares': int
                },
                'companyReports': [{
                    'eventDate': str,
                    'reportType': str
                }],
                'country': str,
                'currency': str,
                'dividends': [{
                    'amountPerShare': float,
                    'currency': str,
                    'exDate': str,
                    'paymentDate': str
                }],
                'flagCode': str,
                'hasInvestmentFees': bool,
                'highestPrice': float,
                'id': str,
                'isin': str,
                'keyRatios': {
                    'directYield': float,
                    'priceEarningsRatio': float,
                    'volatility': float
                },
                'lastPrice': float,
                'lastPriceUpdated': str,
                'latestTrades': [],
                'loanFactor': float,
                'lowestPrice': float,
                'marketMakerExpected': bool,
                'marketPlace': str,
                'marketTrades': bool,
                'name': str,
                'numberOfOwners': int,
                'numberOfPriceAlerts': int,
                'orderDepthLevels': [
                    {
                        'buy': {
                            'percent': float,
                            'price': float,
                            'volume': int
                        },
                        'sell': {
                            'percent': float,
                            'price': float,
                            'volume': int
                        }
                    }
                ],
                'orderDepthReceivedTime': str,
                'positions': [],
                'positionsTotalValue': float,
                'priceAtStartOfYear': float,
                'priceFiveYearsAgo': float,
                'priceOneMonthAgo': float,
                'priceOneWeekAgo': float,
                'priceOneYearAgo': float,
                'priceSixMonthsAgo': float,
                'priceThreeMonthsAgo': float,
                'priceThreeYearsAgo': float,
                'pushPermitted': bool,
                'quoteUpdated': str,
                'relatedStocks': [{
                    'flagCode': str,
                    'id': str,
                    'lastPrice': float,
                    'name': str,
                    'priceOneYearAgo': float
                }],
                'sellPrice': float,
                'shortSellable': bool,
                'superLoan': bool,
                'tickerSymbol': str,
                'totalValueTraded': float,
                'totalVolumeTraded': int,
                'tradable': bool
            }
        """

        return self.get_instrument(
            InstrumentType.STOCK,
            stock_id
        )

    def get_certificate_info(
        self,
        certificate_id: str
    ):
        """ Returns info about a certificate

        Returns:
            {
                'administrationFee': float,
                'assetRootCategory': str,
                'assetSubCategory': str,
                'assetSubSubCategory': str,
                'change': float,
                'changePercent': float,
                'currency': str,
                'direction': str,
                'flagCode': str,
                'hasInvestmentFees': bool,
                'highestPrice': float,
                'id': str,
                'isin': str,
                'issuerName': str,
                'lastPrice': float,
                'lastPriceUpdated': str,
                'leverage': float,
                'lowestPrice': float,
                'marketPlace': str,
                'name': str,
                'numberOfPriceAlerts': int,
                'positions': List,
                'positionsTotalValue': float,
                'priceAtStartOfYear': float,
                'priceOneMonthAgo': float,
                'priceOneWeekAgo': float,
                'priceOneYearAgo': float,
                'priceSixMonthsAgo': float,
                'priceThreeMonthsAgo': float,
                'priipDocumentUrl': str,
                'prospectus': str,
                'pushPermitted': bool,
                'quoteUpdated': str,
                'shortName': str,
                'tickerSymbol': str,
                'totalValueTraded': float,
                'totalVolumeTraded': int,
                'tradable': bool,
                'underlyingCurrency': str
            }
        """

        return self.get_instrument(
            InstrumentType.CERTIFICATE,
            certificate_id
        )

    def get_warrant_info(
        self,
        warrant_id: str
    ):
        """ Returns info about a warrant

        Returns:
            {
                'callIndicator': str,
                'change': float,
                'changePercent': float,
                'currency': str,
                'direction': str,
                'endDate': str,
                'finalTerms': str,
                'flagCode': str,
                'hasInvestmentFees': bool,
                'highestPrice': float,
                'id': str,
                'isin': str,
                'issuerName': str,
                'lastPrice': float,
                'lastPriceUpdated': str,
                'lowestPrice': float,
                'marketPlace': str,
                'name': str,
                'numberOfPriceAlerts': int,
                'parity': float,
                'positions': [],
                'positionsTotalValue': float,
                'priceAtStartOfYear': float,
                'priceOneMonthAgo': float,
                'priceOneWeekAgo': float,
                'priceOneYearAgo': float,
                'priceSixMonthsAgo': float,
                'priceThreeMonthsAgo': float,
                'priipDocumentUrl': str,
                'pushPermitted': bool,
                'quoteUpdated': str,
                'strikePrice': int,
                'tickerSymbol': str,
                'totalValueTraded': float,
                'totalVolumeTraded': int,
                'tradable': bool,
                'underlyingCurrency': str,
                'underlyingOrderbook': {
                    'change': float,
                    'changePercent': float,
                    'currency': str,
                    'flagCode': str,
                    'highestPrice': float,
                    'id': str,
                    'lastPrice': float,
                    'lastPriceUpdated': str,
                    'lowestPrice': float,
                    'name': str,
                    'tickerSymbol': str,
                    'totalVolumeTraded': int,
                    'type': str,
                    'updated': str
                },
                'warrantType': str
            }
        """

        return self.get_instrument(
            InstrumentType.WARRANT,
            warrant_id
        )

    def get_index_info(
        self,
        index_id: str
    ):
        """ Returns info about an index

        Returns:
            {
                'change': float,
                'changePercent': float,
                'currency': str,
                'description': str,
                'flagCode': str
                'highestPrice': float,
                'id': str,
                'lastPrice': float,
                'lastPriceUpdated': str,
                'lowestPrice': float,
                'name': str,
                'numberOfPriceAlerts': int,
                'priceAtStartOfYear': float,
                'priceFiveYearsAgo': float,
                'priceOneMonthAgo': float,
                'priceOneWeekAgo': float,
                'priceOneYearAgo': float,
                'priceSixMonthsAgo': float,
                'priceThreeMonthsAgo': float,
                'priceThreeYearsAgo': float,
                'pushPermitted': bool,
                'quoteUpdated': str,
                'title': str
            }
        """

        return self.get_instrument(
            InstrumentType.INDEX,
            index_id
        )

    def get_instrument(
        self,
        instrument_type: InstrumentType,
        instrument_id: str
    ):
        """
            Get instrument info
            For more info on return models for this function see functions
            [
                get_stock_info(),
                get_fund_info(),
                get_certificate_info(),
                get_index_info(),
                get_warrant_info()
            ]
        """

        return self.__call(
            HttpMethod.GET,
            Route.INSTRUMENT_PATH.value.format(
                instrument_type.value,
                instrument_id
            )
        )

    def search_for_stock(
        self,
        query
    ):
        """ Search for a stock

        Args:
            query: can be a ISIN ('US0378331005'),
                name ('Apple'),
                tickerSymbol ('AAPL')

        Returns:
            {
                'totalNumberOfHits': int,
                'hits': [{
                    'instrumentType': 'STOCK',
                    'numberOfHits': int,
                    'topHits': [{
                        'currency': str,
                        'lastPrice': float,
                        'changePercent': float,
                        'tradable': bool,
                        'tickerSymbol': str,
                        'flagCode': Str,
                        'name': str,
                        'id': str
                    }]
                }]
            }
        """
        return self.search_for_instrument(
            InstrumentType.STOCK,
            query
        )

    def search_for_fund(
        self,
        query: str
    ):
        """ Search for a fund

        Args:
            query: can be a ISIN ('SE0012454338'),
                name ('Avanza'),
                tickerSymbol ('Avanza Europa')

        Returns:
            {
                'hits': [{
                    'instrumentType': 'FUND',
                    'numberOfHits': int,
                    'topHits': [{
                        'changeSinceOneDay': float,
                        'changeSinceOneYear': float,
                        'changeSinceThreeMonths': float,
                        'id': str,
                        'managementFee': float,
                        'name': str,
                        'risk': int,
                        'riskLevel': str,
                        'tickerSymbol': str,
                        'tradable': bool
                    }]
                }],
                'totalNumberOfHits': int
            }
        """

        return self.search_for_instrument(
            InstrumentType.FUND,
            query
        )

    def search_for_certificate(
        self,
        query: str
    ):
        """ Search for a certificate

        Args:
            query: can be a ISIN, name or tickerSymbol

        Returns:
            {
                'hits': [{
                    'instrumentType': 'CERTIFICATE',
                    'numberOfHits': int,
                    'topHits': [{
                        'changePercent': float,
                        'currency': str,
                        'flagCode': str,
                        'id': str,
                        'lastPrice': float,
                        'name': str,
                        'tickerSymbol': str,
                        'tradable': True
                    }]
                }],
                'totalNumberOfHits': 1
            }
        """

        return self.search_for_instrument(
            InstrumentType.CERTIFICATE,
            query
        )

    def search_for_warrant(
        self,
        query: str
    ):
        """ Search for a warrant

        Args:
            query: can be a ISIN, name or tickerSymbol

        Returns:
            {
                'hits': [{
                    'instrumentType': 'WARRANT',
                    'numberOfHits': int,
                    'topHits': [{
                        'changePercent': float,
                        'currency': str,
                        'flagCode': str,
                        'id': str,
                        'lastPrice': float,
                        'name': str,
                        'tickerSymbol': str,
                        'tradable': True
                    }]
                }],
                'totalNumberOfHits': int
            }
        """

        return self.search_for_instrument(
            InstrumentType.WARRANT,
            query
        )

    def search_for_instrument(
        self,
        instrument_type: InstrumentType,
        query: str
    ):
        """ Search for a specific instrument

        Returns:
            See the functions [
                search_for_stock(),
                search_for_fund(),
                search_for_certificate(),
                search_for_warrant()
            ]
            for more info about the return models
        """
        return self.__call(
            HttpMethod.GET,
            Route.INSTRUMENT_SEARCH_PATH.value.format(
                instrument_type.value.upper(),
                query
            )
        )

    def get_order_book(
        self,
        order_book_id: str,
        instrument_type: InstrumentType
    ):
        """ Get order book info

        Returns:
            {
                'account': {
                    'buyingPower': float,
                    'id': str,
                    'name': str,
                    'totalBalance': float,
                    'type': str
                },
                'fund': {
                    'NAV': float,
                    'buyFee': float,
                    'buyTradeDate': str,
                    'buyVisibleDate': str,
                    'id': str,
                    'loanFactor': float,
                    'managementFee': float,
                    'minStartAmount': float,
                    'name': str,
                    'otherFees': str,
                    'otherOrderDescription': str,
                    'positionValue': float,
                    'positionVolume': float,
                    'prospectus': str,
                    'sellFee': float,
                    'sellTradeDate': str,
                    'sellVisibleDate': str,
                    'stopTime': str,
                    'tradable': bool,
                    'type': str
                }
            }
        """
        return self.__call(
            HttpMethod.GET,
            Route.ORDERBOOK_PATH.value.format(
                instrument_type.value,
                order_book_id
            )
        )

    def get_order_books(
        self,
        order_book_ids: Sequence[str]
    ):
        """ Get info about multiple order books

        Returns:
            [{
                'changePercentOneYear': float,
                'changePercentPeriod': float,
                'changePercentThreeMonths': float,
                'currency': str,
                'id': str,
                'instrumentType': str,
                'lastUpdated': str,
                'managementFee': float,
                'minMonthlySavingAmount': float,
                'name': str,
                'prospectus': str,
                'rating': int,
                'risk': int,
                'tradable': bool
            }]
        """

        return self.__call(
            HttpMethod.GET,
            Route.ORDERBOOK_LIST_PATH.value.format(
                ','.join(order_book_ids)
            )
        )

    def get_positions(self):
        """ Get owned positions

        Returns:
            {
                'instrumentPositions': [{
                    'instrumentType': str,
                    'positions': [{
                        'accountId': str,
                        'accountName': str,
                        'accountType': str,
                        'acquiredValue': float,
                        'averageAcquiredPrice': float,
                        'change': float,
                        'changePercent': float,
                        'changePercentPeriod': float,
                        'changePercentThreeMonths': float,
                        'currency': str,
                        'depositable': bool,
                        'lastPrice': float,
                        'lastPriceUpdated': str,
                        'name': str,
                        'orderbookId': str,
                        'profit': float,
                        'profitPercent': float,
                        'tradable': bool,
                        'value': float,
                        'volume': float
                        }],
                    'todaysProfitPercent': float,
                    'totalProfitPercent': float,
                    'totalProfitValue': float,
                    'totalValue': float
                }],
                'totalBalance': float,
                'totalBuyingPower': float,
                'totalOwnCapital': float,
                'totalProfit': float,
                'totalProfitPercent': float
            }
        """

        return self.__call(HttpMethod.GET, Route.POSITIONS_PATH.value)

    def get_insights_report(
        self,
        account_id: str,
        time_period: TimePeriod
    ):
        """ Get report about the development of your owned positions during the specified timeperiod

        Returns:
            {
                'developmentResponse': {
                    'chartData': [{
                        'development': float,
                        'dividends': float,
                        'month': int,
                        'total': float,
                        'year': int
                    }],
                    'hasUnlistedInstrument': bool,
                    'instruments': [{
                        'instrumentDisplayName': str,
                        'instrumentType': str,
                        'outcome': {
                            'balanceDevelopments': List,
                            'development': float,
                            'dividends': float,
                            'total': float
                        },
                        'positions': [{
                            'currentPosition': float,
                            'endValue': float,
                            'isin': str,
                            'link': {
                                'buyable': bool,
                                'flagCode': str,
                                'linkDisplay': str,
                                'orderbookId': str,
                                'sellable': bool,
                                'shortLinkDisplay': str,
                                'tradeable': bool,
                                'type': str,
                                'urlDisplayName': str
                            },
                            'outcome': {
                                'balanceDevelopments': List,
                                'development': float,
                                'developmentPartOfTotalDevelopmentInPercent': float,
                                'dividends': float,
                                'dividendsPartOfTotalDevelopmentInPercent': float,
                                'stake': float,
                                'total': float,
                                'totalBuyAmount': float,
                                'totalDevelopmentInPercent': float,
                                'totalOtherAmount': float,
                                'totalSellAmount': float,
                                'totalTurnover': float,
                                'transactionTotals': [{
                                    'count': int,
                                    'presentableTransactionType': str,
                                    'totalAmount': str,
                                    'transactionType': str
                                }],
                                'transactions': [{
                                    'accountName': str,
                                    'amount': str,
                                    'date': str,
                                    'isin': str,
                                    'price': float,
                                    'type': str,
                                    'volume': float
                                }]
                            },
                            'shortName': str,
                            'startValue': float
                        }],
                        'totalOutcome': {
                            'development': float,
                            'dividends': float,
                            'total': float
                        },
                        'totalOutcomeForUnknownDevelopments': {
                            'development': float,
                            'dividends': float,
                            'total': float
                        },
                        'unknownPositionDevelopments': List
                    }],
                    'fromDate': str,
                    'otherTransactions': {
                        'otherTransactionsGroups': List,
                        'total': int
                    },
                    'totalDevelopment': {
                        'currentValue': float,
                        'startValue': float,
                        'totalChange': float
                    },
                    'transactionsResponse': {
                        'allTransactions': [{
                            'month': int,
                            'total': float,
                            'totalAutogiro': float,
                            'totalDeposits': float,
                            'totalWithdrawals': float,
                            'transactions': [{
                                'accountName': str,
                                'accountTypeName': str,
                                'amount': float,
                                'date': str,
                                'description': str,
                                'transactionType': str,
                                'transactionTypeName': str
                            }],
                            'year': int,
                            'yearMonth': str
                        }],
                        'chartData': [{
                            'allTransactions': float,
                            'autogiro': float,
                            'deposit': float,
                            'month': int,
                            'withdrawal': float,
                            'year': int
                        }],
                        'totalAll': float,
                        'totalAutogiro': float,
                        'totalDeposits': float,
                        'totalWithdraws': float
                    }
                }
            }
        """
        return self.__call(
            HttpMethod.GET,
            Route.INSIGHTS_PATH.value.format(
                time_period.value,
                account_id
            )
        )

    def get_deals_and_orders(self):
        """ Get currently active deals and orders

        Returns:
            {
                'accounts': [{'id': str, 'name': str', 'type': str}],
                'deals': [{
                    'account': {'id': str, 'name': str, 'type': str},
                    'dealId': str,
                    'dealTime': str,
                    'marketTransaction': bool,
                    'orderId': str,
                    'orderbook': {
                        'currency': str,
                        'id': str,
                        'marketPlace': str,
                        'name': str,
                        'type': str
                    },
                    'price': float,
                    'sum': float,
                    'type': str,
                    'volume': float
                }],
                'orders': [{
                    'account': {'id': str, 'name': str, 'type': str},
                    'deletable': bool,
                    'marketTransaction': bool,
                    'modifyAllowed': bool,
                    'orderDateTime': str,
                    'orderId': str,
                    'orderbook': {
                        'currency': str,
                        'id': str,
                        'marketPlace': str,
                        'name': str,
                        'type': str
                    },
                    'price': float,
                    'rawStatus': str,
                    'status': str,
                    'statusDescription': str,
                    'sum': float,
                    'transactionFees': {
                        'commission': float,
                        'fundOrderFee': {'rate': float, 'sum': float},
                        'marketFees': float,
                        'totalFees': float,
                        'totalSum': float,
                        'totalSumWithoutFees': float
                    },
                    'type': str,
                    'visibleOnAccountDate': str
                }],
                'reservedAmount': float
            }
        """
        return self.__call(
            HttpMethod.GET,
            Route.DEALS_AND_ORDERS_PATH.value
        )

    def get_inspiration_lists(self):
        """ Get all available inspiration lists

        This returns lists similar to the ones found on:

        https://www.avanza.se/aktier/aktieinspiration.html

        https://www.avanza.se/fonder/fondinspiration.html

        Returns:
            [{
                'averageChange': float,
                'averageChangeSinceThreeMonths': float,
                'highlightField': {'label': str, 'percent': bool},
                'id': str,
                'imageUrl': str,
                'information': str,
                'instrumentType': str,
                'name': str,
                'orderbooks': [{
                    'change': float,
                    'changePercent': float,
                    'currency': str,
                    'flagCode': str,
                    'highlightValue': int,
                    'id': str,
                    'lastPrice': float,
                    'name': str,
                    'priceOneYearAgo': float,
                    'priceThreeMonthsAgo': float,
                    'updated': str
                }],
                'statistics': {
                    'negativeCount': int,
                    'negativePercent': float,
                    'neutralCount': int,
                    'neutralPercent': float,
                    'positiveCount': int,
                    'positivePercent': float
                }
            }]
        """
        return self.__call(
            HttpMethod.GET,
            Route.INSPIRATION_LIST_PATH.value.format('')
        )

    def get_inspiration_list(self, list_type: ListType):
        """ Get inspiration list

        Returns:
            {
                'averageChangeSinceThreeMonths': float,
                'highlightField': {'label': str, 'percent': bool},
                'id': str,
                'imageUrl': str,
                'information': str,
                'instrumentType': str,
                'name': str,
                'orderbooks': [{
                    'changeSinceOneDay': float,
                    'changeSinceOneYear': float,
                    'changeSinceThreeMonths': float,
                    'highlightValue': int,
                    'id': str,
                    'lastUpdated': str,
                    'name': str
                }],
                'statistics': {
                    'negativeCount': int,
                    'negativePercent': float,
                    'neutralCount': int,
                    'neutralPercent': float,
                    'positiveCount': int,
                    'positivePercent': float
                }
            }
        """
        return self.__call(
            HttpMethod.GET,
            Route.INSPIRATION_LIST_PATH.value.format(
                list_type.value
            )
        )

    def get_chart_data(self, order_book_id: str, period: TimePeriod):
        """ Return chart data for an order book for the specified time period

        Returns:
            {
                'ceiling': float,
                'change': float,
                'changePercent': float,
                'comparisonName': str,
                'comparisonSeries': [{'timestamp': str, 'value': float}],
                'dataSeries': [{'timestamp': str, 'value': float}],
                'floor': float,
                'max': float,
                'min': float
            }
        """
        return self.__call(
            HttpMethod.GET,
            Route.CHARTDATA_PATH.value.format(
                order_book_id,
                period.value.lower()
            )
        )

    def place_order(
        self,
        account_id: str,
        order_book_id: str,
        order_type: OrderType,
        price: float,
        valid_until: date,
        volume: int
    ):
        """ Place an order

        Returns:
            {
                messages: List[str],
                orderId: str,
                requestId: str,
                status: str
            }
        """

        return self.__call(
            HttpMethod.POST,
            Route.ORDER_PLACE_PATH.value,
            {
                'accountId': account_id,
                'orderbookId': order_book_id,
                'orderType': order_type.value,
                'price': price,
                'validUntil': valid_until.isoformat(),
                'volume': volume
            }
        )

    def get_order(
        self,
        account_id: str,
        order_id: str
    ):
        """ Get an existing order

        Returns:
        {
            'account': {
                'buyingPower': float,
                'id': str,
                'name': str,
                'totalBalance': float,
                'type': str
            },
            'brokerTradeSummary': {
                'items': [{
                    'brokerCode': str,
                    'buyVolume': int,
                    'netBuyVolume': int,
                    'sellVolume': int
                }],
                'orderbookId': str
            },
            'customer': {
                'courtageClass': str,
                'showCourtageClassInfoOnOrderPage': bool
            },
            'firstTradableDate': str,
            'hasInstrumentKnowledge': bool,
            'hasInvestmentFees': {'buy': bool, 'sell': bool},
            'hasShortSellKnowledge': bool,
            'lastTradableDate': str,
            'latestTrades': [{
                'buyer': str,
                'cancelled': bool,
                'dealTime': str,
                'matchedOnMarket': bool,
                'price': float,
                'seller': str,
                'volume': int
            }],
            'marketMakerExpected': bool,
            'marketTrades': bool,
            'order': {
                'orderCondition': str,
                'orderType': str,
                'price': float,
                'validUntil': str,
                'volume': int
            },
            'orderDepthLevels': List,
            'orderDepthReceivedTime': str,
            'orderbook': {
                'change': float,
                'changePercent': float,
                'currency': str,
                'exchangeRate': float,
                'flagCode': str,
                'highestPrice': float,
                'id': str,
                'lastPrice': float,
                'lastPriceUpdated': str,
                'lowestPrice': float,
                'name': str,
                'positionVolume': float,
                'tickerSymbol': str,
                'totalValueTraded': float,
                'totalVolumeTraded': float,
                'tradable': bool,
                'tradingUnit': int,
                'type': str,
                'volumeFactor': float
            },
            'tickSizeRules': [{
                'maxPrice': int,
                'minPrice': int,
                'tickSize': int
            }],
            'untradableDates': List[str]
        }
        """

        return self.__call(
            HttpMethod.GET,
            Route.ORDER_GET_PATH.value.format(
                # Have tried this with three different instrument types
                # (STOCK, FUND, CERTIFICATE)
                # and it only seems to work when sending the instrument type
                # as STOCK
                InstrumentType.STOCK.value,
                account_id,
                order_id
            )
        )

    def delete_order(
        self,
        account_id: str,
        order_id: str
    ):
        """ Delete an existing order

        Returns:
            Returns:
            {
                messages: List[str],
                orderId: str,
                requestId: str,
                status: str
            }
        """
        return self.__call(
            HttpMethod.DELETE,
            Route.ORDER_DELETE_PATH.value.format(
                account_id,
                order_id
            )
        )

    def get_monthly_savings_by_account_id(
        self,
        account_id: str
    ):
        """ Get monthly savings at avanza for specific account

        Returns:
            {
                'monthlySavings': [{
                    'account': {
                        'id': str,
                        'name': str,
                        'type': str
                    },
                    'amount': float,
                    'cash': {'amount': float, 'percent': float},
                    'externalAccount': {
                        'accountNumber': str,
                        'bankName': str,
                        'clearingNumber': str
                    },
                    'fundDistributions': [{
                        'amount': float,
                        'orderbook': {
                            'buyable': bool,
                            'id': str,
                            'name': str
                        },
                        'percent': float
                    },
                    'id': str,
                    'name': str,
                    'purchaseDay': int,
                    'status': str,
                    'transferDay': int
                }],
                'totalAmount': float
            }
        """

        return self.__call(
            HttpMethod.GET,
            Route.MONTHLY_SAVINGS_PATH.value.format(account_id)
        )

    def get_all_monthly_savings(
        self
    ):
        """ Get your monthly savings at Avanza 

        Returns:
            {
                'monthlySavings': [{
                    'account': {
                        'id': str,
                        'name': str,
                        'type': str
                    },
                    'amount': float,
                    'cash': {'amount': float, 'percent': float},
                    'externalAccount': {
                        'accountNumber': str,
                        'bankName': str,
                        'clearingNumber': str
                    },
                    'fundDistributions': [{
                        'amount': float,
                        'orderbook': {
                            'buyable': bool,
                            'id': str,
                            'name': str
                        },
                        'percent': float
                    },
                    'id': str,
                    'name': str,
                    'purchaseDay': int,
                    'status': str,
                    'transferDay': int
                }],
                'totalAmount': float
            }
        """

        return self.__call(
            HttpMethod.GET,
            Route.MONTHLY_SAVINGS_PATH.value.format('')
        )

    def pause_monthly_saving(
        self,
        account_id: str,
        monthly_savings_id: str
    ):
        """ Pause an active monthly saving

        Returns:
            'OK'

        """

        return self.__call(
            HttpMethod.PUT,
            Route.MONTHLY_SAVINGS_PAUSE_PATH.value.format(
                account_id,
                monthly_savings_id
            )
        )

    def resume_monthly_saving(
        self,
        account_id: str,
        monthly_savings_id: str
    ):
        """ Resume a paused monthly saving

        Returns:
            'OK'

        """

        return self.__call(
            HttpMethod.PUT,
            Route.MONTHLY_SAVINGS_RESUME_PATH.value.format(
                account_id,
                monthly_savings_id
            )
        )

    def delete_monthly_saving(
        self,
        account_id: str,
        monthly_savings_id: str
    ) -> None:
        """ Deletes a monthly saving

        Returns:
            None

        """

        return self.__call(
            HttpMethod.DELETE,
            Route.MONTHLY_SAVINGS_REMOVE_PATH.value.format(
                account_id,
                monthly_savings_id
            )
        )

    def create_monthly_saving(
        self,
        account_id: str,
        amount: int,
        transfer_day_of_month: int,
        purchase_day_of_month: int,
        clearing_and_account_number: str,
        fund_distribution: Dict[str, int]
    ):
        """ Create a monthly saving at Avanza

        Args:
            account_id: The Avanza account to which the withdrawn money should be transferred to

            amount: minimum amount 100 (SEK)
                the amount that should be withdrawn from the external account every month

            transfer_day_of_month: valid range (1-31)
                when the money should be withdrawn from the external account

            purchase_day_of_month: valid range (1-31)
                when the funds should be purchased,
                must occur after the transfer_day_of_month

            clearing_and_account_number: The external account from which the money for the monthly savings should be withdrawn from,
                has to be formatted as follows 'XXXX-XXXXXXXXX'

            fund_distrubution: the percentage distribution of the funds
                The key is the funds id and the value is the distribution of the amount in a whole percentage
                The sum of the percentages has to total 100

                Examples:
                    {'41567': 100}
                    {'41567': 50, '878733': 50}
                    {'41567': 25, '878733': 75}

        Returns:
            {
                'monthlySavingId': str,
                'status': str
            }

            monthlySavingId has the following format: 'XX^XXXXXXXXXXXXX^XXXXXX'
            status should have the value 'ACCEPTED' if the monthly saving was created successfully
        """

        if not 1 <= transfer_day_of_month <= 31:
            raise ValueError(
                "transfer_day_of_month is outside the valid range of (1-31)")

        if not 1 <= purchase_day_of_month <= 31:
            raise ValueError(
                "purchase_day_of_month is outside the valid range of (1-31)")

        if transfer_day_of_month >= purchase_day_of_month:
            raise ValueError(
                "transfer_day_of_month must occur before purchase_day_of_month")

        if len(fund_distribution) == 0:
            raise ValueError(
                "No founds were specified in the fund_distribution"
            )

        if sum(fund_distribution.values()) != 100:
            raise ValueError("The fund_distribution values must total 100")

        return self.__call(
            HttpMethod.POST,
            Route.MONTHLY_SAVINGS_CREATE_PATH.value.format(account_id),
            {
                'amount': amount,
                'autogiro': {
                    'dayOfMonth': transfer_day_of_month,
                    'externalClearingAndAccount': clearing_and_account_number
                },
                'fundDistribution': {
                    'dayOfMonth': purchase_day_of_month,
                    'fundDistributions': fund_distribution
                }
            }
        )
