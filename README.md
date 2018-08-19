# SDE 형태의 1개 입력파일 읽기 python 언어

EDISON 시뮬레이션 SW 개발자를 위한 1개의 SDE 입력 파일 읽어, 입력파일안에 있는 변수값을 출력하는 python언어 예제 파일입니다.

```
bin/
 - main.py     
inp/
 - input.dat 
```


입력 파일의 경우에는 변수와 값 구분자를 ' '을 사용하였으며, 변수와 변수 사이를 구분하기 위해 ' \n '를 사용하였습니다. 파일로 입력을 받으며, 샘플 입력 파일은 아래와 같으며, **inp** 폴더에 **input.dat** 로 저장되어 있습니다.

```
INT1 42
REAL1 42.112
LIST1 a
VECTOR1 [ 1 0 0 ]
```


본 예제는 ./[실행파일명] -[옵션] [입력 파일 경로]로 실행시 옵션 뒤에 입력된 경로의 파일을 열고 닫는 예제로 Makefile과 소스코드는  **src** 폴더에 저장되어 있으며, 컴파일이 완료되면 바이너리 파일은 **bin** 폴더에 저장됩니다.


## 설치하기

zip 파일을 다운로드 받아 압축을 풀거나 ```git clone``` 명령어를 이용하여, 프로젝트를 가져올 수 있습니다.

```bash
$ git clone https://github.com/sp-edison/python_example_sde.git
```

```bash
$ cd ../bin
$ ./main.py -i ../inp/input.dat
input file = ../inp/input.dat
init1 :42
real1 :42.112
list1 :a
vector1 :[1, 0, 0]
```
