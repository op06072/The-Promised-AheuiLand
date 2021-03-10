# 약속의 아희랜드
[약속](http://yaksok.org)으로 만든 [아희](https://aheui.github.io/) 인터프리터입니다.
파이썬3로 작성된 [아희.py](https://github.com/op06072/The-Promised-AheuiLand/blob/master/아희.py)를 약속 언어로 이식하여 만들었습니다.

#사용법
[yaksok.js](https://github.com/yaksok/yaksok.js)를 참고하여 nodejs와 yaksok.js를 설치합니다.

```package.yaml``` 파일을 만들고 다음과 같이 입력합니다.
```
시작: 아희
결과: 아희.js
```
```.아희``` 또는 ```.aheui``` 확장자로 끝나는 아희 코드파일을 생성하여 아희코드를 작성합니다.
다음과 같이 컴파일하고 실행합니다. 만약 파일명이 ```테스트.아희```라면
```
$ ysjs compile
$ node 아희.js 테스트.아희
안녕, 세상!
```
