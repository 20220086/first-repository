import random
import header

# 1 헤더 출력
header.header_print("Bagles", "2022 09 28", "20220086 KIL SANG-JUN")

# 2 전역 변수 선언
MAX_GUESSES = 10
NUM_DIGITS = 3

# 3 함수 설계
def getSecretNum():
    pass
    return secretNum

def getGuessNum():
    pass
    return guessNum

def getGuessResult(secret, guess):
    pass
    return result

# 4 getSecretNum() 구현
numList = list('0123456789')
random.shuffle(numList)
print(numList)
