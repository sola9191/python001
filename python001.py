a_string ="like this" 
b_string = "False"
a_number = 3
a_float = 3.12
a_boolen = False
a_none = None
print(type(a_none))
# 주석은 샵을 사용한다 

# Sequence Type
# list
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days)
print(type(days)) #list
print(days)

# https://docs.python.org/3/library/
# python이 어떻게 동작하는지 알수있음

print("Mon" in days) #True
print(days[0]) #Mon
print(len(days)) #5
days.append("Sat")
print(days) # Sat추가됨
days.reverse()
print(days) # 제일 마지막게 첫번째로옴

#tuple
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(type(days)) #tuple
# list랑 같지만 변경이 불가능함

nico = {
  "name" : "Nico",
  "age" : 29,
  "korean" : True,
  "fav_food" : ["Kimchi", "Sashimi"]
}

print(nico["age"]) #29
nico["fav_color"] = "Blue"
print(nico)

#형변환
age  = "18"
print(type(age)) # str
n_age = int(age)
print(type(n_age)) #int

원준="배고파"
print(원준)

nico = {
  "tulpe" : (1,2,3)
  age : 44


}
print(nico["tulpe"])