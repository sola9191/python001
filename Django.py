# 3.0 ~
# Django --> framework
# Pinterest, Instagram 장고로 만들어짐

# arguments / keyword arguemtents
# 객체지향 프로그래밍

# 두가지 타입의 arguments가 있음
- positional arguement
- keyword argument

def plus(a, b, *args, **kwargs):
  print(args) # tuple type으로 출력
  print(kwargs) # dictionary type으로 출력
  return a+b

print(111,1,1,1,1,1,1) # print함수는 여러파라미터 받기가능
plus(10,5,1,1,1,1,1,1,3) 
# *args의 의미: positional argument가 엄청 많이 있다
plus(1,2, hello=True, fds=False)
# *kwargs의 의미: keyword argument가 엄청 많이 있다