
from util import util
import math

# 특정 범위의 정수를 입력받는 함수
def int_get(input_str, minval=1, maxval=None, default=None): 
    
    while True:
        val = input(input_str+'['+str(default)+'] ')
        if val == '' and default is not None:
            return default
        elif set(val) <= set("0123456789"):
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
        

# 좌에서 우로 한 문자씩 출력 
def print_anglefn(fn, fname, start_deg, end_deg, width, length):

    print(" x  ", end='')
    util.char_line('-', width)
    print(" "+fname)

    interval   = round((end_deg - start_deg)/length)
    left_half  = round((width-1)/2)
    right_half = width - left_half - 1
    
    for i in range(start_deg, end_deg+interval, interval):
        val = round(fn(math.radians(i)),4)
        loc = min(round((val+1) * left_half) + 1, width)
        print(f"{i:0>3} ", end='')

        if loc < left_half+1:
            util.char_line(' ', loc-1)
            print('*', end='')
            util.char_line(' ', left_half-loc)
            print("|", end='')
            util.char_line(' ', right_half)
        elif loc > left_half+1:
            util.char_line(' ', left_half)
            print("|", end='')
            util.char_line(' ', loc-left_half-2)
            print('*', end='')
            util.char_line(' ', width-loc)
        else: # loc == left_half+1 
            util.char_line(' ', left_half)
            print("*", end='')
            util.char_line(' ', right_half)

        print(" {:>6.3f}".format(val+0))


# 리스트를 만들어 한줄씩 출력
def print_anglefn2(fn, fname, start_deg, end_deg, width, length):

    print(" x  ", end='')
    util.char_line('-', width)
    print(" "+fname)
    
    interval = round((end_deg - start_deg)/length)
    center   = int(width / 2) + 1   
    
    for i in range(start_deg, end_deg+interval, interval):
        prtline = [' ' for i in range(width)]
        val = round(fn(math.radians(i)),4)
        loc = min(int((val + 1) * width / 2) + 1, width)
        prtline[center-1] = '|'
        prtline[loc-1]    = '*'
        prtline = ''.join(prtline)
        print(f"{i:0>3} {prtline} {val+0:>6.3f}")

def main():
    
    util.print_header("1-4: Prining sine waves", "2022.9.26", "(c) Kim, Tae-Hyong")   
        
    fn_sel    = int_get('출력할 삼각함수를 선택하세요(1.sine, 2.cosine):', maxval=2, default=1)
    start_deg = int_get('시작 각도를 입력하세요:', minval=0, default=0)
    end_deg   = int_get('마지막 각도를 입력하세요:', minval=start_deg+1, default=360)
    gr_width  = int_get('그래프의 폭을 입력하세요:', minval=10, default=70)
    gr_length = int_get('그래프의 길이를 입력하세요:', minval=10, default=70)
    
    if fn_sel == 1:
        print_anglefn2(math.sin, "sin(x)", start_deg, end_deg, gr_width, gr_length)
    else: # fn_sel==2
        print_anglefn2(math.cos, "cos(x)", start_deg, end_deg, gr_width, gr_length)    

if __name__ == '__main__':
    main()                
