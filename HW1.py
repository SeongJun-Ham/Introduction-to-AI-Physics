#1 제목 페이지 (이름, 학번 포함)
# 성명: 함성준
# 학번: 201921251

#2 문제 정의

#3 Pseudo-code

#4 실행 결과
def roof_same(num):
    idx = 1
    while idx != num+1:
        print(f"{i}"*(i))
        idx += 1


def roof_increasing(num):
    idx = 1
    sentance = "1"
    while idx != num+1:
        print(sentance)
        idx += 1
        sentance += str(idx)


while True:
    order = int(input("1. same number, 2. increasing number, 3. terminate the program: "))
    input_number = int(input("lines? "))
    if order == 1:
        roof_same(input_number)
    elif order == 2:
        roof_increasing(input_number)
    elif order == 3:
        break
    else:
        print("Wrong option. Please choose the right option")
    idx = 0


#5 토론

