def solution(queue1, queue2):
    target = (sum(queue1)+sum(queue2))//2
    sum_q1 = sum(queue1)
    answer = 0
    pointer1 = 0
    pointer2 = 0
    while pointer1+pointer2<600000:
        if sum_q1>target:
            sum_q1-=queue1[pointer1]
            queue2.append(queue1[pointer1])
            pointer1+=1
            answer+=1
        elif sum_q1<target:
            sum_q1+=queue2[pointer2]
            queue1.append(queue2[pointer2])
            pointer2+=1
            answer+=1
        else:
            return answer
    else:
        return -1
            
            
queue2 =[3, 2, 7, 2]
queue1 =[4, 6, 5, 1]
print(solution(queue1, queue2))
