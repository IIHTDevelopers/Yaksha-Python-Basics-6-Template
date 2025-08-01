import pandas as pd

# ✅ Dataset is provided for learners to use
def create_score_dataframe():
    """
    Returns:
        pd.DataFrame: A DataFrame with columns ['Player', 'Age', 'Runs']
    """
    data = {
        "Player": ["Kohli", "Rohit", "Gill", "Dhoni", "Hardik"],
        "Age": [35, 36, 24, 42, 30],
        "Runs": [1200, 980, 750, 1600, 890]
    }
    return pd.DataFrame(data)


# TODO: Calculate the average runs scored by all players
def get_average_score(df):
    """
    Args:
        df (pd.DataFrame): DataFrame containing a 'Runs' column

    Returns:
        float: The average score of all players
    """
    # TODO: Calculate average from the 'Runs' column
    pass


# TODO: Count how many players are older than a given age (default: 30)
def count_players_above_age(df, age=30):
    """
    Args:
        df (pd.DataFrame): DataFrame with 'Age' column
        age (int): Age threshold. Default is 30.

    Returns:
        int: Number of players with age > given age
    """
    # TODO: Filter players older than `age` and return count
    pass


# 📌 Sample usage
if __name__ == "__main__":
    df = create_score_dataframe()
    print("Player Data:")
    print(df)

    avg_score = get_average_score(df)
    print(f"\nAverage Score of Players: {avg_score:.2f}")

    senior_count = count_players_above_age(df)
    print(f"Number of Players Aged Above 30: {senior_count}")
