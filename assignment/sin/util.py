
def val_sin(start_deg, end_deg, width, length):
    start = start_deg # 시작 각도
    end = end_deg # 종료 각도
    width = width # 폭
    length = length # 길이
    val = start
    return start, end, width, length, val

def print_first(width):
    print(" x  ", end="")
    print("-"*(width), end=" ")
    print("sin(x)")
    

def spaceleft(sinval, width):
    # 사인값 양수
    if round(sinval*int((width/2))) > 0:
        if (width % 2) == 0: # width가 짝수인 경우
            print(" "*int(width/2), end="")
            print("|", end="")
        elif (width % 2) == 1: # width가 홀수인 경우
            print(" "*int((width-1)/2), end="")
            print("|", end="")
        print(" "*(round(sinval*int((width/2)))-1), end="") # 별 좌측 공백
        print("*", end="")
        if (width % 2) == 0: # width가 짝수인 경우 별 우측 공백
            print(" "*int(((width/2)-round(sinval*int((width/2))))), end="")
        elif (width % 2) == 1: # width가 홀수인 경우 별 우측 공백
            print(" "*int((((width-1)/2)-round(sinval*int(((width-1))/2)))), end="")

    # 사인값 0
    if round(sinval*(width/2)) == 0:
        if (width % 2) == 0: # width가 짝수인 경우
            print(" "*int(width/2), end="")
            print("*", end="")
            print(" "*int(width/2), end="")
        elif (width % 2) == 1: # width가 홀수인 경우
            print(" "*int((width-1)/2), end="")
            print("*", end="")
            print(" "*int((width-1)/2), end="")

    # 사인값 음수 (절댓값 대신 사인값 +와 -를 바꿈)
    if round(sinval*int((width/2))) < 0:
        if (width % 2) == 0: # width가 짝수인 경우 별 왼쪽 공백
            print(" "*int((width/2+round(sinval*int((width/2))))), end="")
        elif (width % 2) == 1: # width가 홀수인 경우 별 왼쪽 공백
            print(" "*int(((width+1)/2+round(sinval*int(((width-1)/2))))), end="")
        print("*", end="") # 사인별
        if (width % 2) == 0: # width가 짝수인 경우
            print(" "*-(round(sinval*int((width/2)))+1), end="") # 별 우측 공백
        elif (width % 2) == 1: # width가 홀수인 경우
            print(" "*-(round(sinval*int((width/2)))+2), end="") # 별 우측 공백
        if (width % 2) == 0: # width가 짝수인 경우
            print("|", end="")
            print(" "*int(width/2), end="")
        elif (width % 2) == 1: # width가 홀수인 경우
            print("|", end="")
            print(" "*int((width-1)/2), end="")