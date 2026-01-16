# Markowitz-Efficient-Frontier
Python implementation of the Markowitz Efficient Frontier for portfolio optimization, using historical stock data from yfinance. Demonstrates calculation of expected returns, variances, and volatilities for 2-3 assets, with extensions for multi-asset portfolios.


This repository contains a Python script for calculating and visualizing the Markowitz Efficient Frontier, a key concept in modern portfolio theory. It uses historical stock data to simulate portfolios that maximize expected returns for a given risk level (or minimize risk for a target return). 

## Project Overview
The Markowitz Efficient Frontier illustrates the optimal trade-off between risk (volatility) and return in a portfolio. This implementation:
- Fetches historical closing prices using `yfinance`.
- Computes log returns, expected portfolio returns, variances, and volatilities.
- Simulates thousands of random portfolios to approximate the frontier.
- Visualizes the results in a scatter plot.

This project is ideal for demonstrating quantitative finance skills, such as in job applications for roles in asset management, hedge funds, or fintech.

## Requirements
- Python 3.6+
- Libraries: `numpy`, `pandas`, `yfinance`, `matplotlib`

## Limitations
- Relies on historical data; assumes future returns follow past patterns (not always true).
