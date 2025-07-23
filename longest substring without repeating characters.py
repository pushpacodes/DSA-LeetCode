class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = [0] * 128  
        start = 0
        end = 0
        n = len(s)
        max_len = 0
        while end < n:
            index = ord(s[end])
            if hashmap[index] == 0:
                hashmap[index] = 1
                max_len = max(max_len, end - start + 1)
                end += 1
            else:
                hashmap[ord(s[start])] = 0
                start += 1
        return max_len
