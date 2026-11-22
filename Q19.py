def reverse_segment(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate_right(nums, k):
    n = len(nums)
    k %= n

    if k == 0:
        return

    reverse_segment(nums, 0, n - 1)
    reverse_segment(nums, 0, k - 1)
    reverse_segment(nums, k, n - 1)