# 1.  `hello()` гэдэг function үүсгэ. Дуудагдахад:
#      Hello Python!
# def hello():
#     print("Hello Python!")
# hello()
 

# 2.  greet(name)` function бич. Оролт: Bat
# def greet(name):
#     print("Hello", name)
# greet("Bat")
 

# 3.  introduce(name, age)` function бич.
# def introduce(name, age):
#     print(f"{name} нь {age} настай.")
# introduce("Bat", 18)



# 4. add(a, b)` function бичээд хоёр тооны нийлбэрийг хэвлэ.
# def add(a, b):
#     print(a + b)
# add(5, 3)



# 5.  square(num)` function бич. Өгсөн тооны квадратыг return хий.
# def square(num):
#     return num * num
# result = square(5)
# print(result)



# 6. max_num(a, b)` function бич. Хоёр тооны ихийг return хий.
# def max_num(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max_num(10, 20))


# 7.
# def check_even(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even(6))
# print(check_even(7))



# 8. check_age(age)` function бич.
#    - 18 болон түүнээс дээш → `"Adult"`
#    - бусад → `"Minor"`
# def check_age(age):
#     if age >= 18:
#         return "Adult"
#     else:
#         return "Minor"
# print(check_age(20))
# print(check_age(15))


# 9.  get_grade(score)` function бич.
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"
# print(get_grade(95))
# print(get_grade(85))
# print(get_grade(75))
# print(get_grade(65))
# print(get_grade(50))



# 10. print_numbers(n)` function бич. 1-ээс n хүртэлх тоог хэвлэ.
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)
# print_numbers(5)



# 11. sum_numbers(n)` function бич. 1-ээс n хүртэлх бүх тооны нийлбэрийг return хий.
# def sum_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# print(sum_numbers(5))



# 12. count_even(n)` function бич. 1-ээс n хүртэл хэдэн тэгш тоо байгааг ол.
# def count_even(n):
#     count = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even(10))


# 13. count_digits(num)` function бич. Тоон дотор хэдэн цифр байгааг ол.
# def count_digits(num):
#     count = 0
#     while num > 0:
#         num = num // 10
#         count += 1
#     return count
# num=int(input("TOOGOO UG: "))
# print(count_digits(num))



# 14. `find_max(nums)` function бич. List доторх хамгийн их тоог return хий.
# def find_max(nums):
#     max_num = nums[0]
#     for i in nums:
#         if i > max_num:
#             max_num = i
#     return max_num
# nums = list(map(int,input("TOONUUD UG: ").split()))
# print(find_max(nums))


# 15. find_min(nums)` function бич.
# def find_min(nums):
#     min_num = nums[0]
#     for i in nums:
#         if i < min_num:
#             min_num = i
#     return min_num
# nums = [3, 8, 2, 10, 5]
# print(find_min(nums))



# 16. count_even(nums)` function бич. List дотор хэдэн тэгш тоо байгааг ол.
# def count_even(nums):
#     count = 0
#     for i in nums:
#         if i % 2 == 0:
#             count += 1
#     return count
# nums = list(map(int,input("TOONUUD UG: ").split()))
# print(count_even(nums))



# 17.  `list_sum(nums)` function бич. List-ийн бүх элементийн нийлбэрийг return хий.
# def list_sum(nums):
#     total = 0
#     for i in nums:
#         total += i
#     return total
# nums = list(map(int,input("TOONUUD UG: ").split()))
# print(list_sum(nums))



# 18.  get_age(students, name)` function бич.
# def get_age(students, name):
#     return students[name]
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print(get_age(students, "Sara"))



# 19.  
# def find_student(students, name):
#     if name in students:
#         return "Found"
#     else:
#         return "Not found"
# students = {
#     "Bat": 18,
#     "Sara": 19,
#     "Bold": 20
# }
# print(find_student(students, "Sara"))
# print(find_student(students, "Anu"))



# 20.
# def average_score(students):
#     total = 0
#     for score in students.values():
#         total += score
#     return total / len(students)
# students = {
#     "Bat": 80,
#     "Sara": 90,
#     "Bold": 70
# }
# print(average_score(students))



# 21. unique_count(nums)` function бич. List-ийн давхардаагүй элементийн тоог ол.
# def unique_count(nums):
#     return len(set(nums))
# nums = list(map(int,input("TOONUUD UG: ").split()))
# print(unique_count(nums))



# 22.  unique_numbers(nums)` function бич. List-ээс давхардлыг арилгаад set буцаа.
# def unique_numbers(nums):
#     return set(nums)
# nums =  list(map(int,input("TOONUUD UG: ").split()))
# print(unique_numbers(nums))


# 23.  
# def greet(name="Guest"):
#     print("Hello", name)
# greet()
# greet("Bat")



# 24.
# power(num, exponent=2)` function бич.
# def power(num, exponent=2):
#     return num ** exponent
# print(power(5))
# print(power(2, 3))



# 25. `discount(price, percent=10)` function бич. Default-аар 10% хямдардаг байг.
# def discount(price, percent=10):
#     return price - (price * percent / 100)
# print(discount(10000))
# print(discount(10000, 20))



# 26. sum_all(*args)` function бич. Хэдэн ч тоо өгсөн нийлбэрийг ол.
# def sum_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(sum_all(1, 2, 3))
# print(sum_all(10, 20, 30, 40))



# 27. 
# def find_max(*args):
#     max_num = args[0]
#     for i in args:
#         if i > max_num:
#             max_num = i
#     return max_num
# print(find_max(5, 8, 2, 10, 3))



# 28. 
# def count_even(*args):
#     count = 0
#     for i in args:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even(1, 2, 4, 7, 8, 10))



# 29.  
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# show_info(name="Bat", age=18, city="Ulaanbaatar")



# 30.
# def calculate_total(**prices):
#     total = 0
#     for price in prices.values():
#         total += price
#     return total
# print(calculate_total(
#     apple=2000,
#     banana=3000,
#     orange=2500
# ))



# 31.
# def analyze_numbers(nums):
#     max_num = nums[0]
#     min_num = nums[0]
#     total = 0
#     even = 0
#     odd = 0
#     for i in nums:
#         total += i
#         if i > max_num:
#             max_num = i
#         if i < min_num:
#             min_num = i
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return {
#         "max": max_num,
#         "min": min_num,
#         "sum": total,
#         "even": even,
#         "odd": odd
#     }
# nums =list(map(int,input("JAGSAALT UG: ").split()))
# print(analyze_numbers(nums))  


# 32. 
# def student_average(students, name):
#     scores = students[name]
#     total = 0
#     for score in scores:
#         total += score
#     return total / len(scores)
# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(student_average(students, "Bat"))



# 33. best_student(students)` function бич. Дээрх dictionary-ээс
#     хамгийн өндөр дундажтай оюутны нэрийг return хий.
# def best_student(students):
#     best_name = ""
#     best_average = 0
#     for name, scores in students.items():
#         total = 0
#         for score in scores:
#             total += score
#         average = total / len(scores)
#         if average > best_average:
#             best_average = average
#             best_name = name
#     return best_name
# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(best_student(students))


# 34.
# def calculate(*args, **kwargs):
#     total = 0
#     for i in args:
#         total += i
#     bonus = kwargs.get("bonus", 0)
#     tax = kwargs.get("tax", 0)
#     return total + bonus - tax
# print(calculate(10, 20, 30, bonus=100, tax=20))
