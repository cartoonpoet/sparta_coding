def permute(nums):
    answer = []
    def backtrack(start=0):
        if start == len(nums):
            print(nums, nums[:])
            return answer.append(nums)

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start+1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack()
    return answer


# 예시 실행
print(permute([1, 2, 3]))