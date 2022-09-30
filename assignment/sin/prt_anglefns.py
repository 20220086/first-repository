import math
import util
import header
import os

header.header_print("draw a sin wave", "2022 09 28", "20220086 KIL SANG-JUN")

# a = start deg : 시작 각도
# b = end_deg : 종료 각도
# c = width : 폭
# d = length : 길이 (줄 수)

def print_sin(a,b,c,d):
    start, end, width, length, val = util.val_sin(a,b,c,d)
                                   #(시작 각도, 종료 각도, 그래프의 폭, 그래프의 줄 수)
    util.print_first(width)
    while end >= val:
        # 앞 숫자
        val = int(val)
        val_str = str(val)
        print(val_str.zfill(3), end=" ")

        # 계산 1
        sinval = math.sin((2*math.pi*val)/360) # 사인값 계산

        # space
        util.spaceleft(sinval, width)

        # 길이
        val += (end-start)/length # 길이 (그래프 줄 수)

        # 사인값 프린트
        if sinval >= 0: # 양수면 한 칸 띄워서 줄 맞추기
            print(" ",end="") 
        print(format(round(sinval,3),'.3f')) # 반올림, 빈 칸 수 채우기

        # sin 별 위치 = round(sinval*25)

print_sin(0,360,99,36)
os.system("pause")