

class Solution:
    def checkValidString(self, s: str) -> bool:
        s_len = len(s)
        q = []
        for i in range(s_len-1, -1, -1):
            if s[i] == ')' or s[i] == '*':
                q.append(s[i])
            else:
                found = False
                temp_lst = []
                while len(q) != 0:
                    ele = q.pop()
                    if ele == ')':
                        found = True
                        for temp_ele in temp_lst:
                            q.append(temp_ele)
                        break
                    elif ele == '*':
                        temp_lst.append(ele)
                if not found:
                    if len(temp_lst) == 0:
                        return False
                    else:
                        temp_lst.pop()
                        while len(temp_lst) != 0:
                            q.append(temp_lst.pop())
        print(q)
        if len(q) == 0:
            return True

        wild_char = 0
        for i in q[::-1]:
            if i == ')':
                if wild_char == 0:
                    return False
                else:
                    wild_char -= 1
            else:
                wild_char += 1
        return True


sol = Solution()
s = "(()(()))(()()()))))((((()*()*(())())(()))((*()(*((*(*()))()(())*()()))*)*()))()()(())()(()))())))"
res = sol.checkValidString(s)
print(res)
