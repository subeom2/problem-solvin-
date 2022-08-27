def solution(s):
    closed=0
    opened=0
    if s[0]==')' or s[-1]=='(':
        return False
    elif s.count('(')-s.count(')')!=0:
        return False
    for i in range(1,len(s)):
        if s[0]!=s[i]:
            closed+=1
        else:
            opened+=1
        if closed>opened+1:
            return False
    else:
        return True