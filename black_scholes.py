#Fair option value according to the black and scholes model

# Assumptions: 
# The reurns are normally distributed*
# It is an European option that can be exercised only at expiration
# No dividend is payed out during the contract period

# * Lots of conditions apply xD

# 5 input variables

# S: spot price or current price of the underlying instrument
# K: strike price
# r: risk-free interest rate
# sigma: volatility  or standard deviation of the underlying instrument
# t: time to maturity


# call option  price = S*N(d1) - K*exp(-r*t)*N(d2)
# put option  price = K*exp(-r*t)*N(-d2) - S*N(-d1)

# N is the cummalative distribution function cdf or the integral of probability density function

#   where d1 = (ln(S/K) + (r + 0.5*sigma^2)*t)/(sigma*sqrt(t))
#   and   d2 = d1 - sigma*sqrt(t)


from statistics import NormalDist
import numpy as np
import scipy as sp
from scipy.stats import norm

def d1(S, K, r, sigma, t):
    return (np.log(S/K) + (r + 0.5*sigma**2)*t)/(sigma*np.sqrt(t))

def d2(S, K, r, sigma, t):
    return d1(S, K, r, sigma, t) - sigma*np.sqrt(t)


def call_option_value(S, K, r, sigma, t):
    return S*np.exp(-r*t)*norm.cdf(d1(S, K, r, sigma, t)) - K*np.exp(-r*t)*norm.cdf(d2(S, K, r, sigma, t))

def put_option_value(S, K, r, sigma, t):
    return K*np.exp(-r*t)*norm.cdf(-d2(S, K, r, sigma, t)) - S*np.exp(-r*t)*norm.cdf(-d1(S, K, r, sigma, t))


def annualised_volatility(sigma, t):
    return sigma*np.sqrt(t)

def z_score(mean,sigma,input):
    return (input - mean)/sigma

print(z_score(7,2,10))
print(NormalDist(mu=7,sigma=2).zscore(10))

print(call_option_value(100, 100, 0.05, 0.2, 10))


# Monte Carlo simulation

# Calculating the misspriced option value to find an edge


