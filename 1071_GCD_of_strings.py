class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def do_gcd(a,b):
            while a%b != 0:
                q=b
                b=a%b
                a=q
            return b
        len1 = len(str1)
        len2 = len(str2)
            
        gcd = do_gcd(len1,len2)
        pattern = str2[:gcd]
        result = ''
        if 1<=len1 and 1<=len2<=1000:
            if str1.startswith(pattern):
                if pattern * int(len1/gcd) == str1 and pattern * int(len2/gcd) == str2:
                    result = pattern
                else:
                    pass                   
            else:
                pass
        else:
            pass
        return result
