# chapter 7. True, False 그리고 if와 형제들

# 1. 참과 거짓을 의미하는 값(데이터)

True  #  True가 출력된다. (앞 첫 글자는 대문자로 작성해주어야 한다.)
False # 마찬가지

# True   참을 의미함, 질문 내용이 맞는 경우의 대답이 되기도 한다.
# false  거짓을 의미함, 질문 내용이 맞지 않는 경우의 대답이 되기도 한다.

print(3 > 10)
print(3 < 10)

r = 3 < 10
print(r)


# 파이썬은 True, False를 값으로 취급한다.


print(type(True))

print(type(False))

# 둘다 bool type으로 뜬다.


# javascript에서 배운 boolean형이 여기서 bool형 데이터 이다. 완전히 동일하다.


# main.py

def main():    # main 함수의 정의
	print("simple frame")

main()  # main함수 호출을 명령함

# 위의 코드를 소스파일에 담아서 실행하면 먼저 main 함수가 정의되고, 이어서 그 만들어진 main함수의 호출까지 진행이 된다. 따라서 우리가 실행하고자 하는 코드를 위의 
# main 함수 내에 위치시키면 그 결과를 확인할 수 있다.

# 따로 파일로 생성해놓았다.


# 3. if문 : 조건이 맞으면 실행을 해라

# if_positive.py

def main():    # main 함수의 정의

	num = int(input("정수 입력: "))
	if num > 0:
		print("양의 정수입니다.")

main()

# 다음과 같은 문장을 한줄에 모두 담아도 된다.

num = 2
if num > 0: print("양의 정수 입니다.")   # 한줄에 모두 담은 경우



# 4. if ~ else 문 : 이쪽 길! 아니면 다른 길! (만약 ~라면, 아니면 ~)

# if_else.py

def main():
	num = int(input("정수 입력: "))
	if num > 0:
		print("0보다 큰 수입니다.")    # num이 0보다 크면 이 문장 실행

	else:
		print("0보다 크지 않은 수입니다.")    # num이 0 보다 크지 않으면 이문장 실행


main()

# 구조 자체를 외우는 것이 좋다.

# 5. if ~ elif ~ else 문 : 여러 길 중에서 하나의 길만 선택!

# if_elif_else.py

def main():
	num = int(input("정수 입력:  "))

	# 조건에 따라서 아래 문장 1, 2, 3 중 하나만 실행이 된다.

	if num > 0:
		print("0보다 큰 수 입니다.")    # 문장 1

	elif num < 0:
		print("0보다 작은 수 입니다.")    # 문장 2

	else:
		print("0으로 판단이 됩니다.")    # 문장 3

main()

# 6. True or False를 반환하는 연산

#  A >= Z    A가 Z보다 크거나 같으면 True, 그렇지 않으면 False 반환
#  A <= Z    A가 Z보다 작거나 같으면 True, 그렇지 않으면 False 반환
#  A == Z    A와 Z가 같으면 True, 같지 않으면 False 반환 (cf. A = Z 는 같다는 의미가 아니다. 오른쪽항을 왼쪽으로 넣는 대입이다.) 
#  A != Z    A와 Z가 같지 않으면 True, 같으면 False 반환
#        ( ! 는 not 의 의미;  javascript와 비슷 )


# if_elif_elss2.py

def main():
	num = int(input("정수 입력 : "))
	if num == 1:      # num이 1이면 True
		print("1을 입력했습니다.")

	elif num == 2:    # num이 2이면 True
		print("2를 입력했습니다.")

	elif num == 3:    # num이 3이면 True
		print("3을 입력했습니다.")

	else:
		print("1, 2, 3 아닌 정수 입력했습니다.")


main()   # 위의 함수를 실행하여라!!


# 2의 배수이면서도 3의 배수인 수 입력하기 (code의 구조적 파악이 중요하다.)

# if_and_if.py

def main():
	num = int(input("2의 배수이면서 3의 배수인 수 입력: "))
	if num % 2 == 0:    # 연산 순서 구분되게 (num % 2) == 0로 입력 가능
		if num % 3 == 0:    # 연산 순서 구분되게 (num % 3) == 0로 입력 가능
			print("OK!")
		else:
			print("NO!")

	else:
		print("NO!")

main() 

# A and Z : A와 Z가 모두 True이면 True, 그렇지 않으면 False 반환

# A or Z : A와 Z 둘 중 하나라도 True이면 True, 그렇지 않으면 False 반환

# not A  : A가 Ture이면 False, A가 False이면 True 반환 ("A가 아니다.")

# 연산자들의 결과 정리 ( 이 Boolean 연산자의 원리는 javacript에서도 통용된다. 똑같은 원리이다.)



# 1. and 연산자

#  p1            p2               p1 and p2

# True          True                True
# True          False               False
# False         True                False
# False         False               False


# 2. or 연산자

#  p1            p2               p1 and p2

# True          True                True
# True          False               True
# False         True                True
# False         False               False


# 3. not 연산자

#    p            not p
#  True           False
#  False           True


# 이러한 and, or, not 연산을 어디에 쓸 수 있을까??
# 앞에서 설정하였던 값이 2와 3의 배수인지 묻는 문장을 한줄짜리 code로 정리
# 할수 있다.

num = 6
(num % 2) == 0 and (num % 3) == 0   # num의 값이 2와 3의 배수인지 묻는 문장!

# 결괏값은 True로 나온다.

# Process

# (num % 2 ) == 0 and (num % 3) == 0       # and 연산은 맨 마지막에

# 따라서 num이 6이면 위의 문장은 다음의 단계를 거쳐서 마지막에 True만 남게 된다.

# (num % 2) == 0 and (num % 3) == 0  # and의 왼쪽부터 계산해서 아래 상태가 된다.
    # → True and (num % 3) == 0  # and의 오른쪽도 계산해서 아래 상태가 됨
    # → True and True
    # → True

# and.py

def main():
	num = int(input("2의 배수이면서 3의 배수인 수 입력: "))
	if (num % 2) == 0 and (num % 3) == 0:    # num이 2와 3의 배수이면 조건 True
		print("맞아!")
	else:
		print("응! 아니야")


main()	





 
# list와 문장을 대상으로도 동작한다.

'abc' == 'abc'   # 두 문자열이 같은가?

# 결괏값 : True

 # 'abc' !== 'abc'  # 두 문자열이 다른가?

 # 결괏값 : False

 # 문자열의 내용을 비교해도 사용할 수 있다.

 # [1, 2, 3] = [1, 2]

# 결괏값 : False

# [1, 2, 3] != [1, 2]

# 결괏값 : True

# 8. True or False로 답하는 함수들


# s.isdigit()    문자열 s가 숫자로만 이뤄져 있으면 True, 아니면 False 반환
# s.isalpha()    문자열 s가 알파벳으로만 이뤄져있으면 True, 아니면 False 반환
# s.startswith(prefix)   문자열 s가 prefix로 시작하면 True, 아니면 False 반환
# s.endswith(suffix)   문자열 s가 suffix로 끝나면 True, 아니면 False 반환

st1 = "1  23"
st2 = "OneTwoThree"

print(st1.isdigit())   # s1은 숫자로만 이뤄져 있나요? 숫자로 이루어져 있더라도 띄워져 있으면 x이다.

print(st2.isdigit())    # s2는 숫자로만 이뤄져 있나요?


st1 = "123"
st2 = "OneTwoThree"

print(st1.isalpha())

print(st2.isalpha())



str = "Supersprint"
print(str.startswith("Super"))
print(str.endswith("print"))

# code 짜보기

# 휴대폰 번호를 입력 받는다. 이 번호는 010으로 시작해야 하고 숫자로만 이뤄져야 한다.

# 정상적인 입력입니다. 메시지 출력

# 01022223333

# 정상적이지 않은 입력입니다.

# 010 2222 3333 공백이 들어가서 오류

# 010-2222-3333 중간에 -문자가 들어가서 오류

# 01922223333 019로 시작해서 오류


# is_phone_num.py
def main ():
	pnum = input("스마트폰 번호 입력: ")
	if pnum.isdigit() and pnum.startswith("010"):
		print("정상적인 입력입니다.")

	else:
		print("정상적이지 않은 입력입니다.")


main()


# 9. in, not in

# 문자열 내용의 일부를 확인하는 함수

# s.find(sub)    # 앞에서부터 sub를 찾아서 index값 반환
# s.rfind(sub)   # 뒤에서부터 sub를 찾아서 index값 반환
# s.startswith(prefix)   # prefix로 시작하면 True 반환
# s.endswith(suffix)    # suffix로 끝나면 True 반환

# 이 문자열 안에 이런 내용이 포함되어 있어?
# 구체적으로 문자열 "Tomato spaghetti"안에 "ghe"가 존재하는가?

# 다음과 같이 작성할 수 있다.

s = "Tomato spaghetti"
if s.find("ghe") != -1:   # "ghe"가 없으면 find 함수는 -1을 반환한다.
	print("있습니다.")
else:
	print("없습니다.")

# find 함수는 해당 내용이 존재하면 그 위치의 index값을, 존재하지 않으면 -1을 반환한다. 그래서 위의 예에서는 find가 반환하는 값이 -1인지 확인하는
# 방식으로 "ghe"의 존재 유무를 확인하였다.
# 그런데 다음과 같이 in 연산자를 사용하는 방법도 있다.

if "ghe" in s:
	print("있습니다.")
else:
	print("없습니다.")

# 있습니다 가 출력됨

# 위치 정보가 필요없이 찾는 내용의 존재 유무만 확인하고자 한다면 in 연산자를 사용하는 것이 좋다.
# 위치 정보까지 필요하다면 find 함수를 사용해야 한다.

# 문자열만을 대상으로 하는 find 함수와 달리 in 연산자는 다음과 같이 list를 대상으로도 사용할수 있다.

# (chapter 9에 나오는 튜플이라는 것을 대상으로도 사용할 수 있다.)

3 in [1, 2, 3]   # list [1, 2, 3] 안에 3이 있는가?
4 in [1, 2, 3]   # list [1, 2, 3] 안에 4가 있는가?


# e in S      S에 e가 있으면 True, 없으면 False 반환

# e not in S    S에 e가 없으면 True, 있으면 False 반환


# 3 not in [1, 2, 3]     # [1, 2, 3] 안에 3이 없지요?
#  False 출력

# 4 not in [1, 2, 3]     # [1, 2, 3] 안에 4가 없지요?
#  True 출력

# "he" not in "hello"     # "he"는 "hello"의 일부가 아니지요?
#  False 출력

# "oo" not in hello       # "oo"는 "hello"의 일부가 아니지요?
# True 출력

# True or Flase를 반환하는 연산자 정리!

# and     둘 다 True 인가?
# or      둘 중 하나라도 True 인가?
# not     바꿔라!
# in      들어 있는가?
# not in  들어 있지 않은가?


# 10. 수(Number)를 True와 False로 인식하는 방식

# 앞서 설명했듯이 ,다음과 같은 if문의 구조에서 <조건>에 해당하는 위치에는 True of False가 
# 와야 한다.

if True:
	print("사실입니다.")

# 결괏값: 사실입니다.


what = True
if what:
	print("사실입니다.")

# 결괏값: 사실입니다.

num = 1    # num에 0을 저장해서 실행해보자.
if num:
	print("0 아닙니다.")

# 결괏값: 0 아닙니다.


num = 0    #num에 저장된 값을 바꿔서 실행해보자.
if num:
	print("0이 아닙니다.")
else:
	print("0이 맞습니다.")

# 결괏값 : 0 맞습니다.


# 위의 두 예에는 다음의 공통점이 있다.

# True or False가 와야하는 위치에 '수(number)가 등장했다.'

# 위와 같이 True or False가 와야하는 위치에 '수'가 올 경우,
# python은 이를 다음과 같이 해석한다.


# *******
# 0이 오는 경우                      False가 온 것으로 간주한다.
# 0이 아닌 수가 오는 경우             True가 온 것으로 간주한다.

# 이는 일종의 약속이니 이러한 사실은 단순히 받아들이고 활용하면 된다.



num = 1
if num != 0:
	print("num은 0이 아닙니다")


# 위의 코드를 단순화

num = 1
if num:
	print("num은 0이 아닙니다.")



bool(5)    # 정수 5는 True에요? False에요?

#  결괏값 : True

bool("Hwat")  # 문자열 "Hwat"은 True에요? False 에요?

#  결괏값 : True

bool("")  # 텅 빈 문자열은 True에요? False에요?


#  결괏값 : False

# 위의 함수 호출을 통해서 빈 문자열은 False, 비어 있지 않은 문자열은
#  True로 해석됨을 알 수 있다.


bool([1, 2, 3])    # list [1, 2, 3]은 True? 아님 False?

#  결괏값 : True

bool([])  # 빈 list는 True? or False?

#  결괏값 : False


# 문자열과 유사하게 빈 리스트는 False로, 비어 있지 않은 list는 True로
# 해석됨을 알 수 있다.







#  chapter 8. for loop 와 while loop   






# 1. for loop에 대한 remind

# for loop의 기본 뼈대 

# for <변수> in <번위>:
	# <for에 속하는 문장들>

# "하나 이상의 문장을 정해진 횟수만큼 반복해서 실행한다."

#  for_sum.py

def main():
	sum = 0
	for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
		sum = sum + i     # sum에 저장된 값을 i에 저장된 값만큼 증가시킴

	print("sum =", sum, end = ' ' )

main()

# end ='' 이 옵션의 경우 print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있습니다. 


# for_sum_range.py

def main():
	sum = 0
	for i in range (1, 11):   # 변수 i에 1부터 11 이전의 값까지 넣어가며 반복
		sum = sum + i

	print("sum =", sum, end =' ')

main()





# 2. True인 동안 반복하는 While loop (False가 될때 멈춘다.)

# While loop는 다음과 같이 생겼다.

# while <조건>:
	# <조건이 True인 경우 반복 실행할 문장들>

#while_basic.py

def main():
	cnt = 0
	while cnt < 3:    # cnt의 값이 3보다 작으면 반복
		print(cnt, end = '  ')
		cnt = cnt + 1    # cnt에 저장된 값을 1 증가


main()



# 3. for loop    vs.   while loop

# 공통점 : code의 반복 실행에 사용된다.
# 차이점 : for loop : 반복의 횟수를 지정, while loop는 반복의 조건을 지정

# 기본 form 

# for <변수> in <반복 범위>:
	# <for에 속하는 문장들>


# while <반복 조건>:
	# <조건이 True인 경우 반복 실행할 문장들>	 

# 대부분의 경우 for loop <-------> while loop 

# while_sum.py

def main():
	i = 1
	sum = 0   # 1부터 10까지의 합이 이 변수에 저장된다.
	while i < 11:   # i의 값이 11보다 작은 동안 반복
		sum = sum + i   # sum의 값을 i만큼 증가
		i = i + 1    # i의 값을 1 증가
	print("sum =", sum, end =' ')

main() 

# 어떨때 while loop로 작성하기에 적당할까?

# ex> "1부터 더해 나가다가 몇을 더했을때 처음으로 100을 넘기게 되는가?"
# 100을 넘길 때까지 덧셈을 계속해 나간다는 '반복 조건'이 있는 상황이므로 이 경우에는 while loop를 쓰는 것이 어울린다.


# while_over100.py

def main():
	i = 1
	sum = 0
	while sum <= 100:    # sum의 값이 100 이하인 경우에만 반복을 해라!
		sum = sum + i
		i = i + 1
	print(i-1, "더했을 때의 합", sum, end ='')

main()

def main():
	i = 1
	sum = 0
	while sum <= 10:    # sum의 값이 100 이하인 경우에만 반복을 해라!
		sum = sum + i
		i = i + 1
	print(i - 1, "더했을 때의 합", sum, end ='')
	# 0부터 시작해서 i - 1 해줌

main()



# 4. break 문

# 조건 : while loop나 for loop 안에서 사용해야 한다. break가 실행되면 이 명령문이 포함된 while loop나 for loop를 빠져나가게 된다.

# while_break.py

def main():
	i = 0
	while i < 100:
		print(i, end = ' ')
		i = i + 1
		if i == 20:
			break     # 이 문장이 속한 while loop를 빠져나간다.

main()


# 한 줄로 표현 :   if i == 20: break 


## while_over100.py와 비교

# while_over100_break.py

def main():
	i = 1
	sum = 0
	while True:
		sum = sum + i
		if sum > 100:    # sum > 100이면 아래의 break가 실행된다.
			print(i, "더했을 때의 합", sum, end = '  ')

			break
		i = i + 1

main()



# while True :
	# <조건이 True인 경우 반복 실행할 문장들>


# 이 경우 <반복 조건>이 항상 True이므로 이는 빠져나가지 못하는 구조의 while loop가 된다. 그리고
# 이러한 구조의 while loop를 가리켜 '무한 loop'라 한다. 물론 절대로 빠져 나가지 못하는 while loop를 만들면 이는 잘못이다.
# 그러나 예제에서는 다음 code를 while loop 안에 둠으로 인해서 빠져나갈 수 있는 길을 마련해 두었다.



# 5. continue 문


for i in range(1, 11):
	print(i, end = ' ')

# 여기서 짝수이면 출력을 건너뛴다.

# code 추가 
  # if i % 2 == 0:     # i가 짝수이면,
  	# continue           # for에 속한 문장들 중 나머지 부분 생략


for i in range(1, 11):
	if i % 2 == 0:
		continue

	print(i, end = '  ')    # 위의 continue가 실행되면 이 문장을 건너뛴다.

# 홀수가 출력된다.


u = 0
while u < 10:
	u = u + 1
	if u % 3 == 0: continue   # u가 3의 배수이면 다음 문장을 건너뛴다.
	print(u, end = '  ')


# 6. 이중 loop

#  for loop안에 또 for loop가 존재할때, 이를 가리켜 이중 for loop 라고 한다.


for i in [1, 2]:      # 바깥쪽 for loop
		for j in ['a', 'b' ,'c']:      # 안쪽 for loop
			print(j * i, end = '')


# 출력 결괏값 : a b c aa bb cc

# 분석

# 분석의 시작은 바깥쪽 for loop에서 시작한다. 바깥쪽 for loop에 의해서 그 안쪽에 위치한 for loop가 반복 실행되는 구조이다. 
# 즉, 변수 i가 1일때 다음의 형태로 안쪽 for loop가 실행이 된다. (그리고 a b c가 출력된다.)

# 그리고 이어서 변수 i가 2가 되어 다음 형태로 안쪽 for loop가 실행이 된다. (그래서 aa bb cc가 출력된다.)

# list안에 담겨 있는 문자열들 안에 문자 'r'이 몇번 등장하는지 세어보는 예제 (분석 철저히 할 필요가 있음)


sr = ['father', 'mother', 'brother']
cnt = 0
for s in sr:
		for c in s:
			if c == 'r':
					cnt += 1

print(cnt)


# 문제 :
# 1부터 10까지의 합을 구하라


