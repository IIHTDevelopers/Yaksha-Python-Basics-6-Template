# loan_management.py

import numpy as np

# Loan ID, Principal Amount, Interest Rate (%), Tenure (Years)
loan_data = np.array([
    [101, 5000, 5, 2],
    [102, 10000, 4, 5],
    [103, 7500, 6, 3],
    [104, 12000, 3, 4],
    [105, 3000, 7, 1]
])

# Function to calculate total repayment amount
def calculate_total_amount(principal, rate, tenure):
    """
    Calculate the total repayment amount for a loan using the formula:
    total_amount = principal + (principal * rate / 100) * tenure

    Args:
        principal (float): The principal amount of the loan.
        rate (float): The interest rate as a percentage.
        tenure (int): The tenure of the loan in years.

    Returns:
        float: The total repayment amount.
    """
    # TODO: Implement the calculation logic
    pass

# Function to display loan details and total repayment amounts
def display_loans(loan_data):
    """
    Display the loan details and total repayment amounts for each loan.

    Args:
        loan_data (np.array): A NumPy array containing loan details.

    Returns:
        list: A list of strings containing loan information.
    """
    # TODO: Implement logic to display loan details
    pass

# Function to find the loan with the highest total repayment amount
def find_highest_repayment(loan_data):
    """
    Find the loan with the highest total repayment amount.

    Args:
        loan_data (np.array): A NumPy array containing loan details.

    Returns:
        np.array: The loan with the highest total repayment amount.
    """
    # TODO: Implement logic to find the loan with the highest repayment
    pass

# Main function to process loans
def process_loans():
    """
    Main function to execute the loan processing system.
    """
    print("Loan Management System")
    # TODO: Call display_loans() and find_highest_repayment() functions
    pass

# Execute the loan management system if this script is run directly
if __name__ == '__main__':
    process_loans()
