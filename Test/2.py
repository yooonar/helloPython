def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    i = 0

    for item in completion :
        if completion[i] != participant[i] :
            answer = participant[i]
            break
        i += 1
    if answer == "" :
        answer = participant[len(participant) -1 ]
    return answer
