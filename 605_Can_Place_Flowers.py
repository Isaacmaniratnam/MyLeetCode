class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fbl = len(flowerbed)
        counter = 0
        def validate_bed(bed,fbl,n):
            flag = False
            if 1<=fbl<=20000 and 0<=n<=fbl:
                for i in range(fbl-1):
                    if fbl >=2 and (bed[i] == 0 or bed[i] == 1) and (bed[i+1] == 0 or bed[i+1] == 1):
                        if bed[i] == 1 and bed[i+1] == 1:
                            break
                        else:
                            flag =  True
                    else:
                        pass
            else:
                pass
            return flag
        
        if fbl>1 and validate_bed(flowerbed,fbl,n):
            if flowerbed[0] == 0 and flowerbed[1]== 0:
                flowerbed[0] = 1
                counter+=1
            else:
                pass
            for i in range(1,fbl-1):
                if flowerbed[i-1] != 1 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    counter+=1
                else:
                    pass
            if flowerbed[-1] == 0 and flowerbed[-2]== 0:
                flowerbed[-1] = 1
                counter+=1
            else:
                pass
        elif fbl == 1:
            if flowerbed[0] == 0 and n == 1:
                flowerbed[0] = 1
                counter+=1
            else:
                pass
        else:
            pass
            
        if counter >= n:
            return True
        else:
            return False
