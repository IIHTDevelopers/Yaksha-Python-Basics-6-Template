import pandas as pd

# 1️⃣ TODO: Read recipe data from a text file and return as DataFrame use the recipes.txt
def read_recipe_file(filename):
    """
    Args:
        filename (str): Path to recipe file

    Returns:
        pd.DataFrame: DataFrame with columns ['Recipe', 'Calories', 'Ingredients']
    """
    # TODO: Read the file and construct a DataFrame
    pass

# 2️⃣ TODO: Filter recipes over a calorie threshold
def get_high_calorie_recipes(df, threshold=500):
    """
    Args:
        df (pd.DataFrame): DataFrame with recipe data
        threshold (int): Calorie threshold

    Returns:
        pd.DataFrame: Filtered recipes
    """
    # TODO: Filter rows where Calories > threshold
    pass

# 3️⃣ TODO: Return ingredients of a given recipe
def get_ingredients(df, recipe_name):
    """
    Args:
        df (pd.DataFrame): DataFrame with recipe data
        recipe_name (str): Recipe to look up

    Returns:
        str: Ingredients or "Recipe not found."
    """
    # TODO: Return the matching row's ingredients
    pass

# 🔍 Sample Execution
if __name__ == "__main__":
    df = read_recipe_file("recipes.txt")
    print("All Recipes:")
    print(df)

    print("\nHigh Calorie Recipes (>500):")
    print(get_high_calorie_recipes(df))

    print("\nIngredients for 'Pizza':")
    print(get_ingredients(df, "Pizza"))
