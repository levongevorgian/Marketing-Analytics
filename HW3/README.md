# HW3 - Survival Analysis & CLV

This repository contains my third homework for DS223 - Marketing Analytics. The assignment focuses on applying survival analysis using Accelerated Failure Time (AFT) models to predict customer churn and calculate Customer Lifetime Value (CLV).

## Directory Structure

**code/**  
Contains the Python notebook and supporting code:  
- [`AFT_Model.ipynb`](code/AFT_Model.ipynb) — Main notebook with AFT model fitting, survival analysis, and CLV calculations.  

**data/**  
Contains the dataset and processed results:  
- [`telco.csv`](data/telco.csv) — Original subscriber dataset.  
- [`telco_encoded_with_clv.csv`](data/telco_encoded_with_clv.csv) — Dataset with encoded features, predicted lifetime, and CLV.  

**img/**  
Contains visualizations from the analysis:  
- [`AFT Survival Curves.png`](img/AFT%20Survival%20Curves.png) — Survival curves for median customer across all models.  
- [`Survival Curves by Regions.png`](img/Survival%20Curves%20by%20Regions.png) — Survival curves by region using final model.  
- [`CLV Distribution.png`](img/CLV%20Distribution.png) — Histogram of predicted CLV.  
- [`CLV Boxplot.png`](img/CLV%20Boxplot.png) — Boxplot of predicted CLV.  
- [`Average CLV by Region.png`](img/Average%20CLV%20by%20Region.png) — Bar plot of average CLV by region.  
- [`Average CLV by Customer Category.png`](img/Average%20CLV%20by%20Customer%20Category.png) — Bar plot of average CLV by customer category.  
- [`Churn vs CLV.png`](img/Churn%20vs%20CLV.png) — Scatter plot of churn probability (12 months) vs CLV.  

**report/**  
Contains the written report:  
- [`report.pdf`](report.pdf) — Short report summarizing findings, insights, and retention recommendations.  

**requirements/**  
- [`requirements.pdf`](requirements.pdf) — Homework instructions.  
- [`requirements.txt`](requirements.txt) — Python dependencies.  

## Homework Overview

The goal of this homework is to:  
1. Build AFT models (Weibull, Log-Logistic, Log-Normal) to predict churn.  
2. Compare models and select the best one based on AIC and interpretability.  
3. Identify significant features and refit the final model.  
4. Calculate predicted customer lifetime and CLV.  
5. Explore CLV across different segments (region, customer category).  
6. Estimate suggested retention budget.  

## Analysis Summary

- LogNormal AFT model was selected as the final model based on lowest AIC and interpretability.  
- Key factors affecting churn: age, customer category, internet and voice subscriptions, marital status.  
- High-value segments: older, married customers, especially in premium service categories.  
- Estimated annual retention budget: calculated using predicted CLV and survival probabilities.  

## References

- DS223 - Marketing Analytics course materials.  
- [Lifelines Python library documentation](https://lifelines.readthedocs.io/en/latest/lifelines.fitters.html) for survival analysis and AFT models.
