
# util.py

# 문자 출력 함수
def char_line(char, size):
    for i in range(size):
        print(char, end='')

# 별 출력 함수
def star_line(size):
    for i in range(size):
        print('*', end='')
    print()
    
# 공백 출력 함수
def print_space(size):
    for i in range(size):
        print(' ', end='')
        
# 텍스트 출력 함수
def print_text(text, total_size, text_size):
    print('* ', end='')
    total_space = total_size - text_size - 4
    left_space = int(total_space/2)
    print_space(left_space)
    print(text, end='')
    print_space(total_space - left_space)
    print(' *')
    
# 헤더 출력 함수
def print_header(title, date, name):
    
    # 헤더 길이 길이 정하기
    title_size = len(title)
    date_size  = len(date)
    name_size  = len(name)
    
    header_size = max(title_size, date_size, name_size)+4

    # 첫 줄 출력
    star_line(header_size)
    
    # 제목 출력
    print_text(title, header_size, title_size)

    # 날짜 출력
    print_text(date, header_size, date_size)

    # 이름 출력
    print_text(name, header_size, name_size)
    
    # 마지막 줄 출력
    star_line(header_size)   
