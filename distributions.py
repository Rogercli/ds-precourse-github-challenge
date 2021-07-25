import math

def factorial(n):
    prod=1
    for i in range(2,n+1):
        prod*=i
    return prod

def combinations(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))
def binomial_pmf(n, p, k):
    x=combinations(n,k)
    return round((x*(((p)**k)*((1-p)**(n-k)))),5)
print(binomial_pmf(40,.25,5))


def poisson_pmf(k,lam):
    return ((lam**k)*(math.e**-lam))/factorial(k)


def geometric_pmf(n,p):
    return (1-p)**(n-1)*p