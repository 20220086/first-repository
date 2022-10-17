
def star_line(count):
    for i in range(count):
        print('*', end='')
    print()
    
def print_space(count):
    for i in range(count):
        print(' ', end='')
        
def header_text(width, text):
    print("*", end='')
    lspace = int((width - len(text))/2)
    print_space(lspace)
    print(text, end='')
    rspace = width - lspace - len(text)
    print_space(rspace)
    print("*")
    
def header_print(title, date, name):
    line_len = max(len(title), len(date), len(name))
    star_line(line_len+4)
    header_text(line_len+2, title)
    header_text(line_len+2, date)
    header_text(line_len+2, name)
    star_line(line_len+4)    
