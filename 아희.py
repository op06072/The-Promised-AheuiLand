코드공간 = []
def 세종어제(훈민정음):
    나랏말씀 = []
    for 글자 in 훈민정음:
        if '가' <= 글자 <= '힣':
            음절 = ord(글자) - ord('가')
            초성 = 음절 // 588
            중성 = (음절 - 588 * 초성) // 28
            종성 = 음절 - 588*초성 - 28*중성
            나랏말씀.append([초성, 중성, 종성])
        else:
            나랏말씀.append([글자])
    return 나랏말씀

def 한글처리(코드):
    수치들 = []
    for 한줄 in 코드:
        수치들.append(세종어제(한줄))
    return 수치들

def 공간이동(왼오른, 위아래, 얼마나, 코드):
    왼오른 += 얼마나[0]
    위아래 += 얼마나[1]

    while 위아래 > len(코드) - 1:
        위아래 -= len(코드)
    while 위아래 < 0:
        위아래 += len(코드)
    
    while 왼오른 > len(코드[위아래]) - 1:
        왼오른 -= len(코드[위아래])
    while 왼오른 < 0:
        왼오른 += len(코드[위아래])
    
    return 왼오른, 위아래

def 아희처리(변환수치, 코드):
    global 코드공간
    쌓이는곳 = [[] for i in range(27)]
    줄세우는곳 = []
    지금있는곳 = 쌓이는곳[0]
    쌓나세우나 = 1
    가로,세로 = 0,0
    이동 = [0, 0]
    종성숫자 = [
        0, 2, 4, 4, 2, 5, 5, 3, 5, 7, 9, 9, 7, 9,
        9, 8, 4, 4, 6, 2, 4, 0, 3, 4, 3, 4, 4, 0
        ]
    
    while 1:
        한글자 = 코드[세로][가로]
        글자 = 변환수치[세로][가로]
        방향정렬 = 1

        if len(글자) != 3:
            가로, 세로 = 공간이동(가로, 세로, 이동, 변환수치)
        else:
            초 = 글자[0]
            if 초 == 2:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        지금있는곳[-2] //= 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        지금있는곳[1] //= 지금있는곳[0]
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 3:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        지금있는곳[-2] += 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        지금있는곳[1] += 지금있는곳[0]
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 4:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        지금있는곳[-2] *= 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        지금있는곳[1] *= 지금있는곳[0]
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 5:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        지금있는곳[-2] %= 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        지금있는곳[1] %= 지금있는곳[0]
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 6:
                if len(지금있는곳):
                    if 글자[2] == 21:
                        if 쌓나세우나:
                            print(지금있는곳[-1], end = '')
                            del 지금있는곳[-1]
                        else:
                            print(지금있는곳[0], end = '')
                            del 지금있는곳[0]
                    elif 글자[2] == 27:
                        if 쌓나세우나:
                            print(chr(지금있는곳[-1]), end = '')
                            del 지금있는곳[-1]
                        else:
                            print(chr(지금있는곳[0]), end = '')
                            del 지금있는곳[0]
                    else:
                        if 쌓나세우나:
                            del 지금있는곳[-1]
                        else:
                            del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 7:
                if 글자[2] == 21:
                    삽입 = int(input("숫자를 입력해 주세요.\n"))
                    print("\n")
                elif 글자[2] == 27:
                    삽입 = ord(input("문자 하나를 입력해 주세요.\n"))
                    print("\n")
                else:
                    삽입 = 종성숫자[글자[2]]
                if 쌓나세우나:
                    지금있는곳.append(삽입)
                else:
                    지금있는곳.insert(0, 삽입)
            elif 초 == 8:
                if len(지금있는곳):
                    if 쌓나세우나:
                        지금있는곳.append(지금있는곳[-1])
                    else:
                        지금있는곳.insert(0, 지금있는곳[0])
                else:
                    방향정렬 *= -1
            elif 초 == 9:
                if 글자[2] == 21:
                    지금있는곳 = 줄세우는곳
                    쌓나세우나 = 0
                elif 글자[2] < 21:
                    지금있는곳 =  쌓이는곳[글자[2]]
                    쌓나세우나 = 1
                else:
                    지금있는곳 =  쌓이는곳[글자[2]-1]
                    쌓나세우나 = 1
            elif 초 == 10:
                if len(지금있는곳):
                    if 쌓나세우나:
                        임시 = 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        임시 = 지금있는곳[0]
                        del 지금있는곳[0]
                    if 글자[2] == 21:
                        줄세우는곳.insert(0, 임시)
                    elif 글자[2] < 21:
                        쌓이는곳[글자[2]].append(임시)
                    else:
                        쌓이는곳[글자[2]-1].append(임시)
                else:
                    방향정렬 *= -1
            elif 초 == 12:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        if 지금있는곳[-2] < 지금있는곳[-1]:
                            지금있는곳[-2] = 0
                        else:
                            지금있는곳[-2] = 1
                        del 지금있는곳[-1]
                    else:
                        if 지금있는곳[1] < 지금있는곳[0]:
                            지금있는곳[1] = 0
                        else:
                            지금있는곳[1] = 1
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 14:
                if len(지금있는곳):
                    if 쌓나세우나:
                        if 지금있는곳[-1] == 0:
                            방향정렬 *= -1
                        del 지금있는곳[-1]
                    else:
                        if 지금있는곳[0] == 0:
                            방향정렬 *= -1
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 16:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        지금있는곳[-2] -= 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        지금있는곳[1] -= 지금있는곳[0]
                        del 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 17:
                if len(지금있는곳) > 1:
                    if 쌓나세우나:
                        지금있는곳[-1], 지금있는곳[-2] = 지금있는곳[-2], 지금있는곳[-1]
                    else:
                        지금있는곳[0], 지금있는곳[1] = 지금있는곳[1], 지금있는곳[0]
                else:
                    방향정렬 *= -1
            elif 초 == 18:
                if len(지금있는곳):
                    if 쌓나세우나:
                        finish = 지금있는곳[-1]
                        코드공간 = [쌓이는곳, 줄세우는곳]
                        return finish
                    finish = 지금있는곳[0]
                    코드공간 = [쌓이는곳, 줄세우는곳]
                    return finish
                코드공간 = [쌓이는곳, 줄세우는곳]
                return 0
            
            중 = 글자[1]
            if 중 == 0:
                이동 = [방향정렬, 0]
            elif 중 == 2:
                이동 = [2*방향정렬, 0]
            elif 중 == 4:
                이동 = [-방향정렬, 0]
            elif 중 == 6:
                이동 = [-2*방향정렬, 0]
            elif 중 == 8:
                이동 = [0, -방향정렬]
            elif 중 == 12:
                이동 = [0, -2*방향정렬]
            elif 중 == 13:
                이동 = [0, 방향정렬]
            elif 중 == 17:
                이동 = [0, 2*방향정렬]
            elif 중 == 12:
                if 이동[1]:
                    이동 = [0, -이동[1]]
            elif 중 == 13:
                이동 = [-이동[0], -이동[1]]
            elif 중 == 14:
                if 이동[0]:
                    이동 = [-이동[0], 0]

            가로, 세로 = 공간이동(가로, 세로, 이동, 변환수치)
            코드공간 = [쌓이는곳, 줄세우는곳]

def 아희():
    def 실행():
        코드 = []
        print("아희 코드를 입력후 엔터를 두번치시면 코드가 실행됩니다. (엔터 한번은 개행이 됩니다.)")
        while 1:
            한줄 = input()
            if 한줄 == '':
                break
            코드.append(한줄)
        
        아희처리(한글처리(코드), 코드)

    while 1:
        실행()
        print("\n다른 코드를 실행해 보시겠습니까? (네/아니오)")
        if input() != "네":
            break

def 외부실행(입력):
    코드 = 입력.split("\n")
    아희처리(한글처리(코드), 코드)
    return 코드공간

def 인터프리터():
    import sys
    import os.path as path
    파일이름 = "./" + sys.argv[1]
    try:
        if not path.isfile(파일이름):
            raise Exception("그런 파일은 없습니다.")    
        try:
            if sys.argv[1].split(".")[1] != "아희":
                raise Exception("아희코드 파일이 아닙니다.")
            with open(파일이름, mode="rt", encoding="utf-8") as 파일:
                코드 = [한줄 for 한줄 in 파일]
                파일.close()
            아희처리(한글처리(코드), 코드)
            return 코드공간
        except Exception as 에러:
            print("에러가 발생했습니다.: ", 에러)
    except Exception as 에러:
        print("에러가 발생했습니다.: ", 에러)

인터프리터()

#아희()