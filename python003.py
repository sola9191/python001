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

def plus(*args):
  result = 0
  for number in args:
    result+=number
  print(result)

plus(1,2,2,2,342,432,43,32,4)

#########################################
class Car(): # 설계도같은 개념
  wheels = 4
  doors = 4
  windows = 4
  seats = 4
  
  def start(self):
    print(self.color) # Red로 출력
    print("I started")
  # 모든 method의 첫번째 argument는 그 method를 호출한 instance

porche = Car() # Car의 instance
porche.color = "Red"

# method는 class안에있는 function임
porche.start() # errormessage
#파이썬은 모든 함수를 하나의 argument랑 함께 사용

####################################################################
class Car_2():

  def __init__(self, **kwargs): #kwargs는 dictionary 자료구조
    
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black") 
    # 값 받은게없으면 default 값 black으로 출력
    self.price = kwargs.get("price", "$20")
    # 값 받은게 없으면 default값 20
  # str ovveride
  def __str__(self):
    return f"Car with {self.wheels} wheels"

  



print(dir(Car_2)) # Car_2 class내부의 모든 properties 보여줌
## __str__ method가 호출되면 그 class의 instance를 출력

porche_2 = Car_2(color="green", price="$40")

print(porche_2.color, porche_2.price) 
# 파이썬이 자동으로 __str__ medthod 출력

mini = Car_2()
print(mini.color, mini.price) #default값 black $20 출력

# class에 method를 몇개 더 추가하고 싶을때 새 class를 만드는게 아니고 상속을 받거나 확장할수있음

class Convertible(Car_2): #Car_2를 extend한 class

  def __init__(self, **kwargs): #kwargs는 dictionary 자료구조
    super().__init__(**kwargs) # 부모클래스를 호출하는 function
    self.time = kwargs.get("time", 10)
  
  def take_off(self):
    return "taking off"
  
  # override
  def __str__(self):
    return f"Car with roof"

bmw = Convertible(color="white", price="$100")
print(bmw.take_off())
print(bmw.wheels)
print(bmw)
print(bmw.color) # __init__ method를 override (재정의) 했지만 super() function을 써서 부모클래스의 __init__를 가져왔기때문에 color 사용가능
