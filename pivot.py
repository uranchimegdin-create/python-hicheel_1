# 2026.10.28____WEDNESDAY:
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)

# arr = list(map(int,input("JAGSAALT UG: ").split()))
# print(quick_sort(arr))


# TASKSSSSS

# 1. n` ширхэг бүхэл тоо өгөгдөнө. Quick Sort ашиглан өсөх дарааллаар эрэмбэл.
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = []
#     mid = []
#     right = []
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right) 
# arr = list(map(int,input("JAGSAALTAA UG: ").split()))
# print(quick_sort(arr))



# 2. Quick Sort ашиглан тоонуудыг ихээс бага руу эрэмбэл.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i > pivot:
#             left.append(i)
#         elif i < pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# nums=list(map(int,input("JAGSAAALTAAAA?: ").split()))
# print(quick_sort(nums))


# 3. Массив дотор ижил тоонууд хэд хэд байж болно. Бүх элементийг өсөх дарааллаар эрэмбэл.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# nums=list(map(int,input("JAGSAAALTAAAA?: ").split()))
# print(quick_sort(nums))


# 4. Массив дотор сөрөг тоо, эерэг тоо болон `0` байна. Quick Sort ашиглан өсөх дарааллаар эрэмбэл.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# nums=list(map(int,input("JAGSAAALTAAAA?: ").split()))
# print(quick_sort(nums))


# 5.  Массивыг Quick Sort ашиглан өсөх дарааллаар эрэмбэлээд хамгийн бага
#     3 тоог хэвлэ. Массив дор хаяж 3 элементтэй.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#         a=quick_sort(left) + mid + quick_sort(right)
#     return a[0:3]
    

# nums=list(map(int,input("JAGSAAALTAAAA?: ").split()))
# print(quick_sort(nums))


# 6.  Quick Sort ашиглан эрэмбэлж, хамгийн их хоёр тоог
#     ихээс бага руу хэвлэ. Массив дор хаяж 2 элементтэй.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i > pivot:
#             left.append(i)
#         elif i < pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#         a= quick_sort(left) + mid + quick_sort(right)
#     return a[:2]
# nums=list(map(int,input("JAGSAAALTAAAA?: ").split()))
# print(quick_sort(nums))


# 7.  BURUUU SHUUU!!!
#     Оюутны нэр болон онооны хосууд өгөгдөнө. Quick Sort ашиглан 
#     оноогоор нь өсөх дарааллаар эрэмбэл.
# def quick_sort(name,score):
#     if len(name) <= 1:
#         return nums
#     pivot = score[len(score) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in score:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# n=int(input("HEDEN NER UGUH?: "))
# quick_sort=[]
# name=str(input("NER: "))
# score=int(input("ONOO: "))
# quick_sort.append(name,score)
# print(quick_sort(name,score))



# 7. BURUUU SHUUU!!!
# def quick_sort(**name):
#     if len(names) <= 1:
#         return nums
#     pivot = nums[len(name) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in name:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# n=int(input("HEDEN SURGC UGUH?: "))
# quick_sort=[]
# name=str(input("NER: "))
# score=int(input("ONOO: "))
# quick_sort.append(name,score)
# print(quick_sort)



# 7. 
# def quick_sort(student):
#     if len(student) <= 1:
#         return student
#     pivot = student[len(student) // 2][1]
#     left = []
#     right = []
#     mid = []
#     for i in student:
#         if i[1] < pivot:
#             left.append(i)
#         elif i[1] > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)

# n = int(input("HEDEN SURAGCH BNA?: "))
# students = []
# for i in range(n):
#     name, score = input().split(":")
#     students.append((name, int(score)))

# students = quick_sort(students)
# for student in students:
#     print(f"ONOOGOOR NI EREMBELEVEL: {student[0]}, {student[1]}")



# 8.  Үгсийн массивыг үгийн уртаар богиноос урт руу эрэмбэл. Энэ жишээнд ижил 
#     урттай үгсийн хоорондын дараалал чухал биш.
# def quick_sort(words):
#     if len(words) <= 1:
#         return words
#     pivot = len(words[len(words) // 2])
#     left = []
#     right = []
#     mid = []
#     for word in words:
#         if len(word) < pivot:
#             left.append(word)
#         elif len(word) > pivot:
#             right.append(word)
#         else:
#             mid.append(word)
#     return quick_sort(left) + mid + quick_sort(right)
# words=list(map(str,input("UGSEEE UG: ").split()))
# print(quick_sort(words))


# 9.   Массивыг Quick Sort ашиглан эрэмбэлээд медианыг ол.
#      - Элементийн тоо сондгой бол голын элементийг ав.
#      - Элементийн тоо тэгш бол голын хоёр элементийн дунджийг ол.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums)//2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# nums = list(map(int,input("TOONUUDAA UG: ").split()))
# nums = quick_sort(nums)
# n = len(nums)
# medium = []
# if n % 2 != 0:
#     median = nums[n//2]
# else:
#     median = (nums[n // 2 - 1] + nums[n // 2]) / 2
# print(f"EREMBELEGDSEN NI: {quick_sort(nums)}")
# print(f"MEDIAN NI: {median}")

        




# 10. Хоёр массивыг нэг массив болгон нэгтгээд Quick Sort ашиглан өсөх дарааллаар эрэмбэл.
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = []
#     right = []
#     mid = []
#     for i in nums:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             mid.append(i)
#     return quick_sort(left) + mid + quick_sort(right)
# b=list(map(int,input("EHNII JAGSAALT UG: ").split()))
# a=list(map(int,input("NEXT JAGSAALT UG: ").split()))
# c=b+a
# print(quick_sort(c))
