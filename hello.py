

# # 리스트 []


# # subway1=10
# # subway2=10
# # subway3=10
# # subway4=10
# subway=["유재석","조세호","박명수"]

# print(subway)


# subway.append("하하")
# subway.insert(1,"정형돈")


# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)


# subway.append("유재석")
# print(subway)

# print(subway.count("유재석 "))

# # num_list=[5,4,6,8,7,1]

# # num_list.sort()
# # print(num_list)
# # num_list.reverse()
# # print(num_list)

# # num_list.clear()
# # print(num_list)

# num_list=[5,4,6,8,7,1]
# mix=["조세호",20,True]
# num_list.extend(mix)
# print(num_list)

# 사전 {key1:value1, key2:value2}
# net={3:"유재석",100:"김태호"}

# print(net[3])
# print(net[100])

# print(net.get(5)) # None 출력
# print(net.get(5,"사용가능")) # 값이 없을 떄 None 을 출력하지만 사용가능 출력
# print("hi")
# print(net[5]) # 값이 없을 떄 프로그램 종료


# print(3 in net) # True
# print(5 in net) # False


# net2={"A-3": "유재석", "B-4":"조세호"}

# net2.clear()
# print(net2["A-3"])

# print(net2)
# net2["A-3"]="김종국"
# net2["B-4"]="김태호"
# print(net2)

# del net2["A-3"]
# print(net2)

# print(net2.keys())

# print(net2.values())

# print(net2.items())


# 튜플 (tuple)

# menu=("돈까스","치즈까스")  
# print(menu[0])
# print(menu[1])


# name="김종국"
# age=20
# hobby="코딩"
# print(name,age,hobby)

# (name,age,hobby)=("김종국",20,"코딩")
# print(name,age,hobby)


# 집합(set)
# 중복 안됨, 순서 없음

# my_set={1,2,33,3,3}
# print(my_set)

# java={"유재석","김태호","조세호"}
# python=set(["유재석","박명수"])

# # 교집합
# print(java&python)
# print(java.intersection(python))

# # 합집합
# print(java|python)
# print(java.union(python))

# # 차집합
# print(java-python)
# print(java.difference(python))

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)


# # set {} 대괄호
# menu={"커피","우유","주스"}   
# print(menu,type(menu))   


# # list [] 중괄호
# menu=list(menu)
# print(menu,type(menu))

# # tuple () 소괄호

# menu=tuple(menu)
# print(menu,type(menu))


# menu=set(menu)
# print(menu,type(menu))


from random import *

# list=[1,2,3,4,5]
# print(list)
# shuffle(list)

# print(list)

# print(sample(list,1))

# num_list=list(range(1,21)) # 1~20 까지 숫자 생성
# print(type(num_list))
# shuffle(num_list)

# win=sample(num_list,4)
# print(win)



# print("-"*3 ,"당첨자 발표","-"*3)
# print(f"치킨 당첨자 : {win[0]}")
# print(f"커피 당첨자 : {win[1:]}")
# print("-"*3 ,"축하합니다","-"*3)


# 문제 1
# 국어=80
# 영어=75
# 수학=55
# score=[80,75,55]
# print((국어+영어+수학)/3)

# 문제 2
# num=int(input("숫자를 입력해주세요 : "))
# if num%2 == 0 :
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")

# 문제 3
pin ="881120-1068234"

# yyyymmdd=pin[:6]
# num=pin[7:]
# print(yyyymmdd)
# print(num)

# 문제 4

# print(pin[7])

# 문제 5

# a="a:b:c:d"

# b=a.replace(":","#")
# print(b)

# 문제 6

# a=[1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)


# 문제 7 

# a=['Life','is','too','short']
# result=' '.join(a)
# print(result)


# 문제 8
# a=(1,2,3)
# a=(1,2,3,4)
# print(a)

# 문제 9
# a=dict()
# print(a)


# a['name']="py"
# print(a)
# a[('a',)]="py"
# print(a)
# a[[1]]="py"
# print(a)
# a[250]="py"
# print(a)

# 문제 10
# a={'A':90,'B':80 ,'C':70}
# result=a.pop("B")
# print(a)
# print(result)

# 문제 11
# a=[1,1,1,2,2,3,3,3,4,4,5]
# aSet=set(a)  # 리스트 -> 집합으로 변환 
# b=list(aSet) # 집합 -> 리스트로 변환
# print(b) # 리스트 출력

a=b=[1,2,3]
a[1]=4
print(b)