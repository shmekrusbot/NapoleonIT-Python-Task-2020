class Solution:
    def romanToInt(self,s:str)->int:
        if(len(s)>=1 and len(s) <=15):
            Sum_Roman_Digits = 0
            Dictionary_Roman_Numbers = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
            for i in range(-1,-len(s),-2):
                if(Dictionary_Roman_Numbers[s[i]] > Dictionary_Roman_Numbers[s[i-1]]):
                    Sum_Roman_Digits += Dictionary_Roman_Numbers[s[i]]-Dictionary_Roman_Numbers[s[i-1]]
                else:
                    Sum_Roman_Digits += Dictionary_Roman_Numbers[s[i]] + Dictionary_Roman_Numbers[s[i-1]]
            if(len(s) % 2 == 1):
                Sum_Roman_Digits  +=Dictionary_Roman_Numbers[s[0]]            
            return Sum_Roman_Digits

#Solution class tests
temp = Solution()
#1
print("s = III")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'III'))
print('\n')
#2
print("s = IV")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'IV'))
print('\n')
#3
print("s = IX")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'IX'))
print('\n')
#4
print("s = VLIII")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'VLIII'))
print('\n')
#5
print("Test s = MCMXCIV")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'MCMXCIV'))
print('\n')
#6
print("Test s = LXXXVIII")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'LXXXVIII'))
print('\n')
#7
print("Test s = DCCCLXXXII")
print("Roman number(is s) in integer = ",temp.romanToInt(s = 'DCCCLXXXII'))
print('\n')




