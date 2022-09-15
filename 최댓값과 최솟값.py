def solution(s):
    ss=s.split()
    ss=list(map(int,ss))
    answer = str(min(ss))+' '+str(max(ss))
    return answer