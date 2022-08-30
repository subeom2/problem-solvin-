def solution(progresses, speeds):
    date=[]
    answer=[]
    for i in range(len(progresses)):
        n=0
        while progresses[i] < 100:
            progresses[i]+=speeds[i]
            n+=1
        date.append(n)
    m=1
    a=date[:1]
    for i in range(1,len(date)):
        if a>=date[i:i+1]:
            m+=1
        else:
            answer.append(m)
            m=1
            a=date[i:i+1]
    answer.append(m)
    return answer