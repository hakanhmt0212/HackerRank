def plusMinus(arr):
    sumsP = 0
    sumsM = 0
    sumsZ = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            sumsM += 1
        elif arr[i] > 0:
            sumsP += 1
        else:
            sumsZ += 1
    print(round(sumsP / len(arr), 6))
    print(round(sumsM / len(arr), 6))
    print(round(sumsZ / len(arr), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
