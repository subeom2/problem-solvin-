def solution(s):
    count=0
    change=0
    while s!="1":
        count+=(len(s)-s.count("1"))
        s=str(bin(s.count("1"))[2:])
        change+=1
    return [change, count]