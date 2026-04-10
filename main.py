# DeFi Risk Analysis - Lending Strategy Simulation
# Author: Francisco A. Obregon

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Generate Simulated Data
# -----------------------------
def generate_data(days=100):
    np.random.seed(42)

    df = pd.DataFrame({
        "Day": range(1, days + 1),
        "APY": np.random.uniform(0.03, 0.20, days),       # 3% - 20%
        "Liquidity": np.random.uniform(0.2, 1.0, days),   # 0 (low) to 1 (high)
        "Volatility": np.random.uniform(0.1, 0.9, days)   # 0 (low) to 1 (high)
    })

    return df


# -----------------------------
# 2. Risk Score Calculation
# -----------------------------
def calculate_risk(df):
    df["Risk_Score"] = (
        (df["Volatility"] * 0.6) +
        ((1 - df["Liquidity"]) * 0.4)
    )

    # Normalize Risk Score (0–1)
    df["Risk_Score"] = (df["Risk_Score"] - df["Risk_Score"].min()) / (
        df["Risk_Score"].max() - df["Risk_Score"].min()
    )

    return df


# -----------------------------
# 3. Classify Risk Levels
# -----------------------------
def classify_risk(score):
    if score < 0.3:
        return "Low Risk"
    elif score < 0.6:
        return "Medium Risk"
    else:
        return "High Risk"


def apply_risk_labels(df):
    df["Risk_Level"] = df["Risk_Score"].apply(classify_risk)
    return df


# -----------------------------
# 4. Simulate Returns
# -----------------------------
def simulate_returns(df, initial_investment=1000):
    df["Daily_Return"] = df["APY"] / 365
    df["Portfolio_Value"] = initial_investment * (1 + df["Daily_Return"]).cumprod()
    return df


# -----------------------------
# 5. Stress Scenario Simulation
# -----------------------------
def apply_stress_scenario(df):
    df["Stress_Liquidity"] = df["Liquidity"]

    # Simulate liquidity crash (days 60–70)
    df.loc[60:70, "Stress_Liquidity"] = df.loc[60:70, "Liquidity"] * 0.3

    df["Stress_Risk"] = (
        (df["Volatility"] * 0.6) +
        ((1 - df["Stress_Liquidity"]) * 0.4)
    )

    return df


# -----------------------------
# 6. Summary Metrics
# -----------------------------
def print_summary(df):
    print("\n=== SUMMARY ===")
    print(f"Average APY: {round(df['APY'].mean() * 100, 2)}%")
    print(f"Average Risk Score: {round(df['Risk_Score'].mean(), 2)}")
    print(f"High Risk Days: {len(df[df['Risk_Level'] == 'High Risk'])}")


# -----------------------------
# 7. Visualization
# -----------------------------
def plot_results(df):

    # Portfolio Growth
    plt.figure()
    plt.plot(df["Day"], df["Portfolio_Value"])
    plt.title("Portfolio Growth Over Time")
    plt.xlabel("Day")
    plt.ylabel("Portfolio Value")
    plt.show()

    # Risk Score
    plt.figure()
    plt.plot(df["Day"], df["Risk_Score"])
    plt.title("Risk Score Over Time")
    plt.xlabel("Day")
    plt.ylabel("Risk Score")
    plt.show()

    # APY vs Risk
    plt.figure()
    plt.scatter(df["APY"], df["Risk_Score"])
    plt.title("APY vs Risk")
    plt.xlabel("APY")
    plt.ylabel("Risk Score")
    plt.show()


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    df = generate_data()
    df = calculate_risk(df)
    df = apply_risk_labels(df)
    df = simulate_returns(df)
    df = apply_stress_scenario(df)

    print_summary(df)
    plot_results(df)


if __name__ == "__main__":
    main()