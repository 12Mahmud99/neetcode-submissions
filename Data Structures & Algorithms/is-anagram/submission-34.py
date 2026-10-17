class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table, table2= {},{}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in table.keys():
                table[s[i]]+=1
            else:
                table[s[i]]=0

            if t[i] in table2.keys():
                table2[t[i]]+=1
            else:
                table2[t[i]]=0
        
        for k in table.keys():
            if k not in table2.keys():
                return False
            elif table[k]!=table2[k]:
                return False
        return True