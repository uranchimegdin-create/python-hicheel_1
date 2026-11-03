# 1.   Бүхэл тоо уншаад эерэг/сөрөг, тэгш/сондгой 
#      эсэхийг хэвлэ. 0 бол Тэг гэж хэвлэ.
# num = int(input("SHALGAH TOO ORUUL: "))
# if num == 0:
#     print("Тэг")
# else:
#     if num > 0:
#         print("Эерэг")
#     else:
#         print("Сөрөг")
#     if num % 2 == 0:
#         print("Тэгш")
#     else:
#         print("Сондгой")


# 2. 
# score = int(input("SHALGAH ONOO ORUUL: "))
# if score < 0 or score > 100:
#     print("Буруу оноо")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# 3.  Он уншаад өндөр жил мөн эсэхийг хэвлэ. Он 4-т хуваагддаг
#     ба 100-д хуваагддаггүй бол, эсвэл 400-д хуваагддаг бол өндөр жил.
# year = int(input("On oruulna uu: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Undur jil")
# else:
#     print("Undur jil bish")



# 4.  Гурвалжны 3 талын уртыг уншина. Аль нэг хоёр талын нийлбэр гурав дахь 
#     талаасаа их биш бол Гурвалжин үүсэхгүй. Үгүй бол 
#     Тэгш талт, Адил хажуут эсвэл Энгийн гэж хэвлэ.
# a = int(input("A TAL UG: "))
# b = int(input("B TAL UG: "))
# c = int(input("C TAL UG: "))
# if a + b <= c or a + c <= b or b + c <= a:
#     print("Gurvaljin uusgehgui")
# elif a == b == c:
#     print("Tegsh talt")
# elif a == b or a == c or b == c:
#     print("Adil hajuut")
# else:
#     print("Engiin")


# 5. 
# km = int(input())
# hour = int(input())
# if km <= 2:
#     price = 3000
# else:
#     price = 3000 + (km - 2) * 1500
# if hour >= 22 or hour <= 5:
#     price += 2000
# print(price)



# 6. 
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total += i
# print(total)



# 7. Эерэг бүхэл тоо уншаад цифрүүдийнх нь
#    нийлбэрийг while давталтаар ол. str() ашиглахгүй.
# n = int(input("BUHEL TOO ORUUL: "))
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print(total)



# 8. Эерэг бүхэл тоог while давталтаар урвуулж хэвлэ. str() ашиглахгүй.
# n = int(input("TOO ORUUL: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print(reverse)


# 9.  1-ээс n хүртэлх тоог нэг мөрөнд зайгаар тусгаарлаж хэвлэ.
#     3-т хуваагдвал тооны оронд Физ, 5-д хуваагдвал Базз,
#     хоёуланд нь хуваагдвал ФизБазз гэж хэвлэ.
# n = int(input("HED HVRTEL YBAH VE?: "))
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizBuzz", end=" ")
#     elif i % 3 == 0:
#         print("Fiz", end=" ")
#     elif i % 5 == 0:
#         print("Buzz", end=" ")
#     else:
#         print(i, end=" ")


# 10. Програмдаа secret = 37 гэж нууц тоо хадгал. Хэрэглэгч
#     зөв таах хүртэл тоо уншиж,Их байна эсвэл
#     Бага байна гэж хэвлэ. Зөв таавал хэдэн оролдлогоор таасныг хэвлэ.
# secret = 37
# count = 0
# while count < 5:
#     n = int(input("TAAH TOO ORUUL: "))
#     count += 1
#     if n > secret:
#         print("Ih baina")
#     elif n < secret:
#         print("Baga baina")
#     else:
#         print(f"ZOW BNA,{count} OROLDLOGOOR TAALAA.")
#         break
# if count == 5 and n != secret:
#     print(f"{count} OROLDLOGO DUUSLAA,Yalagdsan!")


# 11. n уншаад n × n хэмжээтэй 
#     үржүүлэх хүснэгтийг хэвлэ. Тоонуудыг зайгаар тусгаарла.
# n = int(input("toogoo ug: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i * j, end=" ")
#     print()


# 12. n мөртэй пирамид хэвлэ. i-р мөрөнд 
#     эхлээд n − i зай, дараа нь 2i − 1 од байна.
# n = int(input("HEDEN MUR BAIH?: "))
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))



# 13. Нийлбэр нь target болох бүх хосыг (arr[i], arr[j]) 
#     tuple хэлбэрээр, i < j байхаар, олдсон дарааллаар нь буцаа.
#     Функц: find_pairs(arr, target)
#     Оролт:  arr = [2, 7, 4, 5, 1], target = 6
# def find_pairs(arr, target):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 pairs.append((arr[i], arr[j]))
#     return pairs
# arr = list(map(int, input("LISTEE UG: ").split()))
# target = int(input("HAIH TOO UG: "))
# print(find_pairs(arr, target))


# 14.  Хамгийн олон давтагдсан тоо болон давтамжийг 
#      (тоо, давтамж) хэлбэрээр буцаа. Давтамж тэнцүү бол жагсаалтад
#      түрүүлж орсныг нь сонго. dict ашиглахгүй, давхар давталтаар шийд.
# def most_frequent(arr):
#     max_count = 0
#     result = 0
#     for i in range(len(arr)):
#         count = 0
#         for j in range(len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count > max_count:
#             max_count = count
#             result = arr[i]
#     return (result, max_count)
# arr = list(map(int, input("LISTEE UG: ").split()))
# print(most_frequent(arr))


# 15.  2 хэмжээст жагсаалтын мөр бүрийн болон багана бүрийн
#      нийлбэрийг (мөрүүд, баганууд) хэлбэрээр буцаа.
# def row_col_sums(matrix):
#     rows = []
#     cols = []
#     for i in range(len(matrix)):
#         total = 0
#         for j in range(len(matrix[i])):
#             total += matrix[i][j]
#         rows.append(total)
#     for j in range(len(matrix[0])):
#         total = 0
#         for i in range(len(matrix)):
#             total += matrix[i][j]
#         cols.append(total)
#     return (rows, cols)
# matrix = []
# n = int(input("HEDEN MUR BAIH?: "))
# for i in range(n):
#     row = list(map(int, input("LISTEE UG: ").split()))
#     matrix.append(row)
# print(row_col_sums(matrix))



# 16. Давхардсан элементүүдийг хасаад, үлдсэнийг анх орсон дарааллаар нь буцаа.
#     Аль хэдийн харсан элементээ set-д хадгал.
# def remove_duplicates(arr):
#     result = []
#     seen = set()
#     for i in arr:
#         if i not in seen:
#             result.append(i)
#             seen.add(i)
#     return result
# arr = list(map(int, input("LISTEE UG: ").split()))
# print(remove_duplicates(arr))



# 17. Өгүүлбэр дэх үг бүр хэдэн удаа орсныг dict хэлбэрээр буцаа.
# def word_count(text):
#     words = text.split()
#     result = {}
#     for word in words:
#         if word in result:
#             result[word] += 1
#         else:
#             result[word] = 1
#     return result
# text = str(input("JIMSNUUDEE ORUUL: "))
# print(word_count(text))


# 18.  нэр → оноонуудын жагсаалт хэлбэрийн dict өгөгдөнө.
#      Сурагч бүрийн дундаж оноотой dict болон хамгийн өндөр 
#      дундажтай сурагчийн нэрийг буцаа.
# def averages(grades):
#     avg = {}
#     max_avg = 0
#     best_student = ""
#     for name in grades:
#         total = sum(grades[name])
#         average = total / len(grades[name])
#         avg[name] = average
#         if average > max_avg:
#             max_avg = average
#             best_student = name
#     return avg, best_student
# grades = {
#     "Anar": [80, 90, 70],
#     "Bold": [60, 75, 90],
#     "Saraa": [95, 85, 90]
# }
# print(averages(grades))



# 19.  Хоёр дугуйлангийн гишүүд set-ээр өгөгдсөн. Хоёуланд нь 
#      явдаг, зөвхөн Python-д явдаг, зөвхөн математикт
#      явдаг сурагчид болон нийт сурагчийн тоог хэвлэ.
# python = {"Anar", "Bold", "Saraa", "Dorj"}
# math = {"Bold", "Gerel", "Dorj"}
# both = python & math
# only_python = python - math
# only_math = math - python
# total = python | math
# print("Hoyuland ni yavdag:", both)
# print("Zuvhun Python:", only_python)
# print("Zuvhun Math:", only_math)
# print("Niit suragch:", len(total))



# 20. (x, y) tuple-уудын жагсаалтаас (0, 0) цэгээс хамгийн хол 
#     байгаа цэг болон түүний x² + y² утгыг буцаа.
# def farthest_point(points):
#     max_distance = -1
#     farthest = None
#     for point in points:
#         x, y = point
#         distance = x**2 + y**2
#         if distance > max_distance:
#             max_distance = distance
#             farthest = point
#     return farthest, max_distance
# n = int(input("Heden tseg ve?: "))
# points = []
# for i in range(n):
#     x, y = map(int, input("tseguud ug: ").split())
#     points.append((x, y))
# print(farthest_point(points))



# 21.  Хоёр функц бич.is_prime(n) нь n анхны тоо бол True буцаана. 
#      primes_up_to(n) нь 2-оос n хүртэлх анхны тоонуудыг 
#      is_prime-ийг дуудаж олно.
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# def primes_up_to(n):
#     result = []
#     for i in range(2, n + 1):
#         if is_prime(i):
#             result.append(i)
#     return result
# num = int(input("Too oruulna uu: "))
# print("Anhnii too esehiig shalgah:", is_prime(num))
# print("Anhnii toonuud:", primes_up_to(num))



# 22.  Шугаман хайлтаар x тооны жагсаалт дахь бүх индексийг буцаа.
#      Олдохгүй бол хоосон жагсаалт.
# def find_all(arr, x):
#     result = []
#     for i in range(len(arr)):
#         if arr[i] == x:
#             result.append(i)
#     return result
# arr = list(map(int, input("Toonuudaa oruulna uu: ").split()))
# x = int(input("Haiх toogoo oruulna uu: "))
# print(find_all(arr, x))



# 23. Утасны дэвтэр (нэр, дугаар) tuple-уудын жагсаалтаар өгөгдөнө.
#     Нэрээр нь шугаман хайлт хийж дугаарыг буцаа. Олдохгүй бол "Олдсонгүй".
# def find_phone(book, name):
#     for person in book:
#         n, phone = person
#         if n == name:
#             return phone
#     return "Oldsongui"
# book = [
#     ("Anar", "99112233"),
#     ("Bold", "88001122"),
#     ("Saraa", "95553344")
# ]
# name = input("Neree oruulna uu: ")
# print(find_phone(book, name))



# 24.  Эрэмбэлэгдсэн жагсаалтаас x-ийг binary search-ээр хайж,
#      (индекс, алхмын тоо) буцаа. mid-ийг шалгах бүр нэг алхам. 
#      Олдохгүй бол индекс нь -1. mid = (low + high) // 2 ашигла.
# def bs_steps(arr, x):
#     low = 0
#     high = len(arr) - 1
#     steps = 0
#     while low <= high:
#         mid = (low + high) // 2
#         steps += 1
#         if arr[mid] == x:
#             return mid, steps
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1, steps
# arr = list(map(int, input("Eremblegdsen toonuudaa oruul: ").split()))
# x = int(input("Haikh toogoo oruul: "))
# print(bs_steps(arr, x))



# 25. Эрэмбэлэгдсэн, давхардалгүй жагсаалтад x байвал түүний индексийг буцаа.
#     Байхгүй бол эрэмбийг эвдэхгүйгээр x-ийг оруулах 
#     индексийг буцаа. Binary search ашигла.
# def search_insert(arr, x):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low
# arr = list(map(int, input("Toonuudaa oruul: ").split()))
# x = int(input("Haikh too: "))
# print(search_insert(arr, x))



# 26. Хөрш хоёр элементийг харьцуулж, буруу дараалалтай 
#     бол солих алхмыг жагсаалт эрэмбэлэгдэх хүртэл давт.
#     (эрэмбэлсэн жагсаалт, солилтын тоо) буцаа.
# def bubble_sort(arr):
#     arr = arr.copy()
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 count += 1
#                 swapped = True
#         if swapped == False:
#             break
#     return arr, count
# arr = list(map(int, input("Toonuudaa oruul: ").split()))
# print(bubble_sort(arr))



# 27. Алхам бүрт эрэмбэлэгдээгүй хэсгийн хамгийн бага элементийг олж,
#     тэр хэсгийн эхний элементтэй нь соль. Алхам бүрийн дараах жагсаалтыг хэвлэ. 
# def selection_sort(arr):
#     arr = arr.copy()
#     n = len(arr)
#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         print(i + 1, "-r alham:", arr)
#     return arr
# arr = list(map(int, input("Toonuudaa oruul: ").split()))
# selection_sort(arr)



# 28. Эрэмбэлээд давхардлыг арилгах
#     Даалгавар: Жагсаалтыг merge sort-оор эрэмбэлээд давхардсан 
#     тоонуудыг хас. set ашиглахгүй.
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
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
# def sort_unique(arr):
#     sorted_arr = merge_sort(arr)
#     result = []
#     for num in sorted_arr:
#         if len(result) == 0 or result[-1] != num:
#             result.append(num)
#     return result
# arr = list(map(int, input("Toonuudaa oruul: ").split()))
# print(sort_unique(arr))



# 29.  нэр → оноо dict өгөгдөнө. Хамгийн өндөр оноотой 3 сурагчийн 
#      нэрийг ихээс бага руу буцаа. Энд sort() ашиглаж болно.
# def top_three(scores):
#     arr = []
#     for name in scores:
#         arr.append((scores[name], name))
#     arr.sort(reverse=True)
#     result = []
#     for i in range(min(3, len(arr))):
#         result.append(arr[i][1])
#     return result
# scores = {}
# n = int(input("Heden suragch ve?: "))
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     scores[name] = score
# print(top_three(scores))



# 30. Эхлээд сурагчдын тоо n, дараа нь n ширхэг оноо уншина. 
#     Эрэмбэлсэн оноонууд, хамгийн их, хамгийнбага оноо,
#     дундаж болон дунджаас дээш оноотой сурагчийн тоог хэвлэ.
# n = int(input("Heden suragch ve?: "))
# scores = []
# for i in range(n):
#     score = int(input("ONOO?: "))
#     scores.append(score)
# scores.sort()
# total = 0
# count = 0
# for score in scores:
#     total += score
# average = total / n
# for score in scores:
#     if score > average:
#         count += 1
# print("Eremblegdsan:", scores)
# print("Hamgiin ih:", scores[-1])
# print("Hamgiin baga:", scores[0])
# print("Dundaj:", average)
# print("Dundjaas deesh:", count)


