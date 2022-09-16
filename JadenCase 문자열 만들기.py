def solution(s):
    answer=''
    s = s.lower()
    s = s.split(' ')
    for i in range(len(s)):
        r = s[i].capitalize()
        answer=answer+r+' ' 
    answer = answer[:-1]
    return answer