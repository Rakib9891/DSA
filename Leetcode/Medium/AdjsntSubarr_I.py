# Given an int arr nums and an int K. Return True if there are two adjsnt subArrs in nums and which are strickly increasing else False. The subArrs len should be K.

def adsntSubArrI(nums, k):
    n = len(nums)
    a = 1
    increase = [a]

    for i in range(1, n):
        if nums[i] > nums[i-1]:
            a += 1
            increase.append(a)
        else:
            a = 1
            increase.append(a)
    print(increase)
    for i in range(k, n-k+1):
        if increase[i] >= k and increase[i+k] >= k:
            return True

    return False


if __name__ == "__main__":
    arr = [2, 5, 7, 8, 9, 2, 3, 4, 3, 2]
    func = adsntSubArrI(arr, 3)
    print(func)