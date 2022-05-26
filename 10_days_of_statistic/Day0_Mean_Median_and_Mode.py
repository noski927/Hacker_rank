N = int(input("n: "))
X = int(input("x "))


def mean(n, x):
    x = [i for i in range(1, x + 1)]
    result = sum(x) / n
    return result


if __name__ == "__main__":
    mean_value = mean(N, X)
    print(f"Mean result: {mean_value}")
