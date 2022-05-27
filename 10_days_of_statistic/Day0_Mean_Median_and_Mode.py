N = int(input("n: "))
X = int(input("x "))


import numpy as np
from scipy import stats
size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))


# def mean(n, x):
#     x = [i for i in range(1, x + 1)]
#     result = sum(x) / n
#     return result
#
#
# if __name__ == "__main__":
#     mean_value = mean(N, X)
#     print(f"Mean result: {mean_value}")
