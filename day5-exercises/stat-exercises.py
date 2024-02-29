import scipy.stats
import numpy as np
from scipy.stats import poisson, norm
import matplotlib.pyplot as plt

######3 Poisson
fig, ax = plt.subplots(1, 1)
# define the expected values of poisson
mu = 1.3
# define the Poisson random variable and plot PMF
rv_pois = poisson.rvs(mu, size=1)
# to plot the PMF, define the quantiles
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), 'o-')
plt.title("PMF of Poisson RV")
plt.show()
#### Now plot CDF
plt.plot(x, poisson.cdf(x, mu), 'o-')
plt.title("CDF of Poisson RV")
plt.show()

# check 1000 realizations
r = poisson.rvs(mu, size=1000)
poisson.pmf(r, mu)
#print(r)

plt.hist(r, density= True)
plt.title('Histogram of n = 1000 poisson realizations')
plt.show()

############ Normal
x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
######## 100 realizations
r = norm.rvs(size = 100)
plt.plot(x, norm.pdf(x), label = 'PDF normal')
plt.plot(x, norm.cdf(x), label = 'CDF normal')
plt.hist(r, density = True, label = 'Histogram normal', color= 'pink')
plt.legend(loc = 'upper left')
plt.title('Standard normal distribution properties')
plt.show()


# Test if two sets of (independent) random data have the same mean
data1 = np.random.randint(0, 100, 100)
data2 = np.random.randint(0, 100, 100)
## test
test_res = scipy.stats.ttest_ind(data1, data2)
p_val = test_res.pvalue
print('Test H0: Difference in means = 0 agains H1: Difference in menas != 0, the p-value is: ', p_val)
print('The p-value < 0.001 so we reject H0 with 95% confidence. Therefore, the data most likely comes from different distributions.')