from scipy.stats import binom

n = 10

p = 0.5

probability_2 = binom.pmf(2, n, p)

probability_3 = binom.pmf(3, n, p)

probability_4 = binom.pmf(4, n, p)

total_probability = probability_2 + probability_3 + probability_4

print("The probability is:", total_probability)