def timeConversion(s):
    arr = s.split(":")
    if ("PM" in arr[2]) and (int(arr[0]) != 12):
        newTime = str(int(arr[0]) + 12) + ":" + arr[1] + ":" + arr[2][:len(arr[2]) - 2]
    elif ("AM" in arr[2]) and (int(arr[0]) == 12):
        newTime = "00"+ ":" + arr[1] + ":" + arr[2][:len(arr[2]) - 2]
    else:
        newTime = s[:len(s) - 2]

    return newTime

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)