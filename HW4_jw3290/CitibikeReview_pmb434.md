## CitiBike Review, by Pablo Mandiola (pmb434)

### Hypothesis formulation

From analyzing the hypothesis, I have three general observations that could be useful to improve it: 

1. The hypothesis lacks a significance level, which is important to define before doing the experiment.

2. I would suggest to use proportions instead of the absolute number, as it is easier to perform a comparison between different samples.

3. Because the underlying data records are trips, it can't really answer if there are more female or male subscribers. What it can answer is if there are more female subscribers using citibike in a given month than male subscribers.

Taking all three points into account, I would suggest to slightly modify the null and alernative hypothesis. For example, keeping the initial idea it could be something like this:

* H<sub>0</sub>: The proportion of female riders who are subscribers is the same or higher than the proportion of male riders who are subscribers, with  significance level 0.05.

* H<sub>a</sub>: The proportion of female riders who are subscribers is lower than the proportion of male riders who are subscribers.

### Data assessment

The data provided has the appropriate features to answer the question, as only the variables Gender and User Type are needed. If the test is to be done on the proportion instead of the absolute number, the same data is needed but it just has to be normalized before performing the test.

### Statistical test suggestion

Taking the suggested modifications into consideration, I suggest to use a Z-test to compare the difference between proportions in two samples. The question we need to answer is if the two samples come from the same or different populations, the data is not parametric, we have one treatment variable and two categories, the data is unpaired and there are at least 30 observations per sample; all this leads us to the Z-test for unpaired data following the chart provided in class.
