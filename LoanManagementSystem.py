import numpy as np

# Dataset: [Customer ID, Name, Loan Amount, Interest Rate %, Tenure in Years]
loan_data = np.array([
    [101, 'Alice', 5000, 5, 2],
    [102, 'Bob', 10000, 4.5, 5],
    [103, 'Charlie', 3000, 6, 1],
    [104, 'Diana', 8000, 3.5, 4],
    [105, 'Ethan', 4500, 5.2, 3]
], dtype=object)

# 1️⃣ TODO: Calculate the total loan amount taken by all customers
def calculate_total_loan(data):
    """
    Args:
        data (np.ndarray): 2D array with loan records

    Returns:
        float: Sum of all loan amounts
    """
    # TODO: Extract and sum up all loan amounts (column index 2)
    pass

# 2️⃣ TODO: Find the customer with the least repayment years
def find_least_tenure(data):
    """
    Args:
        data (np.ndarray): 2D array with loan records

    Returns:
        list: The record of the customer with the shortest loan tenure
    """
    # TODO: Use min() with key on tenure (column index 4)
    pass

# 🔍 Sample usage (keep this unchanged)
def main():
    total_loan = calculate_total_loan(loan_data)
    print(f"Total Loan Amount Taken by All Customers: ${total_loan}")

    fastest = find_least_tenure(loan_data)
    print(f"Customer with Shortest Repayment Period: {fastest[1]} ({fastest[4]} years)")

if __name__ == "__main__":
    main()
