def aVeryBigSum(ar):
    toplam = 0
    for i in range(len(ar)):
        toplam += ar[i]
    return toplam

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().split()))
    result = aVeryBigSum(ar)
    print(result)