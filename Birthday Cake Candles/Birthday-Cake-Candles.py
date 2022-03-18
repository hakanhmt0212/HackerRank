def birthdayCakeCandles(candles):
    tallest = max(candles)
    numberOfCandles = 0
    for i in range(len(candles)):
        if tallest==candles[i]:
            numberOfCandles += 1
    return numberOfCandles

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)