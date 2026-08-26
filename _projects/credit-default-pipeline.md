---
layout: project
title: "Credit Default Prediction Pipeline"
date: 2024-01-01
description: "End-to-end machine learning pipeline for predicting credit default probability using gradient boosting with feature engineering on bureau data."
github: ""   # repo is not public
demo: ""
paper: ""
status: "Completed"
platform: "Python · XGBoost · Optuna · MLflow"
role: "End to end: pipeline, modelling, validation, deployment"
tags: [Python, XGBoost, Credit Risk, Feature Engineering, MLflow]
---

## Overview

This project builds a production-ready binary classification pipeline for predicting the probability of credit default within the next 12 months.

## Problem Statement

Given bureau data and application features for a loan applicant, predict the probability of default (PD) to inform underwriting decisions.

## Approach

1. **Data Ingestion** — Pulling from multiple bureau data sources
2. **Feature Engineering** — WoE encoding, lag features, aggregation across accounts
3. **Model Training** — XGBoost with Optuna hyperparameter search
4. **Validation** — Walk-forward validation preserving temporal ordering
5. **Deployment** — Batch scoring via MLflow model registry

## Results

| Metric | Value |
|--------|------:|
| AUC-ROC | 0.831 |
| Gini | 0.662 |
| KS Statistic | 0.51 |
| PSI (month-3) | 0.08 |

## Key Learnings

- Temporal leakage is the #1 enemy in credit risk models
- WoE encoding significantly improved model stability
- Monotonicity constraints improved trust with the business
