def consecutive(arr):
    if len(arr) <= 1:
        return 0
    arr.sort()
    for num in arr[:(len(arr)-1)]:
        diff = 0
        if num < arr[arr.index(num) + 1]:
            diff = arr[arr.index(num) + 1] - num
            if diff == 1:
                return 0
            else:
                count = 0
                while not diff == 0:
                    arr[arr.index(num) + 1] -= 1
                    count += 1
                    diff -= 1
                return count




consecutive([4, 8, 6])
consecutive([1, 2, 3, 4])
consecutive([])
consecutive([1])
consecutive([-10])