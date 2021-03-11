# 약속의 아희랜드
[약속](http://yaksok.org)으로 만든 [아희](https://aheui.github.io/) 인터프리터입니다.
<br>파이썬3로 작성된 [아희.py](https://github.com/op06072/The-Promised-AheuiLand/blob/master/아희.py)를 약속 언어로 이식하여 만들었습니다.

# 사용법
* [yaksok.js](https://github.com/yaksok/yaksok.js)를 참고하여 nodejs와 yaksok.js를 설치합니다.

* nodejs에 필요한 패키지를 설치합니다.
  - windows: ```npm install -g minimist```
  - macOS & linux: ```sudo npm install -g minimist```
    + ```Cannot find module 'minimist'```에러시 ```npm install minimist```를 통해 해결할 수 있습니다.
    + 그러나 이 경우 minimist를 설치한 경로에서만 사용하실 수 있습니다.

* 아희.약속을 다운받습니다.
  - windows: ```(new-object Net.WebClient).DownloadFile("https://raw.githubusercontent.com/op06072/The-Promised-AheuiLand/master/아희.약속", "./아희.약속")```
  - linux: ```wget https://raw.githubusercontent.com/op06072/The-Promised-AheuiLand/master/아희.약속```
  - macOS: ```curl -O -L https://raw.githubusercontent.com/op06072/The-Promised-AheuiLand/master/아희.약속```

* ```package.yaml``` 파일을 만들고 다음과 같이 입력합니다.
```
시작: 아희
결과: 아희.js
```
* ```.아희``` 또는 ```.aheui``` 확장자로 끝나는 아희 코드파일을 생성하여 아희코드를 작성합니다.
* 약속 코드를 컴파일하고 실행합니다. 만약 파일명이 ```테스트.아희```라면 다음과 같습니다.
```
$ ysjs compile
$ node 아희.js 테스트.아희
안녕, 세상!
```