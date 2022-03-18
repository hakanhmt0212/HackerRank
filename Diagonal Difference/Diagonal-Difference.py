def diagonalDifference(arr):
    int1 = 0
    int2 = 0

    for i in range(len(arr)):
        int1 += arr[i][i]

    for j in range(len(arr)):
        int2 += arr[j][len(arr) - 1 - j]

    return abs((int1 - int2))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
