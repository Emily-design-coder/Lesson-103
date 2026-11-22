from scipy.stats import poisson

expected = 10

probability_12_or_more = 1 - poisson.cdf(11, expected)

probability_12 = poisson.pmf(12, expected)

probability_13 = poisson.pmf(13, expected)

probability_14 = poisson.pmf(14, expected)

probability_15 = poisson.pmf(15, expected)

probability_16 = poisson.pmf(16, expected)

probability_17 = poisson.pmf(17, expected)

probability_18 = poisson.pmf(18, expected)

probability_between = (probability_12 + probability_13 + probability_14 + probability_15 + probability_16 + probability_17 + probability_18)


print("Probability of 12 or more days of rain:", probability_12_or_more)
print("Probability of between 12 and 18 days of rain:", probability_between)