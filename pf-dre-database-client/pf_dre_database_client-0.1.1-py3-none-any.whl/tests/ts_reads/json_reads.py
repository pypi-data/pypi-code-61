# Built-in Modules
from datetime import datetime, timedelta
from unittest import TestCase

# Project Specific Modules
from mms.util import helpers
from mms import TimescaleClientJSON


class TestDataReads(TestCase):
    def setUp(self):
        # self.pr = cProfile.Profile()
        # self.pr.enable()
        # print("\n<<<---")
        self.clientArgs = helpers.get_db_client_kwargs()

    def tearDown(self):
        # p = Stats(self.pr)
        # p.strip_dirs()
        # p.sort_stats('cumtime')
        # p.print_stats(20)
        # print("\n--->>")
        return

    def test_latest_metrics(self):
        device_ids = [398]
        device_metrics = ['P', 'Q', 'S']

        c = TimescaleClientJSON('device_metrics_json',
                                **helpers.get_db_client_kwargs())
        df = c.get_latest_metrics(device_ids, device_metrics, 5)
        # This should pass assuming all the mock meters being pointed to are
        # being polled correctly.
        self.assertEquals(len(device_ids)*len(device_metrics), len(df.index))

    def test_all_metrics(self):
        device_ids = [398]
        device_metrics = ['P', 'Q', 'S']

        c = TimescaleClientJSON('device_metrics_json',
                                **helpers.get_db_client_kwargs())
        c.get_all_metrics(device_ids, device_metrics,
                          (datetime.now() - timedelta(minutes=5)).isoformat(),
                          datetime.now().isoformat())

    def test_aggregated_metrics(self):
        device_ids = [398]
        device_metrics = ['P']

        c = TimescaleClientJSON('device_metrics_json',
                                **helpers.get_db_client_kwargs())
        # First
        c.get_aggregated_metrics(
            '5 minutes', device_ids, device_metrics,
            (datetime.now() - timedelta(minutes=15)).isoformat(),
            datetime.now().isoformat(), 'first')

        # Last
        c.get_aggregated_metrics(
            '5 minutes', device_ids, device_metrics,
            (datetime.now() - timedelta(minutes=15)).isoformat(),
            datetime.now().isoformat(), 'last')

        # Average
        c.get_aggregated_metrics(
            '5 minutes', device_ids, device_metrics,
            (datetime.now() - timedelta(minutes=15)).isoformat(),
            datetime.now().isoformat(), 'avg')

        # Last Observation Carried Forward (10 minutes into future)
        c.get_aggregated_metrics(
            '5 minutes', device_ids, device_metrics,
            (datetime.now() - timedelta(minutes=15)).isoformat(),
            (datetime.now() + timedelta(minutes=10)).isoformat(),
            'avg', 'interpolate')

        # Interpolate (10 minutes into future)
        c.get_aggregated_metrics(
            '5 minutes', device_ids, device_metrics,
            (datetime.now() - timedelta(minutes=15)).isoformat(),
            (datetime.now() + timedelta(minutes=10)).isoformat(),
            'avg', 'locf')
