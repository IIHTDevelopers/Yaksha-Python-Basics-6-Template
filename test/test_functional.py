import unittest
import numpy as np
from LoanManagementSystem import (
    calculate_total_loan,
    
    find_least_tenure,
    loan_data
)


from test.TestUtils import TestUtils

class TestLoanManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.sample_data = np.array([
            [101, 'Alice', 5000, 5, 2],
            [102, 'Bob', 10000, 4.5, 5],
            [103, 'Charlie', 3000, 6, 1],
            [104, 'Diana', 8000, 3.5, 4],
            [105, 'Ethan', 4500, 5.2, 3]
        ], dtype=object)

    def test_total_loan_amount(self):
        try:
            result = calculate_total_loan(self.sample_data)
            self.assertEqual(result, 30500.0)
            self.test_obj.yakshaAssert("test_total_loan_amount", True, "functional")
            print("test_total_loan_amount = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_total_loan_amount", False, "exception")
            print("test_total_loan_amount = Failed")

    
    def test_least_tenure_customer(self):
        try:
            result = find_least_tenure(self.sample_data)
            self.assertEqual(result[1], "Charlie")
            self.assertEqual(int(result[4]), 1)
            self.test_obj.yakshaAssert("test_least_tenure_customer", True, "functional")
            print("test_least_tenure_customer = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_least_tenure_customer", False, "exception")
            print("test_least_tenure_customer = Failed")



import unittest
import pandas as pd
from SportsScore import (
    create_score_dataframe,
    get_average_score,
    count_players_above_age
)
from test.TestUtils import TestUtils

class TestScoreSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.df = create_score_dataframe()

    def test_get_average_score(self):
        try:
            expected_avg = (1200 + 980 + 750 + 1600 + 890) / 5  # 1084.0
            result = get_average_score(self.df)
            self.assertAlmostEqual(result, expected_avg, places=2)
            self.test_obj.yakshaAssert("test_get_average_score", True, "functional")
            print("test_get_average_score = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_get_average_score", False, "exception")
            print("test_get_average_score = Failed")

    def test_count_players_above_30(self):
        try:
            result = count_players_above_age(self.df, age=30)
            self.assertEqual(result, 3)  # Kohli, Rohit, Dhoni
            self.test_obj.yakshaAssert("test_count_players_above_30", True, "functional")
            print("test_count_players_above_30 = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_count_players_above_30", False, "exception")
            print("test_count_players_above_30 = Failed")

import unittest
import pandas as pd
from recipe import *
from test.TestUtils import TestUtils

class TestRecipeFileManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_obj = TestUtils()
        cls.filename = "recipes.txt"
        cls.expected_df = pd.DataFrame({
            'Recipe': ['Pasta', 'Salad', 'Pizza', 'Soup', 'Smoothie'],
            'Calories': [600, 150, 800, 250, 200],
            'Ingredients': [
                'Pasta, Tomato Sauce, Cheese',
                'Lettuce, Tomato, Cucumber',
                'Dough, Cheese, Sauce',
                'Broth, Carrot, Onion',
                'Banana, Milk, Honey'
            ]
        })

    def test_read_recipe_file(self):
        try:
            df = read_recipe_file(self.filename)
            self.assertTrue(isinstance(df, pd.DataFrame))
            self.assertEqual(df.shape, (5, 3))
            self.assertIn("Recipe", df.columns)
            self.test_obj.yakshaAssert("test_read_recipe_file", True, "functional")
            print("test_read_recipe_file = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_read_recipe_file", False, "exception")
            print("test_read_recipe_file = Failed")

    def test_get_high_calorie_recipes(self):
        try:
            df = read_recipe_file(self.filename)
            high_cal = get_high_calorie_recipes(df, 500)
            self.assertIn("Pizza", high_cal['Recipe'].values)
            self.assertIn("Pasta", high_cal['Recipe'].values)
            self.assertNotIn("Salad", high_cal['Recipe'].values)
            self.test_obj.yakshaAssert("test_get_high_calorie_recipes", True, "functional")
            print("test_get_high_calorie_recipes = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_get_high_calorie_recipes", False, "exception")
            print("test_get_high_calorie_recipes = Failed")

    def test_get_ingredients(self):
        try:
            df = read_recipe_file(self.filename)
            result = get_ingredients(df, "Pizza")
            self.assertEqual(result, "Dough, Cheese, Sauce")
            self.test_obj.yakshaAssert("test_get_ingredients", True, "functional")
            print("test_get_ingredients = Passed")
        except Exception:
            self.test_obj.yakshaAssert("test_get_ingredients", False, "exception")
            print("test_get_ingredients = Failed")


if __name__ == "__main__":
    unittest.main()
