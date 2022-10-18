from util import util
import math
import re

def int_get(input_str, minval=None, maxval=None, default=None): 
    
    while True:
        val = input(input_str+'['+str(default)+'] ')
        if val == '' and default is not None:
            return default
        elif set(val) <= set("-0123456789"):
            val = int(val)
            if maxval is not None:
                if minval <= val <=maxval:
                    return val
                else:
                    print(">>> [ERROR] 입력값이 범위를 벗어났습니다!")
            else:
                if minval <= val:
                    return val
                else:
                    print(">>> [ERROR] 입력값이 범위를 벗어났습니다!")
        else:
            print(">>> [ERROR] 정수를 입력해주세요!")

def make_xlist(x_min, x_max):
    bool = 1
    x_list = []
    x_min_for_loop = x_min
    while bool == 1:
        x_list.append(x_min_for_loop)
        x_min_for_loop += 1
        if x_min_for_loop == x_max:
            bool = 0
    return x_list

def equation1(numbers, x_val):
    y_val = numbers[0]*x_val + numbers[2]
    return y_val

def equation2(numbers, x_val):
    y_val = numbers[0]*x_val**2 + numbers[2]*x_val + numbers[4]
    return y_val

def equation3(numbers, x_val):
    y_val = numbers[0]*x_val**3 + numbers[2]*x_val**2 + numbers[4]*x_val + numbers[6]
    return y_val

def equation4(numbers, x_val):
    y_val = numbers[0]*x_val**4 + numbers[2]*x_val**3 + numbers[4]*x_val**2 + numbers[6]*x_val + numbers[8]
    return y_val

def equation5(numbers, x_val):
    y_val = numbers[0]*x_val**5 + numbers[2]*x_val**4 + numbers[4]*x_val**3 + numbers[6]*x_val**2 + numbers[8]*x_val + numbers[10]
    return y_val


def print_fn(fn, x_min, x_max, y_min, y_max):

    x_len = int(x_max - x_min)
    y_len = int(y_max - y_min)

    # x_mid = int(round((x_len)/2))
    # y_mid = int(round((y_len)/2))

    #그래프 리스트
    gragh = [[" " for j in range(x_len)] for i in range(y_len)]


    if y_max < 0: # x축 그리기
        pass
    else:
        for i in range(y_len): 
            gragh[y_len-y_max][i] = "-"

    if x_min > 0:  # y축 그리기
        pass
    else:
        for i in range(x_len):
            gragh[i][abs(x_min)+1] = "|"


    # gragh[y_len-y_max+1][abs(x_min)+1] = "+" # 원점  


    numbers = re.findall(r'\d+', fn) # 식에서 숫자 추출하기

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
  
    x_list = make_xlist(x_min, x_max)

    # print(x_list)

    for i, x_val in enumerate(x_list):
        if len(numbers) == 3: # 1차식
            y_val = int(equation1(numbers, x_val))
        elif len(numbers) == 5: # 2차식
            y_val = int(equation2(numbers, x_val))
        elif len(numbers) == 7: # 3차식
            y_val = int(equation3(numbers, x_val))
        elif len(numbers) == 9: # 4차식
            y_val = int(equation4(numbers, x_val))
        elif len(numbers) == 11: # 5차식
            y_val = int(equation5(numbers, x_val))
        else : # 6차 이상
            print("[ERROR} 1~6차 사이의 식을 입력해주세요")
        
        if y_min <= y_val and y_max >= y_val:
            if y_len-y_max-y_val < y_len :
                gragh[y_len-y_max-y_val][i] = "*"
        else:
            print("범위 밖의 값 : (", x_val, y_val, ")")
            

    for i in range(x_len):
        print("".join(gragh[i]))
    

def main():
    util.header_print("1-5: Prining functions", "2022.10.18", "Kil, Sang-Jun")

    fn    = input('출력할 함수를 작성하세요 (ex. 2x^1+1) : ')
    x_min = int_get('x 최소값을 입력하세요 : ', minval=-50, default=-10)
    x_max = int_get('x 최대값을 입력하세요 : ', minval=5, default=10)
    y_min = int_get('y 최소값을 입력하세요 : ', minval=-50, default=-10)
    y_max = int_get('y 최대값을 입력하세요 : ', minval=5, default=10)

    print_fn(fn, x_min, x_max, y_min, y_max)

if __name__ == '__main__':
    main()  