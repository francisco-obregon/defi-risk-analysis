# DeFi Lending Risk Analysis

## 📌 Overview

This project presents a simplified risk analysis framework for a DeFi (Decentralized Finance) lending strategy. It simulates how yield, liquidity, and market volatility interact, and evaluates whether a strategy is truly attractive when considering both return and risk.

The objective is to move beyond headline returns (APY) and assess how sustainable those returns are under different market conditions, including stress scenarios.

---

## 🎯 Objectives

- Analyze the relationship between yield (APY) and risk
- Build a risk scoring model based on liquidity and volatility
- Simulate portfolio performance over time
- Evaluate downside risk through stress scenarios (liquidity shocks)
- Provide insights into the trade-off between return and stability

---

## 🧠 Key Concepts

- **APY (Annual Percentage Yield):** Represents the return of the lending strategy  
- **Liquidity Risk:** Risk of not being able to withdraw funds  
- **Volatility:** Market instability affecting returns  
- **Risk Score:** Composite metric based on liquidity and volatility  
- **Stress Testing:** Simulation of adverse conditions (e.g., liquidity collapse)  

---

## ⚙️ Methodology

### 1. Data Simulation
Synthetic data is generated to represent:
- APY (3%–20%)
- Liquidity levels (low to high)
- Market volatility

### 2. Risk Modeling
A risk score is calculated based on:
- Higher volatility → higher risk  
- Lower liquidity → higher risk  

The score is normalized between 0 and 1 and classified into:
- Low Risk  
- Medium Risk  
- High Risk  

### 3. Portfolio Simulation
An initial investment of $1,000 is simulated over time using daily returns derived from APY.

### 4. Stress Scenario
A liquidity shock is introduced (days 60–70), simulating adverse market conditions and evaluating how risk behaves under stress.

### 5. Visualization
The model generates:
- Portfolio growth over time  
- Risk score evolution  
- Relationship between APY and risk  

---

## 📊 Key Insights

- Higher yields are often associated with higher risk  
- A significant portion of returns may come from unstable conditions  
- Liquidity shocks can significantly increase risk exposure  
- Portfolio growth alone is not sufficient to assess strategy quality  

---

## 📁 Project Structure

```
defi-risk-analysis/
│
├── main.py
├── requirements.txt
└── README.md
```
---

## 🚀 How to Run

### 1. Clone the repository

git clone https://github.com/francisco-obregon/defi-risk-analysis.git  
cd defi-risk-analysis  

### 2. Install dependencies

pip install -r requirements.txt  

### 3. Run the project

python main.py  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  

---

## 💡 Key Takeaway

This project demonstrates how a data-driven approach can be used to evaluate financial strategies beyond surface-level returns, incorporating risk modeling and stress testing to support better investment decisions.

---

## 👤 Author

Francisco A. Obregón  
Financial Risk & Data Analytics Professional  
