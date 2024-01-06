# weather=input("오늘 날씨는 어때요? ") # input은 기본적으로는 str 변수를 담고 있다.

# if weather=="비" or "눈":
#     print("우산을 챙기세요")
# elif weather=="미세먼지":
#     print("마스크 챙기세요")
# else : 
#     print("준비물 필요없어요")   

# temp=int(input("기온은 어때요?"))
# if 30<=temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10<= temp and temp<30 :
#     print("괜찮은 날씨에요")
# elif 0<=temp and temp <10 :
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지 마세요")

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for num in range(1,5):
#     print(f"대기번호 : {num}")

# st=["아이언맨","토르","그루트"]
# for cof in st :
#     print(f"{cof}님 커피가 준비되었습니다.")

# customer="토르"
# index=5
# while index>=1:
#     print(f"{customer}, 커피가 준비되었습니다.{index}번 남았어요")
#     index -= 1
#     if index == 0 :
#         print("커피가 다 나왔어요")

# customer="아이언맨"
# index=1
# while True :
#     print(f"{customer} 님 커피가 준비 되었습니다. {index}번 ")
#     index+=1
#     if index==10:
#         print("커피가 다 나왔어요")
#         break

# customer="토르"
# person="unknown"
# while person!=customer :
#     print(f"{customer}, 커피가 준비 되었습니다.")
#     person=input("이름이 어떻게 되세요?")


# absent=[2,5]
# no_book=7
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student==no_book:
#         print(f"오늘 수업 여기까지 {no_book} 교무실로 따라와")
#         break
#     print(f"{student}, 책을 읽어봐")

# num=[1,2,3,4,5]
# print(num)
# num=[i+100 for i in num]
# print(num)

# students=["아이언맨","토르","그루트"]
# students=[len(i) for i in students]
# print(students)

# students=["iron man","thor","groot"]
# students=[i.upper() for i in students]
# print(students)

from random import *
count=0
person=1
while person<=50:
    num=randrange(5,51)
    if 5<=num<=15 :
     print(f"[O] {person}번째 손님 (소요시간 : {num})")
     count+=1
    else :
     print(f"[ ] {person}번째 손님 (소요시간 : {num})")
    person+=1


print(f"총 탑승 승객 {count} 분")

cnt=0
for i in range(1,51):
  random=randrange(5,51)
  if 5<=random<=15:
   print(f"[O] {i}번째 손님 (소요시간 : {random}분)")
   cnt+=1
  else :
   print(f"[ ] {i}번째 손님 (소요시간 : {random}분)")

print(f"총 탑승 승객 : {cnt} 분")