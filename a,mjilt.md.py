# 1. Хоёр дахь хамгийн их тоо. Давхардсан утгыг нэг утга гэж үзээд 2 дахь хамгийн их тоог ол.
# nums = list(map(int,input().split()))
# nums=list(set(nums))
# nums.sort()
# print(nums[-2])


# 2.Хоёр дахь хамгийн бага тоо.List дотроос 2 дахь хамгийн бага ялгаатай тоог ол.
# too=list(map(int,input().split()))
# too=list(set(too))
# too.sort()
# print(too[1])


# 3.Хамгийн урт дараалсан сондгой хэсэг.List дотор дараалсан сондгой тоонуудын хамгийн урт хэсгийн уртыг ол.
# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]
# count=0
# ist=[]
# for i in range(0,len(nums)-1):
#     if i % 2 !=0:
#         count+=1
#     elif 






# 4.Хамгийн урт өсөх дараалал.Зөвхөн зэрэгцээ элементүүд өсөж байгаа хэсгээс хамгийн уртыг ол.
# too=[1, 2, 4, 2, 3, 5, 7, 9]
# count = 0
# lst = []
# for i in range(0,len(too)-1):
#     if too[i] < too[i+1]:
#         count += 1
#     else:
#         lst.append(count)
#         count=0
# count=0
# lst.append(count)
# print(lst)
# print(max(lst))



# # 5. List дотор хамгийн олон удаа орсон тоог ол.Хэрэв ижил давтамжтай хэд хэдэн тоо байвал хамгийн бага тоог сонго.
# a=[2,3,4,3,5,6,5,5,8]
# max_count=0
# davtalt=0
# for i in a:
#     if a.count(i)>max_count:
#         max_count=a.count(i)
#         davtalt=i
# print(davtalt)




# 6.






# 7.Хоёр list өгөгдөнө. Аль алинд нь байгаа элементүүдийг шинэ list-д оруул. Давхардахгүй байх ёстой.
# a = {1, 2, 3, 4, 5}
# b = {3, 5, 7, 8, 1}
# print(a & b)


# 8. List доторх хоёр өөр байрлалтай элементүүдээс нийлбэр нь хамгийн их байх хосыг ол.
# a=[4, 7, 2, 9, 5]
# a.sort()
# print(a[-2],end=" ",a[-1])


# 9.Нийлбэр нь target.List болон target өгөгдөнө.Нийлбэр нь target болох хоёр элементийн index-ийг ол.
# nums = [4, 8, 2, 7, 5]
# target = 9





# 10. List доторх хоёр өөр тооны абсолют зөрүү хамгийн бага байх хосыг ол.
# a=[2,15,20,18,14,33]
# a.sort()



# 11.List-ийн сүүлийн элементийг эхэнд нь аваач.insert(), slicing ашиглахгүй.
# number=[1,2,3,4,5]
# new_list = [number[-1]]
# for i in range(len(number) - 1):
#     new_list.append(number[i])
# print(new_list)


# 12.List-ийг баруун тийш K удаа rotate хий.
# nums = [1,2,3,4,5]
# k = 2
# for i in range(k):
#     last=nums.pop()
#     nums.insert(0,last)
# print(nums)


# 13.  List доторх бүх 0-ийг төгсгөлд аваач. Бусад элементүүдийн дараалал өөрчлөгдөхгүй.
# numbers = list(map(int,input("TOONUUDAA UG: ").split()))
# result = []
# for i in numbers:
#     if i != 0:
#         result.append(i)
# for i in numbers:
#     if i == 0:
#         result.append(i)
# print(result)


# 14. List-ийн давхардсан элементүүдийг устгаад, анхны дарааллыг хадгал.
# nums = list(map(int,input("JAGSAALT UG: ").split()))
# result = []
# for i in nums:
#     if i not in result:
#         result.append(i)
# print(result)


# 15.  1-ээс N хүртэлх бүх тооноос нэг тоо дутуу list өгөгдөнө. Дутуу тоог ол.
# numbers = list(map(int, input("Too nuudaa oruul: ").split()))
# n = len(numbers) + 1
# total = n * (n + 1) // 2
# dutuu_too = total - sum(numbers)
# print("Dutuu too:", dutuu_too)


# 16.  Нэг удаа л байгаа тоо List дотор зөвхөн нэг удаа орсон 
#      цорын ганц тоог ол Бусад бүх тоо яг 2 удаа орсон байна.
# numbers = list(map(int, input("Toonuudaa ug: ").split()))
# for i in numbers:
#     if numbers.count(i) == 1:
#         print("Davtagdaagui too:", i)
#         break


# 17. Хөршүүдийн хамгийн их нийлбэр Зэрэгцээ хоёр элементийн нийлбэрүүдээс
#     хамгийн ихийг ол.Гэхдээ хамгийн их нийлбэр өгч байгаа index-үүдийг бас хэвлэ.
# numbers = list(map(int, input("Too nuudaa oruul: ").split()))
# max_sum = numbers[0] + numbers[1]
# max_index = 0
# for i in range(len(numbers) - 1):
#     total = numbers[i] + numbers[i + 1]
#     if total > max_sum:
#         max_sum = total
#         max_index = i
# print("Hamgiin ih niilber:", max_sum)
# print("Index:", max_index, max_index + 1)



# 18. List-ийн тухайн элемент өөрийн зүүн болон баруун хөршөөсөө хоёулангаас нь их 
#     байвал local maximum гэж үзнэ.Бүх local maximum-уудыг хэвлэ.
# numbers = list(map(int, input("Too nuudaa oruul: ").split()))
# for i in range(1, len(numbers) - 1):
#     if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
#         print(numbers[i])


# 19. Элемент өөрийн хоёр хөршөөсөө хоёулангаас нь бага байвал
#     valley гэж үзнэ.Бүх valley элементүүдийг ол.
# numbers = list(map(int, input("Too nuudaa oruul: ").split()))
# for i in range(1, len(numbers) - 1):
#     if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
#         print(numbers[i])


# 20.  List дотор хэдэн local maximum байгааг ол.
# count = 0
# numbers = list(map(int, input("Too nuudaa oruul: ").split()))
# for i in range(1, len(numbers) - 1):
#     if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
#         count += 1
# print(count)


# 21. Тоон пирамид...N өгөгдөнө.
# n = int(input("N = "))
# for i in range(1, n + 1):
#     print(str(i) * i)


# 22.  Урвуу пирамид
# n = int(input("N = "))
# for i in range(n, 0 , -1):
#     print(str(i) * i)


# 23. Floyd Triangle
# n = int(input("N = "))
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()


# 24.  Prime pair.N өгөгдөнө.1–N дотор нийлбэр нь N болох бүх
#      хоёр prime тооны хосыг ол.
# I CANNN'TTTTTTTTTTTTTT


