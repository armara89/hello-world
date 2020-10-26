class Solution:
    def reverseVowels(self, s: str) -> str:
        
        temp = {}
        for i in range(len(s)):
            temp[i] = s[i]
        list1 = []
        
        for i in temp:
            if temp[i].islower():
                if temp[i] == "a" or temp[i] == "e" or temp[i] == "i" or temp[i] == "o" or temp[i] == "u":
                    list1.append(temp[i])
                    temp[i] = "vowel"
            if temp[i].isupper():
                if temp[i].upper() == "A" or temp[i].upper() == "E" or temp[i].upper() == "I" or temp[i].upper() == "O" or temp[i].upper() == "U":
                    list1.append(temp[i])
                    temp[i] = "vowel"
                
        
        # list1 = list1[::-1]
        
        for i in temp:
            if temp[i] == "vowel":
                a = list1.pop()
                temp[i] = a
        
        output = ""
        
        for i in temp.values():
            output += i
        
        return output
