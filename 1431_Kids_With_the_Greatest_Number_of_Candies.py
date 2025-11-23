class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if 2<=len(candies)<=100 and 1<=extraCandies<=50:
            flags = []
            for i_candy in candies:
                if 1<= i_candy <= 100:
                    flag = True
                    for candy in candies:
                        flag = flag and i_candy+extraCandies >= candy
                        if not flag:
                            break
                    flags.append(flag)
                else:
                    pass
        return flags
