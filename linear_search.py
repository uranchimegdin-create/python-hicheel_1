# 1.  Linear Search ашиглан **хамгийн эхний сондгой** тооны index-ийг ол.
# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] % 2 != 0:
#             return i
#     return -1
# nums = [2, 4, 6, 9, 7, 5]
# result = linear_search(nums)
# if result != -1:
#     print("Index:", result)
# else:
#     print("Sondgoi too oldsongui")
    


# 2. Linear Search ашиглан `10`-аас их тоо байгаа эсэхийг шалга.
# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] > 10:
#             return oldloo
#     return oldsongui
# nums = list(map(int,input("TOONUUDAA UG: ").split()))
# result = linear_search(nums)
# print(result)



# 3. Linear Search ашиглан `0`-ийн index-ийг ол.
# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             return i
#     return -1
# nums = list(map(int,input("TOO UG: ").split()))
# result = linear_search(nums)
# if result != -1:
#     print("Index:", result)
# else:
#     print("0 oldsongui")



# 4. 5`-аас их **хамгийн эхний** тоог Linear Search ашиглан ол.
# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] > 5:
#             return arr[i]
#     return -1
# nums = list(map(int,input("TOO UG: ").split()))
# result = linear_search(nums)
# if result != -1:
#     print("Number:", result)
# else:
#     print("Oldsongui")



# 5. Linear Search ашиглан сөрөг тоонуудын **тоог** ол.
# def linear_search(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             count += 1
#     return count
# nums = list(map(int,input("TOO UG: ").split()))
# result = linear_search(nums)
# print("SOROG TOONUUD:", result)



# 6. Хэрэглэгчээс `target` тоо ав.
# `target`-оос бага байгаа **хамгийн эхний** тоог Linear Search ашиглан ол.
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] < target:
#             return arr[i]
#     return -1
# nums = list(map(int,input("TOO UG: ").split()))
# target = int(input("Target: "))
# result = linear_search(nums, target)
# if result != -1:
#     print("Number:", result)
# else:
#     print("Oldsongui")



# 7. Linear Search ашиглан хамгийн эхний **тэгш** тоог ол.
# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             return arr[i]
#     return 1
# nums = list(map(int,input("TOO UG: ").split()))
# result = linear_search(nums)
# if result != -1:
#     print("TEGSH TOO:", result)
# else:
#     print("TEGSH TOO OLDSONGUI")



# 8. Linear Search ашиглан:
#    `15`-аас их **бөгөөд** сондгой байгаа хамгийн эхний элементийн **index**-ийг ол.
# def linear_search(arr):
#     for i in range(len(arr)):
#         if arr[i] > 15 and arr[i] % 2 != 0:
#             return i
#     return -1
# nums = list(map(int,input("TOO UG: ").split()))
# result = linear_search(nums)
# if result != -1:
#     print("Index:", result)
# else:
#     print("Oldsongui")



# 9. Linear Search ашиглан **80-аас дээш** оноотой хамгийн эхний сурагчийн нэрийг ол.
# def linear_search(students):
#     for i in range(len(students)):
#         if students[i][1] > 80:
#             return students[i][0]
#     return "Oldsongui"
# students = [
#     ("Bat", 75),
#     ("Anu", 85),
#     ("Saraa", 95),
#     ("Bold", 70)
# ]
# result = linear_search(students)
# print("Student:", result)



# 10. Linear Search ашиглан **хамгийн сүүлийн** сондгой тооны index-ийг ол.
# def linear_search(arr):
#     result = -1
#     for i in range(len(arr)):
#         if arr[i] % 2 != 0:
#             result = i
#     return result
# nums = list(map(int,input("TOO UG: ").split()))
# result = linear_search(nums)
# if result != -1:
#     print("Index:", result)
# else:
#     print("Sondgoi too oldsongui")



# 11.  Хэрэглэгчээс тоо ав.
#      Тэр тоо list-д байгаа **бүх index**-ийг олж хэвлэ.
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             print(i)
# nums = list(map(int,input("TOONUUDAA UG: ").split()))
# target = int(input("Target: "))
# linear_search(nums, target)



# 12.  Хэрэглэгчээс нэр ав.
#      Linear Search ашиглан сурагчийг хайж:
#      - оноо `60`-аас дээш бол → `"Тэнцсэн"`
#      - `60`-аас бага бол → `"Тэнцээгүй"`
#      - нэр байхгүй бол → `"Олдсонгүй"`
#      гэж хэвлэ.

# def linear_search(students, target):
#     for i in range(len(students)):
#         if students[i][0] == target:
#             if students[i][1] > 60:
#                 print("Tentsen")
#             else:
#                 print("Tentseegui")
#             return
#     print("Oldsongui")
# students = []
# n = int(input("Heden suragch baina?: "))
# for i in range(n):
#     name = input("Name: ")
#     score = int(input("Score: "))
#     students.append([name, score])
# target = input("Haij bui suragchiin ner: ")
# linear_search(students, target)



