"""Two Sum - LeetCode N (Easy)
https://leetcode.com/problems/two-sum/

Approach: One pass through nums; check difference in dict; store value:idx in dict otherwise
Time: O(n)    Space: O(n)
"""


def solve(nums: list[int], target: int) -> list[int]:
    # Maintain dictionary/hash map of value : index entries
    checked = {}

    # Iterate through numbers
    for i, num in enumerate(nums):
        diff = target - num

        # If difference is in dict, return indices
        # Otherwise add value : idx to dict
        if diff in checked:
            return [checked[diff], i]
        else:
            checked[num] = i
    return []


def test_scaffold():
    assert sorted(solve(nums=[2, 7, 11, 15], target=9)) == sorted([0, 1])
    assert sorted(solve(nums=[3, 2, 4], target=6)) == sorted([1, 2])
    assert sorted(solve(nums=[3, 3], target=6)) == sorted([0, 1])
    assert sorted(solve(nums=[0, 4, -5, 3, 2, 4], target=-3)) == sorted([2, 4])
