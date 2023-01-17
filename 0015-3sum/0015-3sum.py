class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        result = []
        length = len(numbers)
        if not numbers or length < 3:
            return result

        numbers.sort()
        
        for i in range(0,length - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left = i + 1
            right = length - 1
            target = -numbers[i]
            self.find_two_number(numbers,left,right,target,result)
        return result

    def find_two_number(self,numbers,left,right,target,result):
        while left < right:
            if numbers[left] + numbers[right] ==target:
                result.append([-target,numbers[left],numbers[right]])
                right -=1
                left += 1

                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1