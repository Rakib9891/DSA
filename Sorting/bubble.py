import sys
input = sys.stdin.readline

def bubble_sort(nums):

    n = len(nums)
    for _ in range(1, n):
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    print(f'Ans: {nums}')


if __name__ == "__main__":
    print('Type input as space separate valuss')
    print('Example: ->  5 4 3 2 1')
    arr = list(map(int, input().strip().split()))
    if arr:
        bubble_sort(arr)
    else:
        bubble_sort([5, 4, 3, 2, 1])
        print("Since you didn't type any input this is default output from example")
