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
    total_amount = principal + (principal * rate / 100) * tenure
    return total_amount

# Function to display loan details and total repayment amounts
def display_loans(loan_data):
    loan_details = []
    for loan in loan_data:
        loan_id, principal, rate, tenure = loan
        total_amount = calculate_total_amount(principal, rate, tenure)
        loan_info = f"Loan ID: {loan_id}, Principal: ${principal}, Interest Rate: {rate}%, Tenure: {tenure} years, Total Repayment: ${total_amount:.2f}"
        print(loan_info)
        loan_details.append(loan_info)
    return loan_details

# Function to find the loan with the highest total repayment amount
def find_highest_repayment(loan_data):
    highest_loan = max(loan_data, key=lambda x: calculate_total_amount(x[1], x[2], x[3]))
    return highest_loan

# Main function to process loans
def process_loans():
    print("Loan Management System")
    loan_details = display_loans(loan_data)
    highest_loan = find_highest_repayment(loan_data)
    print(f"Loan with the highest repayment: {highest_loan[0]}")
    return loan_details, highest_loan

if __name__ == '__main__':
    process_loans()
