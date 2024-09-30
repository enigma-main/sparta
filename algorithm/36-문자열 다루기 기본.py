def solution(s):
    numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in s:
        if i not in numList:
            return False
    if len(s) == 4 or len(s) == 6:
        return True
    else:
        return False
