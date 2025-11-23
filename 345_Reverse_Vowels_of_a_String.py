class Solution:
    def reverseVowels(self, s: str) -> str:
        len_s = len(s) if s != '' else 0
        word = []
        vowels = []
        if 1<= len_s <= 300000:
            c=0
            for i in range(len_s):
                if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                    vowels.append(s[i])
                    word.append(c)
                    c+=1
                else:
                    word.append(s[i])
        else:
            pass
        if len(vowels) >= 1:
            for i in range(len_s):
                if isinstance(word[i],int):
                    word[i] = vowels[-1*word[i]-1]
                else:
                    pass
            s = ''.join(word)
        else:
            pass
        
        return s
