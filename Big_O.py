# 1. Доорх код ямар Big O вэ?
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])    
# HARIUU: O(1)


# 2. Нэг loop
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)
# Хариу: `O(n)`

 
#  3. List-ийн сүүлийн элементийг авах
# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])
# Хариу: `O(1)`


# 4. `n`-ийг ойлгох
# n = int(input("n: "))
# for i in range(n):
#     print(i)
# - Хэрэв `n = 10` бол loop хэдэн удаа ажиллах вэ? [10 udaa]
# - Хэрэв `n = 100` бол хэдэн удаа?  [100 udaa]
# - Тэгээд Big O-г ол.   O(n)


# Level 2 — `O(n)` vs `O(n²)`

# 5. Аль нь вэ?
# for i in range(n):
#     print(i)
# HARIUUU:   B. `O(n)`   
# 


# 6. Давхар loop
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# Big O  ni  O(n2)


# 7. Нийт хэдэн удаа `print()` ажиллах вэ?
# n = 5
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# gadna loop,dotor loop: tus bvr 5 udaa
# tgheer niit 25 udaa ajillanaaa


# 8. Нийт хэдэн удаа ажиллана? 
# n = 10`
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# tus bvr 10,10 tgheer 100 udaa ajillana.



# 9. Энэ `O(n)` үү, `O(n²)` үү? Энд давхар биш, хоёр **тусдаа** loop байгаа. 
# for i in range(n):
#     print(i)    hariuuu:  O(n)

# for j in range(n):
#     print(j)    hariuuu: O(n)



# 10. Дээрх код `n + n` удаа ажиллана.
#     Үүнийг Big O-оор яаж бичих вэ?
# hariuuu: O(n)


# 11. Аль санаа вэ?
# Доорх дарааллыг хараад ямар Big O-той холбоотойг ол.
# 1000
#  ↓
# 500
#  ↓
# 250
#  ↓
# 125
#  ↓
# 62
#  ↓
# 31
# HARIUUU:    C. `O(log n)`


# 12. Яагаад `1000 → 500 → 250 → 125` гэдэг нь `O(n)` биш `O(log n)`-тэй
#     холбоотой вэ?

# Uchir ni too alham burd 2 dahin bagasaj baina.
# Ene ni buh toog neg neg eer ni shalgahgui, harin alham burd tal 
# hesgiig ni hasaj baina gesen ug.
# Tiimees O(log n) gej uzne.



# 13.  Big O-г ол.  Nийт Big O хэд вэ?
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])
# for number in numbers:
#     print(number)
# HARIUUU: O(n)



# 14. Big O-г ол
# for i in range(n):
#     print(i)
# print("Hello")
# HARIUUU:  O(n)



# 15. Big O-г ол
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# print("Done")

# HARIUUU:     O(n²)
# Uchir ni:
# 1. Gadnah loop → O(n)
# 2. Dotood loop → O(n)
# 3. print("Done") → O(1)
