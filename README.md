# Federal Funds Rate Prediction Model

## Overview

The Federal Reserve (Fed) is a United States governmental institution that serves to keep the national economy stable and under control. It is the most powerful and influential economic organization in the nation, tasked with promoting "maximum employment, stable prices, and moderate long-term interest rates". The Fed's mission is commonly referred to as the "dual mandate", highlighting its focus on employment and inflation, using long-term interest rates as a mechanism to achieve these objectives.

Changes in long-term interest rates, representing the cost of borrowing money, significantly impact personal expenditures and corporate investment. High interest rates encourage savings and deter investment, cooling the economy, while lower rates do the opposite. The most important long-term interest rate in the U.S. is the federal funds rate (FFR), set by the Fed to guide the economy.

## Research Objectives

The ability to predict changes in the FFR could enable optimal financial decisions. Despite various efforts, accurate prediction remains challenging under mixed economic conditions. Our objective is to develop a more robust model for predicting changes in the FFR using regression and classification techniques, focusing on features that best predict Federal Open Market Committee (FOMC) decisions.

## Our Data

We collected data from FRED, Yahoo! Finance, OECD, Wikipedia, and Dr. Kuttner's website, focusing on economic indicators continuously tracked from 1989 to the present day. Our selected features include Bank Prime Loan Rate Changes, Exports of Goods and Services, Personal Consumption Expenditures Rate, and several others detailed in the table below.

| Feature | Variable | Frequency | Description |
| --- | --- | --- | --- |
| Bank Prime Loan Rate Changes | `loan` | daily | Rate charged by banks for short-term loans to creditworthy debtors |
| Exports of Goods and Services | `export` | quarterly | Total dollar value of goods and services exported in the quarter |
| Personal Consumption Expenditures Rate | `pce` | monthly | Measure of core inflation for personal expenditures |
| Unemployment Rate | `ue` | monthly | Number of unemployed as a percentage of the labor force |
| Change in Real GDP | `rgdp` | quarterly | Quarterly change in inflation-adjusted GDP |
| Total Vehicle Sales | `cars` | monthly | Total number of vehicle sales in millions |
| Recession Indicator | `recess` | monthly | Binary variable indicating whether the US is in a recession |
| GDP Deflator | `gdpd` | daily | Price index given by ratio of nominal GDP to real GDP |
| Velocity of M1 Money | `veloc` | quarterly | Ratio of nominal GDP to the quarterly average of M1 money stock |
| New Private Housing Units Started | `house` | monthly | Number of new housing units beginning construction in millions  |

## Data Cleaning and Feature Engineering
Our data, obtained from diverse frequencies, was harmonized and processed to avoid "look-ahead" bias, filling gaps and using a collapse() function to align with FOMC announcement days. New features were introduced to capture trends, enhancing our dataset for analysis.

## Robustness
Our data processing pipeline is designed for ease of modification, supporting the addition of new features or FOMC decisions. This flexible framework ensures our model remains current and adaptable.

## Data Visualization and Basic Analysis
The historical analysis shows a 68% baseline accuracy for predicting FFR changes by always assuming no change. This sets the benchmark for our models. Charts and graphs, such as the change in FFR over time and factor analysis, provide visual insights into our data and model performance.

<p align="center">
  <img src="media/feature_importance.png" alt="feature importance" width="400"/>
  <img src="media/df_factor_analysis_2.png" alt="component analysis" width="400"/>
</p>

## Learning Algorithms and In-Depth Analysis
We explored various models, including RandomForestClassifier, XGBoostClassifier, Softmax Logistic Regression, and Gaussian Discriminant Analysis. Our findings indicate that RandomForestClassifier is the most effective, with an average accuracy of approximately 80%.

#### Average Accuracy Results:
- RandomForestClassifier – Average Accuracy: 0.81
- XGBoostClassifier – Average Accuracy: 0.79
- Softmax Logistic Regression – Average Accuracy: 0.75
- General Discriminant Analysis (GDA) – Average Accuracy: 0.68

#### Classification Reports:
**RandomForestClassifier – Classification Report:**

|       | precision | recall | f1-score | support |
|-------|-----------|--------|----------|---------|
| 0     | 0.82      | 0.42   | 0.56     | 33      |
| 1     | 0.80      | 0.96   | 0.87     | 188     |
| 2     | 0.87      | 0.49   | 0.63     | 53      |
|       |           |        |          |         |
| accuracy|          |        | 0.81     | 274     |
| macro avg| 0.83    | 0.63   | 0.69     | 274     |
| weighted avg| 0.81 | 0.81   | 0.79     | 274     |

**XGBoostClassifier – Classification Report:**

|       | precision | recall | f1-score | support |
|-------|-----------|--------|----------|---------|
| 0     | 0.76      | 0.39   | 0.52     | 33      |
| 1     | 0.78      | 0.96   | 0.86     | 188     |
| 2     | 0.88      | 0.43   | 0.58     | 53      |
|       |           |        |          |         |
| accuracy|          |        | 0.79     | 274     |
| macro avg| 0.81    | 0.60   | 0.66     | 274     |
| weighted avg| 0.80 | 0.79   | 0.77     | 274     |

**Softmax Logistic Regression – Classification Report:**

|       | precision | recall | f1-score | support |
|-------|-----------|--------|----------|---------|
| 0     | 0.68      | 0.39   | 0.50     | 33      |
| 1     | 0.78      | 0.88   | 0.83     | 188     |
| 2     | 0.63      | 0.51   | 0.56     | 53      |
|       |           |        |          |         |
| accuracy|          |        | 0.75     | 274     |
| macro avg| 0.70    | 0.60   | 0.63     | 274     |
| weighted avg| 0.74 | 0.75   | 0.74     | 274     |

**GDA – Classification Report:**

|       | precision | recall | f1-score | support |
|-------|-----------|--------|----------|---------|
| 0     | 0.44      | 0.55   | 0.49     | 33      |
| 1     | 0.83      | 0.69   | 0.75     | 188     |
| 2     | 0.49      | 0.72   | 0.58     | 53      |
|       |           |        |          |         |
| accuracy|          |        | 0.68     | 274     |
| macro avg| 0.59    | 0.65   | 0.61     | 274     |
| weighted avg| 0.72 | 0.68   | 0.69     | 274     |


## Ethical Implications
The development and application of our model raise ethical considerations regarding the potential for information advantage and market impact. We emphasize the importance of responsible use and awareness of the limitations and uncertainties inherent in predictive modeling.

