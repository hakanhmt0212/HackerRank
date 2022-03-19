def breakingRecords(scores):
    min = 0
    max = 0
    higest_score = scores[0]
    lowest_score = scores[0]

    for _ in range(1,len(scores)):
        if scores[_] < lowest_score:
            min += 1
            lowest_score = scores[_]
        elif scores[_] > higest_score:
            max += 1
            higest_score = scores[_]
        else:
            continue
    result = str(max) + str(min)

    return result

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)