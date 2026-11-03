# 1.   6` тоог index ашиглан хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(nums[1][2])



# 2.  "Bold"` нэрийг index ашиглан хэвлэ
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# print(students[2][0])



# 3.  2 дахь дотор list-ийг бүтнээр нь хэвлэ.
# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# print(nums[1])


# 4.  Index ашиглан `70` тоог хэвлэ.
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print(nums[2][0])



# 5. Nested list-ийн хамгийн эхний утгыг хэвлэ.
# nums = [
#     [5, 10],
#     [15, 20]
# ]
# print(nums[0][0])



# 6.  Nested list-ийн хамгийн сүүлийн утгыг хэвлэ.
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# print(nums[2][1])



# 7.  for` loop ашиглан мөр бүрийг хэвлэ.
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for mur in nums:
#     print(mur)


# 8.  Nested loop ашиглан бүх тоог нэг нэгээр нь хэвлэ.
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for mur in nums:
#     for too in mur:
#         print(too)


# 9.   Бүх тоог нэг мөрөнд хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for mur in nums:
#     for too in mur:
#         print(too, end=" ")



# 10.  10-аас их бүх тоог хэвлэ.
# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for mur in nums:
#     for too in mur:
#         if too > 10:
#             print(too)


# 11.  Nested list дотор нийт хэдэн тоо байгааг ол.
# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]
# count = 0
# for row in nums:
#     for num in row:
#         count += 1
# print(count)



# 12.  Бүх тооны нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# total = 0
# for row in nums:
#     for num in row:
#         total += num
# print(total)



# 13. Тэгш тоонуудыг хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in nums:
#     for num in row:
#         if num % 2 == 0:
#             print(num)


# 14.  Сондгой тоонуудын тоог ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in nums:
#     for num in row:
#         if num % 2 != 0:
#             print(num)



# 15. Тэгш тоонуудын нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]
# total = 0
# for row in nums:
#     for num in row:
#         if num % 2 == 0:
#             total += num
# print(total)


#  16.   Эерэг тоонуудын тоог ол
# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]
# count = 0
# for row in nums:
#     for num in row:
#         if num > 0:
#             count += 1
# print(count)



# 17.  Сөрөг тоонуудын нийлбэрийг ол
# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]
# total = 0
# for row in nums:
#     for num in row:
#         if num < 0:
#             total += num
# print(total)



# 18. Хамгийн их тоог ол
# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]
# max_num = nums[0][0]
# for row in nums:
#     for num in row:
#         if num > max_num:
#             max_num = num
# print(max_num)



# 19. Хамгийн бага тоог ол
# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ] 
# min_num = nums[0][0]
# for row in nums:
#     for num in row:
#         if num < min_num:
#             min_num = num
# print(min_num)



# 20. Мөр бүрийн нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in nums:
#     total = 0
#     for num in row:
#         total += num
#     print(total)



# 21. Мөр бүрийн хамгийн их тоог ол
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for row in nums:
#     max_num = row[0]
#     for num in row:
#         if num > max_num:
#             max_num = num
#     print(max_num)



# 22. Мөр бүрийн хамгийн бага тоог ол
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for row in nums:
#     min_num = row[0]
#     for num in row:
#         if num < min_num:
#             min_num = num
#     print(min_num)



# 23. `7` тоо байгаа эсэхийг шалга
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# found = False
# for row in nums:
#     for num in row:
#         if num == 7:
#             found = True
# if found:
#     print("Байна")
# else:
#     print("Байхгүй")



# 24. Өгөгдсөн тоо хэдэн удаа байгааг ол
# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]
# target = 2
# count = 0
# for row in nums:
#     for num in row:
#         if num == target:
#             count += 1
# print(count)


# 25.  5-аас их тоонуудын нийлбэрийг ол
# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ]
# total = 0
# for row in nums:
#     for num in row:
#         if num > 5:
#             total += num
# print(total)


 
# 26.  Хамгийн их нийлбэртэй мөрийг ол
# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]
# max_sum = 0
# max_row = []
# for row in nums:
#     total = 0
#     for num in row:
#         total += num
#     if total > max_sum:
#         max_sum = total
#         max_row = row
# print("Мөр:", max_row)
# print("Нийлбэр:", max_sum)



# 27.   Сурагч бүрийн нэр ба насыг хэвлэ
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# for student in students:
#     print("Нэр:", student[0])
#     print("Нас:", student[1])



# 28.  18-аас дээш настай сурагчдыг хэвлэ
# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]
# for student in students:
#     if student[1] > 18:
#         print(student[0], student[1])


# 29.  Сурагч бүрийн дундаж оноог ол
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80]
# ]
# for student in students:
#     total = 0
#     for score in student[1:]:
#         total += score
#     avg = total / 3
#     print(student[0], "Dundaj onoo:", avg)


# 30.  Хамгийн өндөр дундажтай сурагчийг ол
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80],
#     ["Anu", 90, 90, 90]
# ]
# max_avg = 0
# best_student = ""
# for student in students:
#     total = 0
#     for score in student[1:]:
#         total += score
#     avg = total / 3
#     if avg > max_avg:
#         max_avg = avg
#         best_student = student[0]
# print("Hamgiin undur dundajtai suragch:", best_student)
# print("Dundaj onoo:", max_avg)
