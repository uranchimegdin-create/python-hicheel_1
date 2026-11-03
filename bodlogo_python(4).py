# 1. *Даалгавар:** Тоон массивыг merge sort ашиглан багаас их рүү эрэмбэл.
#    **Функц:** `merge_sort(arr)` — эрэмбэлэгдсэн шинэ жагсаалт буцаана. Үүний 
#    тулд хоёр эрэмбэлэгдсэн жагсаалтыг нийлүүлдэг `merge(left, right)` функцийг бас бич.
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
# arr = list(map(int,input("TOONUUDAA UG: ").split()))
# print(merge_sort(arr))



# 2. Даалгавар:** Тоон массивыг merge sort ашиглан ихээс бага руу эрэмбэл.
#    Эхлээд өсөхөөр эрэмбэлээд дараа нь эргүүлж болохгүй, merge хэсгийг өөрчилж шийд.
#    **Функц:** `merge_sort_desc(arr)`
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def merge_sort_desc(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort_desc(arr[:mid])
#     right = merge_sort_desc(arr[mid:])
#     return merge(left, right)
# arr = list(map(int,input("TOONUUDAA UG: ").split()))
# print(merge_sort_desc(arr))



# 3. Даалгавар:** Ижил тоо хэд хэд орсон массивыг өсөхөөр эрэмбэл. 
#    Давхардсан тоонууд **алга болж болохгүй**, бүгд үлдэх ёстой.
#    **Функц:** `merge_sort(arr)`
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
# arr = list(map(int,input("TOONUUDAA UG: ").split()))
# print(merge_sort(arr))



# 4. *Даалгавар:** Сөрөг, эерэг тоо болон 0 холилдсон массивыг өсөхөөр эрэмбэл.
#    *Функц:** `merge_sort(arr)`
# def merge(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)
# arr = list(map(int,input("TOONUUD UG: ").split()))
# print(merge_sort(arr))



# 5. Массивын **тэгш тоонуудыг эхэнд нь** өсөхөөр,
#    **сондгой тоонуудыг араас нь** өсөхөөр байрлуул.
#    **Функц:** `even_odd_sort(arr)`
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def even_odd_sort(arr):
#     tegsh = []
#     sondgoi = []
#     for i in arr:
#         if i % 2 == 0:
#             tegsh.append(i)
#         else:
#             sondgoi.append(i)
#     return merge_sort(tegsh) + merge_sort(sondgoi)
# arr = list(map(int, input("TOONUUDAA UG: ").split()))
# print(even_odd_sort(arr))



# 6.  Аль хэдийн өсөхөөр эрэмбэлэгдсэн хоёр массив өгөгдөнө. Тэдгээрийг нэг
#     эрэмбэлэгдсэн массив болгож нэгтгэ. Хоёуланг нь залгаад дахин эрэмбэлж болохгүй, зөвхөн `merge` функцийг ашигла.
#     **Функц:** `merge(a, b)`
# def merge(a, b):
#     result = []
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1
#     return result + a[i:] + b[j:]
# a = list(map(int, input("ehnii jagsaalt: ").split()))
# b = list(map(int, input("next jagsaalt: ").split()))
# print(merge(a, b))



# 7.  Массивын хамгийн бага 3 тоог багаас их рүү буцаа. Массив дор 
#     хаяж 3 элементтэй гэж үзнэ. **Функц:** `smallest_three(arr)`
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def smallest_three(arr):
#     return merge_sort(arr)[:3]
# arr = list(map(int, input("JAGSAALT UG: ").split()))
# print(smallest_three(arr))



# 8. Merge sort ажиллах явцад:
#    **харьцуулалтын тоо** — merge хийх үед `left[i] <= right[j]` шалгалт 
#    нийт хэдэн удаа хийгдсэн,
#    **merge-ийн тоо** — `merge` функц нийт хэдэн удаа дуудагдсан
#    гэдгийг тоолж, эрэмбэлэгдсэн массивтай хамт хэвлэ. Массивыг `mid = len(arr) // 2`
#    гэж хуваана.
#    **Функц:** `merge_sort_count(arr)` — `(эрэмбэлэгдсэн_массив, харьцуулалт, merge_тоо)` 
#    буцаана.
# def merge_sort_count(arr):
#     if len(arr) <= 1:
#         return arr, 0, 0
#     mid = len(arr) // 2
#     left, c1, m1 = merge_sort_count(arr[:mid])
#     right, c2, m2 = merge_sort_count(arr[mid:])
#     result = []
#     i = j = 0
#     count = 0
#     while i < len(left) and j < len(right):
#         count += 1
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:] + right[j:]
#     return result, c1 + c2 + count, m1 + m2 + 1
# arr = list(map(int, input("JAGSAALT UG: ").split()))
# sorted_arr, comparison, merge_count = merge_sort_count(arr)
# print("Эрэмбэлэгдсэн:", sorted_arr)
# print("Харьцуулалт:", comparison)
# print("Merge-ийн тоо:", merge_count)



# 9.  Массивын хамгийн их 2 тоог ихээс бага руу буцаа. Массив дор 
#     хаяж 2 элементтэй гэж үзнэ.
#     **Функц:** `largest_two(arr)`
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def largest_two(arr):
#     return merge_sort(arr)[-2:][::-1]
# arr = list(map(int, input("JAGSAALT UG: ").split()))
# print(largest_two(arr))



# 10.  Нэрсийн жагсаалтыг цагаан толгойн дарааллаар эрэмбэл.
#      Бүх нэр том үсгээр эхэлнэ.
#      **Функц:** `merge_sort(names)`
# def merge_sort(names):
#     if len(names) <= 1:
#         return names
#     mid = len(names) // 2
#     left = merge_sort(names[:mid])
#     right = merge_sort(names[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# names = input("NERSEE ORUUL: ").split()
# print(merge_sort(names))



# 11. Сурагч бүр `(нэр, оноо)` хэлбэрийн tuple-ээр өгөгдөнө. Сурагчдыг:
#     1. **оноогоор ихээс бага руу**,
#     2. оноо **тэнцүү** бол **нэрээр цагаан толгойн дарааллаар** эрэмбэл.
#     **Функц:** `sort_students(students)`
# def merge_sort(students):
#     if len(students) <= 1:
#         return students
#     mid = len(students) // 2
#     left = merge_sort(students[:mid])
#     right = merge_sort(students[mid:])
#     result = []
#     while left and right:
#         if left[0][1] > right[0][1] or (left[0][1] == right[0][1] and left[0][0] < right[0][0]):
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def sort_students(students):
#     return merge_sort(students)
# n = int(input("HEDEN SURAGCH UGUH?: "))
# students = []
# for i in range(n):
#     name, score = input("NER BA ONOO: ").split()
#     students.append((name, int(score)))
# print(sort_students(students))



# 12.  Үгсийг **богиноос урт руу** эрэмбэл. Ижил урттай үгс байвал 
#      **цагаан толгойн дарааллаар** байрлуул.
#      **Функц:** `sort_words(words)`
# def merge_sort(words):
#     if len(words) <= 1:
#         return words
#     mid = len(words) // 2
#     left = merge_sort(words[:mid])
#     right = merge_sort(words[mid:])
#     result = []
#     while left and right:
#         if len(left[0]) < len(right[0]) or (len(left[0]) == len(right[0]) and left[0] <= right[0]):
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def sort_words(words):
#     return merge_sort(words)
# words = input("UGSEE UG: ").split()
# print(sort_words(words))



# 13. Эрэмбэлэгдээгүй массивыг эхлээд merge sort-оор эрэмбэл. Дараа нь 
#     binary search ашиглан өгөгдсөн тоог хай. Олдвол **эрэмбэлэгдсэн массив дахь 
#     индексийг**, олдохгүй бол `-1` буцаа.
#     **Функц:** `binary_search(arr, target)`
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def binary_search(arr, target):
#     arr = merge_sort(arr)
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# arr = list(map(int, input("JAGSAALT UG: ").split()))
# target = int(input("HAIH TOO ORUUL: "))
# print(binary_search(arr, target))



# 14. Хоёр үг өгөгдөнө. Хоёр үг ижил үсгүүдээс бүтсэн (зөвхөн дараалал нь өөр)
#     бол `True`, үгүй бол `False` буцаа. Үг бүрийн үсгүүдийг 
#     merge sort-оор эрэмбэлээд харьцуул.
#     **Функц:** `is_anagram(word1, word2)`
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def is_anagram(word1, word2):
#     return merge_sort(list(word1)) == merge_sort(list(word2))
# word1 = input("EHNII UG: ")
# word2 = input("NEXT UG: ")
# print(is_anagram(word1, word2))


# 15. Массивыг merge sort-оор эрэмбэлээд, хоорондын 
#     **зөрүү нь хамгийн бага** хоёр тоог ол. Хэд хэдэн хос ижил зөрүүтэй
#     бол **хамгийн эхэнд** байгаа хосыг буцаа. Массив дор хаяж 2 элементтэй гэж үзнэ.
#     **Функц:** `closest_pair(arr)` — `((тоо1, тоо2), зөрүү)` буцаана.
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right
# def closest_pair(arr):
#     arr = merge_sort(arr)
#     pair = (arr[0], arr[1])
#     diff = arr[1] - arr[0]
#     for i in range(1, len(arr) - 1):
#         d = arr[i + 1] - arr[i]
#         if d < diff:
#             diff = d
#             pair = (arr[i], arr[i + 1])
#     return pair, diff
# arr = list(map(int, input("jagsaalt ug: ").split()))
# print(closest_pair(arr))
