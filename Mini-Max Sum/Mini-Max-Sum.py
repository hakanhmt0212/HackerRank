def miniMaxSum(arr):
    sums = sum(arr)
    print(sums - max(arr), sums - min(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
