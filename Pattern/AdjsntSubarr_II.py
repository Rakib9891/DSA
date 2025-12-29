

def adsntSubArrII(nums):
    n = len(nums)
    a = 1
    increase = [a] * n

    for i in range(1, n):
        if nums[i] > nums[i-1]:
            a += 1
            increase[i] = a
        else:
            a = 1
    idx = None
    l, r = 0, n
    while l <= r:
        m = (l+r) // 2
        if m-1 < n and m+1 < n and increase[m-1] < increase[m] > increase[m+1]:
            idx = m
            break
        elif m-1 < n and increase[m] < increase[m-1]:
            r = m - 1
        elif m+1 < n and increase[m] < increase[m+1]:
            l = m + 1
    print(increase[idx])

    first, second = 1, 1
    for i in range(idx+1, n-1):
        if increase[i] < increase[i+1]:
            second += 1
        else:
            break
    found = False
    for i in range(idx -1, 0, -1):
        if not found and increase[i] > increase[i-1]:
            first += 1
            if increase[i-1] == 1:
                found = True
        else:
            break
    
    return min(first, second)


if __name__ == "__main__":
    # arr = [2, 5, 7, 8, 9, 2, 3, 4, 3, 2]
    arr = [1,2,3,4,4,4,5,6,7]
    func = adsntSubArrII(arr)
    print(func)