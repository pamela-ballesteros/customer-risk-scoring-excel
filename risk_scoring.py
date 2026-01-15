import pandas as pd

# -----------------------------
# Data loaded
# -----------------------------
FILE_PATH = "customer_risk_scoring.xlsx"
SHEET_NAME = "customer_data"

df = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)

# -----------------------------
# 2) Parameters (can be adjusted)
# -----------------------------
w_txn = 0.4
w_amt = 0.4
w_country = 0.2

threshold_review = 0.45
threshold_medium = 0.20

# -----------------------------
# 3) Normalize (0–1) like Excel MIN/MAX
# -----------------------------
def minmax(series: pd.Series) -> pd.Series:
    s_min = series.min()
    s_max = series.max()
    if s_max == s_min:
        # Avoid divide-by-zero if all values are identical
        return series.apply(lambda _: 0.0)
    return (series - s_min) / (s_max - s_min)

df["txn_norm"] = minmax(df["txn_count"])
df["amt_norm"] = minmax(df["avg_txn_amount"])

# -----------------------------
# 4) Risk score
# -----------------------------
df["risk_score"] = (w_txn * df["txn_norm"]) + (w_amt * df["amt_norm"]) + (w_country * df["high_risk_country"])

# -----------------------------
# 5) Threshold-based action
# -----------------------------
def action(score: float) -> str:
    if score >= threshold_review:
        return "Review"
    if score >= threshold_medium:
        return "Monitor"
    return "No Action"

df["recommended_action"] = df["risk_score"].apply(action)
df["predicted_flag"] = (df["risk_score"] >= threshold_review).astype(int)

# -----------------------------
# 6) Sort + summary
# -----------------------------
df = df.sort_values("risk_score", ascending=False)

review_count = (df["recommended_action"] == "Review").sum()
total = len(df)

print(f"Recommended for review: {review_count}/{total} ({review_count/total:.1%})")
print("\nTop 10 highest risk customers:")
print(df[["customer_id", "risk_score", "recommended_action"]].head(10).to_string(index=False))

# -----------------------------
# 7) Save outputs
# -----------------------------
df.to_csv("risk_scoring_output.csv", index=False)
print("\nSaved: risk_scoring_output.csv")

