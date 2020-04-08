from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for ele in strs:

            set_ = Counter(ele)
            is_seen = False
            for i in result:
                if i[0] == set_:
                    is_seen = True
                    i.append(ele)
            if not is_seen:
                result.append([Counter(ele), ele])

        return [i[1:]for i in result]


s = Solution()
strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
# strs = ["eat","tea","tan","ate","nat","bat"]
res = s.groupAnagrams(strs)
expected = [["sol"],["wow"],["gap"],["hem"],["yap"],["bum"],["ugh","ugh"],["aha"],["jab"],["eve"],["bop"],["lyx"],["jed"],["iva"],["rod"],["boo"],["brr"],["hog"],["nay"],["mir"],["deb","deb"],["aft"],["dis"],["yea"],["hos"],["rye"],["hey"],["doc"],["bob"],["eel"],["pen"],["job"],["max"],["oho"],["lye"],["ram"],["nap"],["elf"],["qua"],["pup","pup"],["let"],["gym"],["nam"],["bye"],["lon"]]
print(res)
print(expected)
