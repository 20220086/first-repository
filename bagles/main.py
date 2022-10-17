import random
import header

MAX_GUESSES = 10
NUM_DIGITS  = 3

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum    

def getGuessNum():
    while True:    
        numOnly = True
        getNum = input(str(NUM_DIGITS)+"자리 숫자를 추측하여 입력하세요 : ") 
        if len(getNum) != NUM_DIGITS:
            print("[ERROR] "+str(NUM_DIGITS)+"자릿수가 아닙니다. 다시 입력하세요")
            continue
        for i in range(NUM_DIGITS):
            if not '0' <= getNum[i] <= '9':
                print("[ERROR] "+str(NUM_DIGITS)+"자리 숫자를 입력하세요")
                numOnly = False
                break
        if numOnly:
            break               
    return getNum

def getGuessResult(secret, guess):
    pico  = 0
    fermi = 0
    if secret == guess:
        result = "빙고!"
    elif set(secret) & set(guess) == set():
        result = "베이글"
    else:
        result = ""
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                fermi += 1
            elif guess[i] in secret:
                pico += 1
        for i in range(pico):
            result += "피코 "
        for i in range(fermi):
            result += "페르미 "
    return result 

def main():   
    print(f"\n기회가 {MAX_GUESSES}번 주어집니다")    
    secretNum = getSecretNum()
    for i in range(MAX_GUESSES):
        guessNum = getGuessNum()
        result = getGuessResult(secretNum, guessNum)
        if result == '빙고!':
            print("")
        print(result)
        if result == '빙고!':
            print("게임 종료")
            break
        else: 
            if i < MAX_GUESSES-1:
                print()
                print(f"기회가 {MAX_GUESSES-i-1}번 남았습니다")
            else:
                print(f"\n실패. 정답은 {secretNum}입니다")

if __name__ == '__main__':
    header.header_print("bagles game", "1002", "Kil Sang-Jun")
    main()                