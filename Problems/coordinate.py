class Solution :
    def check(self,x,y,n):
        for i in range(0,n+1):
            temp = i%4
            if temp ==1:
                y = y+i
                print("({},{})".format(x,y))
            elif temp ==2:
                x = x+i
                print("({},{})".format(x, y))
            elif temp ==3:
                y=y-i
                print("({},{})".format(x, y))
            elif temp == 4:
                x = x-i
                print("({},{})".format(x, y))
if __name__=='__main__':
    x =0
    y=0
    n =int(input("Enter value of n  : "))
    obj = Solution()
    obj.check(x,y,n)