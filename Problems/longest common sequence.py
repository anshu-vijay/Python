def lcs(x,y,len_x,len_y):
    if len_x == 0 or len_y == 0:
        return 0
    elif x[len_x-1]==y[len_y-1]:
        return 1 + lcs(x,y,len_x-1,len_y-1)
    else:
        return max(lcs(x,y,len_x,len_y-1),lcs(x,y,len_x-1,len_y))

x ="aggtab"
y="gxtxayb"
print("Lcs length is: ",lcs(x,y,len(x),len(y)))