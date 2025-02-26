# recipe_management.py

import numpy as np
import pandas as pd

# Preset Recipe Data
recipes = {
    "Pasta": {"Flour": 200, "Eggs": 2, "Cheese": 50, "Milk": 100},
    "Pizza": {"Flour": 250, "Tomato": 100, "Cheese": 150, "Olives": 50},
    "Salad": {"Lettuce": 100, "Tomato": 150, "Cucumber": 100, "Cheese": 50},
    "Soup": {"Carrot": 200, "Potato": 150, "Onion": 100, "Garlic": 20},
    "Cake": {"Flour": 300, "Sugar": 200, "Butter": 150, "Eggs": 3}
}

# Ingredient Prices (Per unit in grams/ml)
ingredient_prices = {
    "Flour": 0.5, "Eggs": 5, "Cheese": 2, "Milk": 1,
    "Tomato": 1.5, "Olives": 3, "Lettuce": 1.2, "Cucumber": 2,
    "Carrot": 0.8, "Potato": 0.6, "Onion": 0.9, "Garlic": 4,
    "Sugar": 1.3, "Butter": 2.5
}

# Convert recipes to a Pandas DataFrame
df = pd.DataFrame(recipes).fillna(0)

# Function 1: Calculate total cost of each recipe
def calculate_total_cost():
    """
    Calculate the total cost of each recipe.

    Returns:
        dict: A dictionary with recipe names as keys and total costs as values.
    """
    # TODO: Implement total cost calculation logic
    pass

# Function 2: Normalize ingredient quantities using NumPy (Scaling factor: 1.5)
def normalize_quantities():
    """
    Normalize the ingredient quantities by a scaling factor of 1.5.

    Returns:
        pd.DataFrame: A DataFrame with scaled ingredient quantities.
    """
    # TODO: Implement normalization logic using NumPy
    pass

# Function 3: Unique ingredients across all recipes
def unique_ingredients():
    """
    Get the unique ingredients used across all recipes.

    Returns:
        set: A set of unique ingredient names.
    """
    # TODO: Implement logic to find unique ingredients
    pass

# Display results for manual testing (optional)
if __name__ == '__main__':
    print("\n--- Recipe Ingredient Data (Original) ---")
    print(df)

    print("\n--- Total Cost of Each Recipe ---")
    # TODO: Call calculate_total_cost() and print results
    pass

    print("\n--- Scaled Ingredient Quantities (1.5x) ---")
    # TODO: Call normalize_quantities() and print results
    pass

    print("\n--- Unique Ingredients Used in All Recipes ---")
    # TODO: Call unique_ingredients() and print results
    pass
