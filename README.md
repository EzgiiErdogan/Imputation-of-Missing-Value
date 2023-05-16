# Imputation-of-Missing-Value
In this section, we will look at the improvement methods used for missing data in data sets.

# Methods to Clean/Improve Missing Data Python

Let's take a look at the "missing data" problem, which is one of the problems we encounter very often when processing data.

# Always Missing Data?

Missing data may appear in different data sets from time to time. Well, every "0" value or "NaN" value we see is incomplete yield? In order to determine whether there are missing data in our data set we are working on, we first need to know our data set correctly. For example, for an individual who does not have a car, we may not write any value in our data column, which at first glance does not show us whether our data is missing or not. We deal with the issue with two possibilities, indicating that the individual does not have a car or that data was not actually entered. For this reason, it is important to get to know our dataset correctly. If our data actually exists and has not been entered into our dataset, or if we have encountered an obvious missing data problem, we can use several cleanup/improvement methods.

# Mean, Median and Mode Method

This method is one of the most commonly used methods for completing missing data. It is obtained by taking the means, medians or modes of the data without disturbing the structure of the data set. It is generally used on small datasets. In the example we have, we will try these methods with a small data set.
