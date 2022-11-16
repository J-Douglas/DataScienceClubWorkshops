class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Brute Force/Recursive - O(2^nm)
        def recurse(index1: int, index2: int) -> int:
            if index1 == len(text1) or index2 == len(text2):
                return 0
            
            # Characters are equal
            A = 0 # Increment index1 and index2
            # Characters are not equal
            B = 0 # Increment index1
            C = 0 # Increment index2
            
            if text1[index1] == text2[index2]:
                A = 1 + recurse(index1+1,index2+1)
            else:
                B = recurse(index1+1,index2)
                C = recurse(index1,index2+1)
                
            return max(A,B,C)
        
        return recurse(0,0)