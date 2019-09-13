from unittest import TestCase
from app.trade import Trade


class TestTrade(TestCase):

    def testTrade(self):
        trade = Trade(ticker='aaaaaaaaa', number_shares=12)
        trade.save()
        test = Trade.one_from_where_clause("WHERE ticker=?", ('aaaaaaaaa',))
        self.assertIsInstance(test, Trade)
        self.assertEqual(test.number_shares, 12)
