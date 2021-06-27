# Heart-Disease-Project-AML
A Machine Learning Web Application to help health practitioners solve the problem of heart disease diagnosis using probabilistic machine learning methods. 

# Project Overview 
- Framed the Heart Disease problem through the lenses of a probabilistic framework
- Performed Exploratory Data Analysis to understand the Heart Disease Data Set from the UCI Machine Learning Repository 
- Used 3 methods for feature selection: Correlation Analysis, Recursive Feature Elimination, and Feature Importance (using Extra Trees)
- Built 5 Classification models: Logistic Regression, Naive Bayes, Lasso Regression, Support Vector Machine, and Probabilistic Model (for binary classification)
- Compared and discussed the classification models 

## Resources 
**Python Version:** 3.9.2 <br>
**Packages:** pandas, numpy, seaborn, sklearn, matplotlib, pickle, pymc3, arviz, django, django-widget-tweaks <br>
**Dataset:** https://archive.ics.uci.edu/ml/datasets/heart+disease <br>
**Heart Disease:** https://www.onhealth.com/content/1/heart_disease_coronary_artery

## Python Notebooks
**Notebook Name: Heart_Disease_Project_Notebook -** Contains project objective, data set description, data preprocessing, model building results and discussions <br>
**Notebook Name: Model_Experiment -** Contains classification model building experiments <br>
**Important Note:** When reviewing notebooks on github - try reloading notebook or reloading internet page if any viewing problems are encountered

## Sample figures from Exploratory Data Analysis 
![Figure 2](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure2.png)
![Figure 3](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure3.png)
![Figure 4](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure4.png)
![Figure 5](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure5.png)
![Figure 6](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure6.png)

## Classification Machine Learning Model Performance (Accuracy)
- Logistic Regression (using 7 features): 81%
- Naive Bayes (using 7 features): 80%
- Lasso Regression (using 7 features): 75%
- Logistic Regression (using 14 features): 85%
- Naive Bayes (using 14 features): 84% 
- Lasso Regression (using 14 features): 83%
- Support Vector Machine (using 14 features): 86% 

## Classification Models with Train-Test Split (80% Training and 20% Testing data) 
- Logistic Regression Train Accuracy: 84%
- Logistic Regression Test Accuracy: 85%
- Support Vector Machine Train Accuracy: 87%
- Support Vector Machine Test Accuracy: 85%

## Probabilistic Model Statistic Evulation (Classification Report)
![Figure 7](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure7.png)

## Django App
**Resource:** PyCharm IDE - Windows 64 bit <br>
**PyCharm:** Version: 2021.1.2; Build: 211.7442.45 <br>
**App Folder:** hdWebApp 
![Figure 1](https://github.com/Ellie190/Heart-Disease-Project-AML/blob/main/Sample_figures/figure1.png)


