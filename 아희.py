#!python3

class 아희인터프리터():
    def __init__(self):
        self.코드공간 = []
        self.바구니 = ''
        self.입력방식 = 0

    def 세종어제(self, 훈민정음):
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

    def 한글처리(self, 코드):
        # 수치들 = []
        # 새코드 = []
        수치들 = list(map(lambda 한줄: self.세종어제(한줄), 코드))
        # for 한줄 in 코드:
        #     수치들.append(self.세종어제(한줄))
        너비 = max(list(map(len, 수치들)))
        새코드 = list(map(lambda 한줄: 한줄+' '*(너비 - len(한줄)), 코드))
        # for 한줄 in 코드:
        #     새코드.append(한줄+' '*(너비 - len(한줄)))
        수치들 = list(map(lambda 수치: 수치+[['']]*(너비 - len(수치)), 수치들)) # 3차 배열
        # for 수치 in 수치들:
        #     수치 += [['']]*(너비 - len(수치))
        return 수치들, 새코드

    def 공간이동(self, 왼오른, 위아래, 얼마나, 코드, 원본코드):
        왼오른 += int(얼마나[0])
        위아래 += int(얼마나[1])

        if 얼마나[1] != 0:
            if 위아래 > len(코드) - 1:
                위아래 = 0
                얼마나 = [얼마나[0]/abs(얼마나[0] + int(not 얼마나[0])), 얼마나[1]/abs(얼마나[1]+int(not 얼마나[1]))]
            if 위아래 < 0:
                위아래 = len(코드)-1
                얼마나 = [얼마나[0]/abs(얼마나[0] + int(not 얼마나[0])), 얼마나[1]/abs(얼마나[1]+int(not 얼마나[1]))]
        if 얼마나[0] != 0:
            if 왼오른 > len(원본코드[위아래]) - 1:
                왼오른 = 0
                얼마나 = [얼마나[0]/abs(얼마나[0] + int(not 얼마나[0])), 얼마나[1]/abs(얼마나[1]+int(not 얼마나[1]))]
            elif 왼오른 == len(원본코드[위아래]) - 1 and 코드[위아래] in ['\n', '\t', '\0', '\r']:
                왼오른 = 0
                얼마나 = [얼마나[0]/abs(얼마나[0] + int(not 얼마나[0])), 얼마나[1]/abs(얼마나[1]+int(not 얼마나[1]))]
            if 왼오른 < 0:
                왼오른 = len(원본코드[위아래])-1
                얼마나 = [얼마나[0]/abs(얼마나[0] + int(not 얼마나[0])), 얼마나[1]/abs(얼마나[1]+int(not 얼마나[1]))]

        return 왼오른, 위아래, 얼마나

    def 출력작성(self, 파일이름="", 추가내용=""):
        if 파일이름 != "":
            출력파일 = open(파일이름, mode="at", encoding="utf-8")
            출력파일.write(추가내용)
            출력파일.close()

    def 아희처리(self, 코드내용):
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
        변환수치, 코드 = self.한글처리(코드내용)

        # 중성
        # ㅏ:0 ㅑ:2 ㅓ:4 ㅕ:6
        # ㅗ:8 ㅛ:12 ㅜ:13 ㅠ:17
        # ㅡ:18 ㅢ:19 ㅣ:20

        while 1:
            # 한글자 = 코드[세로][가로]
            글자 = 변환수치[세로][가로] # 변환수치: 3차 배열
            방향정렬 = 1

            if len(글자) != 3:
                if 가로 == 0 and 세로 == 0 and 이동 == [0, 0]:
                    이동 = [0, 1]
                가로, 세로, 이동 = self.공간이동(가로, 세로, 이동, 변환수치, 코드내용)
            else:
                초 = 글자[0]
                if 초 == 2: # 초성 ㄴ
                    if len(지금있는곳) > 1:
                        지금있는곳[-2] //= 지금있는곳[-1]
                        del 지금있는곳[-1]
                        if 쌓나세우나 == 0:
                            줄세우는곳.insert(0, 지금있는곳[-1])
                            del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 3: # 초성 ㄷ
                    if len(지금있는곳) > 1:
                        지금있는곳[-2] += 지금있는곳[-1]
                        del 지금있는곳[-1]
                        if 쌓나세우나 == 0:
                            줄세우는곳.insert(0, 지금있는곳[-1])
                            del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 4: # 초성 ㄸ
                    if len(지금있는곳) > 1:
                        지금있는곳[-2] *= 지금있는곳[-1]
                        del 지금있는곳[-1]
                        if 쌓나세우나 == 0:
                            줄세우는곳.insert(0, 지금있는곳[-1])
                            del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 5: # 초성 ㄹ
                    if len(지금있는곳) > 1:
                        지금있는곳[-2] %= 지금있는곳[-1]
                        del 지금있는곳[-1]
                        if 쌓나세우나 == 0:
                            줄세우는곳.insert(0, 지금있는곳[-1])
                            del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 6: # 초성 ㅁ
                    if len(지금있는곳):
                        if 글자[2] == 21:
                            # print(지금있는곳[-1], end = '')
                            sys.stdout.write(str(지금있는곳[-1]))
                        elif 글자[2] == 27:
                            # print(chr(지금있는곳[-1]), end = '')
                            sys.stdout.write(chr(지금있는곳[-1]))
                        del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 7: # 초성 ㅂ
                    if 글자[2] == 21:
                        #삽입 = int(input("숫자를 입력해 주세요.\n"))
                        if self.입력방식:
                            if self.바구니 == '':
                                삽입 = -1
                            else:
                                임시 = self.바구니.split('\n')
                                삽입 = int(임시[0])
                                self.바구니 = "\n".join(임시[1:])
                        else:
                            삽입 = int(input())
                            #삽입 = self.수읽기()
                        # print("\n")
                    elif 글자[2] == 27:
                        #삽입 = ord(input("문자 하나를 입력해 주세요.\n"))
                        if self.입력방식:
                            if self.바구니 == '':
                                삽입 = -1
                            else:
                                삽입 = ord(self.바구니[0])
                                self.바구니 = self.바구니[1:]
                        else:
                            삽입 = ord(input()[0])
                            #삽입 = self.글읽기()
                        # print("\n")
                    else:
                        삽입 = 종성숫자[글자[2]]
                    if 쌓나세우나:
                        지금있는곳.append(삽입)
                    else:
                        지금있는곳.insert(0, 삽입)
                elif 초 == 8: # 초성 ㅃ
                    if len(지금있는곳):
                        지금있는곳.append(지금있는곳[-1])
                    else:
                        방향정렬 *= -1
                elif 초 == 9: # 초성 ㅅ
                    if 글자[2] == 21: # ㅇ -> 큐
                        지금있는곳 = 줄세우는곳
                        쌓나세우나 = 0
                    elif 글자[2] < 21:
                        지금있는곳 =  쌓이는곳[글자[2]]
                        쌓나세우나 = 1
                    elif 글자[2] != 27:
                        지금있는곳 =  쌓이는곳[글자[2]-1]
                        쌓나세우나 = 1
                elif 초 == 10: # 초성 ㅆ
                    if len(지금있는곳):
                        임시 = 지금있는곳[-1]
                        del 지금있는곳[-1]
                        if 글자[2] == 21:
                            줄세우는곳.insert(0, 임시)
                        elif 글자[2] < 21:
                            쌓이는곳[글자[2]].append(임시)
                        else:
                            쌓이는곳[글자[2]-1].append(임시)
                    else:
                        방향정렬 *= -1
                elif 초 == 12: # 초성 ㅈ
                    if len(지금있는곳):
                        if 지금있는곳[-2] < 지금있는곳[-1]:
                            지금있는곳[-2] = 0
                        else:
                            지금있는곳[-2] = 1
                        del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 14: # 초성 ㅊ
                    if len(지금있는곳):
                        if 지금있는곳[-1] == 0:
                            방향정렬 *= -1
                        del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 16: # 초성 ㅌ
                    if len(지금있는곳):
                        지금있는곳[-2] -= 지금있는곳[-1]
                        del 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 17: # 초성 ㅍ
                    if len(지금있는곳) > 1:
                        지금있는곳[-1], 지금있는곳[-2] = 지금있는곳[-2], 지금있는곳[-1]
                    else:
                        방향정렬 *= -1
                elif 초 == 18: # 초성 ㅎ
                    if len(지금있는곳):
                        finish = 지금있는곳[-1]
                        self.코드공간 = [쌓이는곳, 줄세우는곳]
                        return finish
                    self.코드공간 = [쌓이는곳, 줄세우는곳]
                    return 0

                중 = 글자[1]
                if 중 == 0: # 중성 ㅏ
                    이동 = [방향정렬, 0]
                elif 중 == 2: # 중성 ㅑ
                    이동 = [2*방향정렬, 0]
                elif 중 == 4: # 중성 ㅓ
                    이동 = [-방향정렬, 0]
                elif 중 == 6: # 중성 ㅕ
                    이동 = [-2*방향정렬, 0]
                elif 중 == 8: # 중성 ㅗ
                    이동 = [0, -방향정렬]
                elif 중 == 12: # 중성 ㅛ
                    이동 = [0, -2*방향정렬]
                elif 중 == 13: # 중성 ㅜ
                    이동 = [0, 방향정렬]
                elif 중 == 17: # 중성 ㅠ
                    이동 = [0, 2*방향정렬]
                elif 중 == 18 and 이동[1]: # 중성 ㅡ
                    이동 = [0, -이동[1]*방향정렬]
                elif 중 == 19: # 중성 ㅢ
                    이동 = [-이동[0]*방향정렬, -이동[1]*방향정렬]
                elif 중 == 20 and 이동[0]: # 중성 ㅣ
                    이동 = [-이동[0]*방향정렬, 0]
                else: # 나머지 중성
                    이동 = [이동[0]*방향정렬, 이동[1]*방향정렬]

                if 가로 == 0 and 세로 == 0 and 이동 == [0, 0]:
                    이동 = [0, 1]
                가로, 세로, 이동 = self.공간이동(가로, 세로, 이동, 변환수치, 코드내용)
                self.코드공간 = [쌓이는곳, 줄세우는곳]

    def 아희(self):
        def 실행():
            코드 = []
            print("아희 코드를 입력후 엔터를 두번치시면 코드가 실행됩니다. (엔터 한번은 개행이 됩니다.)")
            while 1:
                한줄 = input()
                if 한줄 == '':
                    break
                코드.append(한줄)
            return self.아희처리(코드)

        while 1:
            실행()
            print("\n다른 코드를 실행해 보시겠습니까? (네/아니오)")
            if input() != "네":
                break

    def 외부실행(self, 입력):
        코드 = 입력.split("\n")
        return self.아희처리(코드)
        # return self.코드공간

    def 인터프리터(self):
        import sys
        import os.path as path
        if len(sys.argv) > 1:
            파일이름 = sys.argv[1]
        else:
            파일이름 = "테스트.아희"
        입력파일 = ''
        if "/" not in 파일이름:
            파일이름 = "./" + 파일이름
        if len(sys.argv) > 2:
            if path.isfile(sys.argv[2]):
                입력파일 = sys.argv[2]
        elif path.getsize(r'/dev/stdin'):
            self.바구니 = sys.stdin.read()
            self.입력방식 = 1
        try:
            if not path.isfile(파일이름):
                raise Exception("그런 파일은 없습니다.")
            try:
                if 파일이름.split(".")[-1] not in ["아희", "aheui"]:
                    raise Exception("아희코드 파일이 아닙니다.")
                with open(파일이름, mode="rt", encoding="utf-8") as 파일:
                    코드 = [한줄 for 한줄 in 파일]
                    파일.close()
                # 출력 = ".".join(파일이름.split(".")[:-1])+".out"
                # 출력파일 = open(출력, mode="wt", encoding="utf-8")
                # 출력파일.close()
                # 아희처리(한글처리(코드), 코드, 출력)
                if 입력파일 != '':
                    with open(입력파일, mode='rt', encoding="utf-8") as 파일:
                        self.바구니 = 파일.read()
                    self.입력방식 = 1
                return self.아희처리(코드)
                # return self.코드공간
            except Exception as 에러:
                print("에러가 발생했습니다.: ", 에러)
        except Exception as 에러:
            print("에러가 발생했습니다.: ", 에러)

if __name__ == "__main__":
    import sys
    아희 = 아희인터프리터()
    sys.exit(아희.인터프리터())

#아희()