
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        sharp_i = 0
        sharp_j = 0
        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == '#' or sharp_i > 0):
                if S[i] == '#':
                    sharp_i += 1
                    i -= 1
                else:
                    if sharp_i > 0:
                        sharp_i -= 1
                        i -= 1

            while j >= 0 and (T[j] == '#' or sharp_j > 0):
                if T[j] == '#':
                    sharp_j += 1
                    j -= 1

                else:
                    if sharp_j > 0:
                        sharp_j -= 1
                        j -= 1

            print(i, j)
            if i == j == -1:
                return True
            if i < 0 or j < 0:
                return False
            if S[i] == T[j]:
                i -= 1
                j -= 1
            else:
                return False

        if i == j == -1:
            return True

        return False



s = Solution()
# S = "bxj##"
# T = "bxo#j##"
# S = "ab#c"
# T = "ad#c"
S = ""
T = "b#"
result = s.backspaceCompare(S, T)
print(result)
