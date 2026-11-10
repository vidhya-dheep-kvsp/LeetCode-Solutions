class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        fdict={}
        for st in strs:
            freq=[0]*26
            for c in st:
                index=ord(c)-ord('a')
                freq[index]+=1
            
            key=tuple(freq)
            if key not in fdict:
                fdict[key]=[]
            
            fdict[key].append(st)

        return list(fdict.values())



