# test_recipe_management.py

import unittest
from io import StringIO
import sys
import os
import pandas as pd

# Add the parent directory to the Python path more explicitly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Importing functions from the recipe_management module
from recipe import calculate_total_cost, normalize_quantities, unique_ingredients
from test.TestUtils import TestUtils

class TestRecipeManagement(unittest.TestCase):

    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

    def test_calculate_total_cost(self):
        """
        Test for calculate_total_cost function
        """
        try:
            expected_costs = {
                "Pasta": 310,
                "Pizza": 725,
                "Salad": 645,
                "Soup": 420,
                "Cake": 800
            }
            result = calculate_total_cost()
            if result == expected_costs:
                self.test_obj.yakshaAssert("TestCalculateTotalCost", True, "functional")
                print("TestCalculateTotalCost = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateTotalCost", False, "functional")
                print("TestCalculateTotalCost = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateTotalCost", False, "exception")
            print(f"TestCalculateTotalCost = Failed ")

    def test_normalize_quantities(self):
        """
        Test for normalize_quantities function
        """
        try:
            # Expected scaled DataFrame
            df_original = pd.DataFrame({
                "Pasta": {"Flour": 200, "Eggs": 2, "Cheese": 50, "Milk": 100},
                "Pizza": {"Flour": 250, "Tomato": 100, "Cheese": 150, "Olives": 50},
                "Salad": {"Lettuce": 100, "Tomato": 150, "Cucumber": 100, "Cheese": 50},
                "Soup": {"Carrot": 200, "Potato": 150, "Onion": 100, "Garlic": 20},
                "Cake": {"Flour": 300, "Sugar": 200, "Butter": 150, "Eggs": 3}
            }).fillna(0)

            expected_scaled_df = df_original * 1.5
            result = normalize_quantities()
            if result.equals(expected_scaled_df):
                self.test_obj.yakshaAssert("TestNormalizeQuantities", True, "functional")
                print("TestNormalizeQuantities = Passed")
            else:
                self.test_obj.yakshaAssert("TestNormalizeQuantities", False, "functional")
                print("TestNormalizeQuantities = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestNormalizeQuantities", False, "exception")
            print(f"TestNormalizeQuantities = Failed ")

    def test_unique_ingredients(self):
        """
        Test for unique_ingredients function
        """
        try:
            expected_ingredients = {
                "Flour", "Eggs", "Cheese", "Milk",
                "Tomato", "Olives", "Lettuce", "Cucumber",
                "Carrot", "Potato", "Onion", "Garlic",
                "Sugar", "Butter"
            }
            result = unique_ingredients()
            if result == expected_ingredients:
                self.test_obj.yakshaAssert("TestUniqueIngredients", True, "functional")
                print("TestUniqueIngredients = Passed")
            else:
                self.test_obj.yakshaAssert("TestUniqueIngredients", False, "functional")
                print("TestUniqueIngredients = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestUniqueIngredients", False, "exception")
            print(f"TestUniqueIngredients = Failed ")


# test_sports_score_prediction.py

import unittest
import os
from io import StringIO
import sys
import pandas as pd

# Importing functions from the main module
from SportsScorePredictionSystem import predict_score, save_predictions, analyze_predictions, match_data

# Yaksha TestUtils for assertion
sys.path.append('..')
from test.TestUtils import TestUtils


class TestSportsScorePrediction(unittest.TestCase):

    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()
        # Setup a temporary CSV file for predictions
        self.test_filename = "test_predictions.csv"
        # Clear the file before each test
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_predict_score(self):
        """
        Test for predict_score function
        """
        try:
            # Test Cases
            test_cases = [
                {"prev_score": 65, "opp_strength": 70, "expected": 66},
                {"prev_score": 80, "opp_strength": 60, "expected": 76},
                {"prev_score": 55, "opp_strength": 75, "expected": 59},
                {"prev_score": 90, "opp_strength": 50, "expected": 82},
                {"prev_score": 70, "opp_strength": 65, "expected": 69}
            ]

            for case in test_cases:
                result = predict_score(case["prev_score"], case["opp_strength"])
                if result == case["expected"]:
                    self.test_obj.yakshaAssert("TestPredictScore", True, "functional")
                    print("TestPredictScore = Passed")
                else:
                    self.test_obj.yakshaAssert("TestPredictScore", False, "functional")
                    print("TestPredictScore = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestPredictScore", False, "exception")
            print(f"TestPredictScore = Failed ")

    def test_save_predictions(self):
        """
        Test for save_predictions function
        """
        try:
            predictions = save_predictions(match_data, self.test_filename)
            # Check if file is created
            self.assertTrue(os.path.exists(self.test_filename), "Predictions file was not created.")

            # Load the file and verify content
            df = pd.read_csv(self.test_filename)
            if len(df) == len(match_data) and "predicted_score" in df.columns:
                self.test_obj.yakshaAssert("TestSavePredictions", True, "functional")
                print("TestSavePredictions = Passed")
            else:
                self.test_obj.yakshaAssert("TestSavePredictions", False, "functional")
                print("TestSavePredictions = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSavePredictions", False, "exception")
            print(f"TestSavePredictions = Failed ")


    def tearDown(self):
        # Clean up the temporary CSV file after each test
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)


# test_loan_management.py

import unittest
from io import StringIO
import sys
import numpy as np

# Importing functions from the main module
from LoanManagementSystem import calculate_total_amount, display_loans, find_highest_repayment, loan_data

# Yaksha TestUtils for assertion
sys.path.append('..')
from test.TestUtils import TestUtils

class TestLoanManagement(unittest.TestCase):

    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()



    def test_display_loans(self):
        """
        Test for display_loans function
        """
        try:
            # Expected Output Lines
            expected_output = [
                "Loan ID: 101, Principal: $5000, Interest Rate: 5%, Tenure: 2 years, Total Repayment: $5500.00",
                "Loan ID: 102, Principal: $10000, Interest Rate: 4%, Tenure: 5 years, Total Repayment: $12000.00",
                "Loan ID: 103, Principal: $7500, Interest Rate: 6%, Tenure: 3 years, Total Repayment: $8850.00",
                "Loan ID: 104, Principal: $12000, Interest Rate: 3%, Tenure: 4 years, Total Repayment: $13440.00",
                "Loan ID: 105, Principal: $3000, Interest Rate: 7%, Tenure: 1 years, Total Repayment: $3210.00"
            ]

            # Call display_loans() and get the returned list
            result = display_loans(loan_data)

            # Compare the returned list with the expected output
            if result == expected_output:
                self.test_obj.yakshaAssert("TestDisplayLoans", True, "functional")
                print("TestDisplayLoans = Passed")
            else:
                self.test_obj.yakshaAssert("TestDisplayLoans", False, "functional")
                print("TestDisplayLoans = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestDisplayLoans", False, "exception")
            print(f"TestDisplayLoans = Failed ")

    def test_find_highest_repayment(self):
        """
        Test for find_highest_repayment function
        """
        try:
            # Highest repayment should be Loan ID 104
            expected_highest = [104, 12000, 3, 4]
            result = find_highest_repayment(loan_data)
            if list(result) == expected_highest:
                self.test_obj.yakshaAssert("TestFindHighestRepayment", True, "functional")
                print("TestFindHighestRepayment = Passed")
            else:
                self.test_obj.yakshaAssert("TestFindHighestRepayment", False, "functional")
                print("TestFindHighestRepayment = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestFindHighestRepayment", False, "exception")
            print(f"TestFindHighestRepayment = Failed ")

if __name__ == '__main__':
    # Create a test suite with all test classes
    test_suite = unittest.TestSuite()
    
    # Add tests from TestRecipeManagement
    test_suite.addTest(unittest.makeSuite(TestRecipeManagement))
    
    # Add tests from TestSportsScorePrediction
    test_suite.addTest(unittest.makeSuite(TestSportsScorePrediction))
    
    # Add tests from TestLoanManagement
    test_suite.addTest(unittest.makeSuite(TestLoanManagement))
    
    # Run the tests
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
