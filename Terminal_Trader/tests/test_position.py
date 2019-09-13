from unittest import TestCase
from app import Position


class TestPosition(TestCase):

    def testPosition(self):
        position = Position()
        position.account_pk = 1
        self.assertEqual(position.tablename, "positions")
        self.assertEqual(position.fields, ['ticker', 'number_shares', 'account_pk'])
        self.assertIsInstance(position, Position)
        self.assertIsNone(position.ticker)
        self.assertEqual(position.account_pk, 1)

    def testCurrentVal(self):
        ibm = Position(ticker="ibm", number_shares=2)
        response = ibm.current_value()
        self.assertIsInstance(response, float)
