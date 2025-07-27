class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        basket = {}
        max_sum = 0
        for end in range(len(fruits)):
            fruit = fruits[end]
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            max_sum = max(max_sum, end - start + 1)
        return max_sum
