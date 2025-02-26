# Sports Score Prediction System

import numpy as np
import pandas as pd

# Preset match data (Team, Previous Score, Opponent Strength)
match_data = [
    {"team": "Team A", "prev_score": 65, "opp_strength": 70},
    {"team": "Team B", "prev_score": 80, "opp_strength": 60},
    {"team": "Team C", "prev_score": 55, "opp_strength": 75},
    {"team": "Team D", "prev_score": 90, "opp_strength": 50},
    {"team": "Team E", "prev_score": 70, "opp_strength": 65}
]

# Predict score using a simple model (prev_score * 0.8 + opp_strength * 0.2)
def predict_score(prev_score, opp_strength):
    return int(prev_score * 0.8 + opp_strength * 0.2)

# Save match predictions to CSV
def save_predictions(match_data, filename="predictions.csv"):
    predictions = []
    for match in match_data:
        predicted_score = predict_score(match["prev_score"], match["opp_strength"])
        match["predicted_score"] = predicted_score
        predictions.append(match)

    pd.DataFrame(predictions).to_csv(filename, index=False)
    return predictions

# Analyze the predictions and find the highest predicted scorer
def analyze_predictions(filename="predictions.csv"):
    df = pd.read_csv(filename)
    print("\nPredicted Scores:\n", df)

    max_score_row = df.loc[df["predicted_score"].idxmax()]
    print(f"\nHighest Predicted Scorer: {max_score_row['team']} with {max_score_row['predicted_score']} points.")

# Main function to process predictions
def sports_score_prediction():
    print("Sports Score Prediction System\n")
    predictions = save_predictions(match_data)
    analyze_predictions()

sports_score_prediction()

