def solution(n):
    arr=''
    while n>3:
        a=n%3
        if a==0:
            arr='4'+ arr
        else:
            arr=str(a)+arr
        n=n//3
        if a==0:
            n-=1 
    if n==3:
        arr='4'+arr
    else:
        arr=str(n)+arr
    return arr