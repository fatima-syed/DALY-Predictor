# DALY-Predictor
A machine learning project aimed at developing a model for predicting Disability-Adjusted Life Years (DALYs) in order to analyze the year-wise reduced life expectancy in different nations due to various mental health disorders. By leveraging historical data on mental health disorders and analyzing their impact on life expectancy, the model aims to provide valuable insights into the burden of mental health on the overall population health.

### Dataset
The dataset contains information on 6,840 studies from 228 countries from 1990 to 2019. Each row represents a country in a certain year, and columns represent features i.e. prevalence of certain disorders. The target variable is DALY (Disability-adjusted life years).

### Model
Random Forest Regressor model has been used in this project which combines multiple decision trees to make predictions. Each decision tree is trained on a random subset of the data and features, and the final prediction is obtained by averaging the predictions of individual trees.

### Group Members
■ Syeda Fatima Shahid (337346) <br>
■ Hafsa Malik (341303) <br>
■ Omar Ahmed (321604)
