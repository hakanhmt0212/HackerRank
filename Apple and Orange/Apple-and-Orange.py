def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesInHouse = 0
    orangesInHouse = 0

    for _ in apples:
        if s <= (_ + a) <= t:
            applesInHouse += 1

    for _ in oranges:
        if s <= (_ + b) <= t:
            orangesInHouse += 1

    print(applesInHouse)
    print(orangesInHouse)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)