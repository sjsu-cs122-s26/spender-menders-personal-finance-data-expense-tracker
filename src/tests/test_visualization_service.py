import unittest
from unittest.mock import patch
import pandas as pd
from src.service.visualization_service import VisualizationService


# mock dataframe to simulate what get_transactions_merged_with_categories_df returns
MOCK_DATA = pd.DataFrame({
    'transaction_id': [1, 2, 3, 4, 5],
    'account_id':     [1, 1, 1, 1, 1],
    'cat_id':         [1, 2, 1, 3, 2],
    'name':  ['Food', 'Rent', 'Food', 'Transport', 'Rent'],
    'amount':         [100, 1200, 200, 50, 1200],
    'type':           ['expense', 'expense', 'expense', 'expense', 'income'],
    'date':           ['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-15', '2024-01-01'],
    'month':          ['January', 'January', 'February', 'February', 'January'],
    'description':    ['Groceries', 'Rent', 'Groceries', 'Bus', 'Salary']
})

class TestVisualizationService(unittest.TestCase):
    def setUp(self):
        # mock all dependencies so we dont need a real database
        with patch('src.service.visualization_service.AccountService'), \
             patch('src.service.visualization_service.CategoryService'), \
             patch('src.service.visualization_service.TransactionService'):
            self.viz_service = VisualizationService()

        # inject mock df directly, bypassing DB
        self.viz_service.df = MOCK_DATA.copy()

# ------------------------------------------------------------------------------------------------ #
#                                        Test requires_account                                     #
# ------------------------------------------------------------------------------------------------ #

    def test_requires_account_raises_when_df_is_none(self):
        self.viz_service.df = None
        with self.assertRaises(ValueError):
            self.viz_service.filter_by_expense_type()

    def test_requires_account_raises_on_all_methods(self):
        self.viz_service.df = None
        methods = [
            lambda: self.viz_service.filter_by_expense_type(),
            lambda: self.viz_service.filter_by_income_type(),
            lambda: self.viz_service.filter_by_category_for_expenses(1),
            lambda: self.viz_service.filter_by_month_for_expenses('January'),
            lambda: self.viz_service.get_unique_categories_for_expenses(),
            lambda: self.viz_service.get_unique_months_for_expenses(),
            lambda: self.viz_service.get_summed_expenses_by_category(),
            lambda: self.viz_service.get_summed_expenses(),
            lambda: self.viz_service.get_summed_income(),
            lambda: self.viz_service.get_summed_expenses_by_month(),
            lambda: self.viz_service.get_summed_expenses_by_category_over_time(),
        ]
        for method in methods:
            with self.assertRaises(ValueError):
                method()

# ------------------------------------------------------------------------------------------------ #
#                                          Test filters                                            #
# ------------------------------------------------------------------------------------------------ #

    def test_filter_by_expense_type_returns_only_expenses(self):
        df = self.viz_service.filter_by_expense_type()
        self.assertTrue((df['type'] == 'expense').all())

    def test_filter_by_expense_type_excludes_income(self):
        df = self.viz_service.filter_by_expense_type()
        self.assertFalse((df['type'] == 'income').any())

    def test_filter_by_income_type_returns_only_income(self):
        df = self.viz_service.filter_by_income_type()
        self.assertTrue((df['type'] == 'income').all())

    def test_filter_by_category_for_expenses(self):
        df = self.viz_service.filter_by_category_for_expenses(category_id=1)
        self.assertTrue((df['cat_id'] == 1).all())
        self.assertTrue((df['type'] == 'expense').all())

    def test_filter_by_month_for_expenses(self):
        df = self.viz_service.filter_by_month_for_expenses(month='January')
        self.assertTrue((df['month'] == 'January').all())
        self.assertTrue((df['type'] == 'expense').all())

# ------------------------------------------------------------------------------------------------ #
#                                        Test unique getters                                       #
# ------------------------------------------------------------------------------------------------ #

    def test_get_unique_categories_for_expenses(self):
        categories = self.viz_service.get_unique_categories_for_expenses()
        self.assertIn('Food', categories)
        self.assertIn('Rent', categories)
        self.assertNotIn('Drinks', categories)  # Transport is expense so should be there

    def test_get_unique_months_for_expenses(self):
        months = self.viz_service.get_unique_months_for_expenses()
        self.assertIn('January', months)
        self.assertIn('February', months)

# ------------------------------------------------------------------------------------------------ #
#                                        Test aggregations                                         #
# ------------------------------------------------------------------------------------------------ #

    def test_get_summed_expenses_by_category_returns_correct_columns(self):
        df = self.viz_service.get_summed_expenses_by_category()
        self.assertIn('name', df.columns)
        self.assertIn('amount', df.columns)

    def test_get_summed_expenses_by_category_sums_correctly(self):
        df = self.viz_service.get_summed_expenses_by_category()
        food_total = df[df['name'] == 'Food']['amount'].values[0]
        self.assertEqual(food_total, 300)  # 100 + 200

    def test_get_summed_expenses_returns_scalar(self):
        total = self.viz_service.get_summed_expenses()
        self.assertEqual(total, 1550)  # 100 + 1200 + 200 + 50

    def test_get_summed_income_returns_scalar(self):
        total = self.viz_service.get_summed_income()
        self.assertEqual(total, 1200)  # only income row

    def test_get_summed_expenses_by_month_returns_correct_columns(self):
        df = self.viz_service.get_summed_expenses_by_month()
        self.assertIn('month', df.columns)
        self.assertIn('amount', df.columns)

    def test_get_summed_expenses_by_month_sums_correctly(self):
        df = self.viz_service.get_summed_expenses_by_month()
        jan_total = df[df['month'] == 'January']['amount'].values[0]
        self.assertEqual(jan_total, 1300)  # 100 + 1200

    def test_get_summed_expenses_by_category_over_time_sorted_descending(self):
        df = self.viz_service.get_summed_expenses_by_category_over_time()
        amounts = df['amount'].tolist()
        self.assertEqual(amounts, sorted(amounts, reverse=True))  # check descending order

# ------------------------------------------------------------------------------------------------ #
#                                         Test edge cases                                          #
# ------------------------------------------------------------------------------------------------ #

    def test_empty_df_returns_empty_results(self):
        self.viz_service.df = pd.DataFrame(columns=MOCK_DATA.columns)
        df = self.viz_service.get_summed_expenses_by_category()
        self.assertTrue(df.empty)

    def test_no_expenses_returns_zero(self):
        self.viz_service.df = MOCK_DATA[MOCK_DATA['type'] == 'income'].copy()
        total = self.viz_service.get_summed_expenses()
        self.assertEqual(total, 0)

if __name__ == '__main__':
    unittest.main()