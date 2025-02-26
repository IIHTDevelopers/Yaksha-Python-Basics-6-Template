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
    total_costs = {}
    for recipe, ingredients in recipes.items():
        cost = sum(ingredient_prices.get(ing, 0) * qty for ing, qty in ingredients.items())
        total_costs[recipe] = round(cost, 2)
    return total_costs

# Function 2: Normalize ingredient quantities using NumPy (Scaling factor: 1.5)
def normalize_quantities():
    matrix = df.to_numpy()  # Convert DataFrame to NumPy array
    scaled_matrix = matrix * 1.5
    return pd.DataFrame(scaled_matrix, index=df.index, columns=df.columns)

# Function 3: Unique ingredients across all recipes
def unique_ingredients():
    unique_set = set()
    for ingredients in recipes.values():
        unique_set.update(ingredients.keys())
    return unique_set

# Display results for manual testing (optional)
if __name__ == '__main__':
    print("\n--- Recipe Ingredient Data (Original) ---")
    print(df)

    print("\n--- Total Cost of Each Recipe ---")
    print(calculate_total_cost())

    print("\n--- Scaled Ingredient Quantities (1.5x) ---")
    print(normalize_quantities())

    print("\n--- Unique Ingredients Used in All Recipes ---")
    print(unique_ingredients())
