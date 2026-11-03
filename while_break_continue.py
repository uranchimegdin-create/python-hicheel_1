# 1. for` ашиглан 1-ээс 10 хүртэлх тоонуудыг нэг нэг мөрөөр хэвлэ.
# for i in range(1, 11):
#     print(i)


# 2.  1-ээс 20 хүртэлх тэгш тоонуудыг хэвлэ.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# 3. 1-ээс 20 хүртэлх сондгой тоонуудыг хэвлэ.
# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)


# 4. 5 x 1 = 5`-аас `5 x 10 = 50` хүртэл хэвлэ.
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)


# 5. Хэрэглэгчээс `N` тоо аваад 1-ээс `N` хүртэл хэвлэ.
# N = int(input("N too: "))
# for i in range(1, N + 1):
#     print(i)



# 6. Хэрэглэгчээс `N` аваад `N`-ээс 1 хүртэл буурах дарааллаар хэвлэ.
# N = int(input("N too: "))
# for i in range(N, 0, -1):
#     print(i)


# 7. 1-ээс 50 хүртэлх 3-т хуваагддаг бүх тоог хэвлэ.
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)


# 8.  1-ээс 30 хүртэлх тооноос 5-д хуваагдахгүй тоонуудыг хэвлэ.
# for i in range(1, 31):
#     if i % 5 != 0:
#         print(i)


# 9. 1-ээс 100 хүртэл хэдэн тэгш тоо байгааг тоолж хэвлэ.
# too = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         too += 1
# print("Tegsh toonii too:", too)



# 10. 1-ээс 100 хүртэл 7-д хуваагддаг хэдэн тоо байгааг ол.
# too = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         too += 1
# print("Niit too:", too)


 
# 11.  1-ээс 100 хүртэлх бүх тооны нийлбэрийг ол.
# niit = 0
# for i in range(1, 101):
#     niit += i
# print("Niilber:", niit)



# 12. 1-ээс 50 хүртэлх тэгш тоонуудын нийлбэрийг ол.
# niit = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         niit += i
# print("Niilber:", niit)



# 13.  for` ашиглахгүйгээр 1-ээс 10 хүртэл хэвлэ.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1



# 14.  10-аас 1 хүртэл буурах дарааллаар хэвлэ.
# i = 10
# while i >= 1:
#     print(i)
#     i -= 


# 15. while` ашиглан 2, 4, 6, 8, ... 20 гэж хэвлэ.
# i = 2
# while i <= 20:
#     print(i)
#     i += 2


# 16. Хэрэглэгчээс `N` аваад 1-ээс `N` хүртэлх тооны нийлбэрийг `while` ашиглан ол.
# N = int(input("N too: "))
# i = 1
# niit = 0
# while i <= N:
#     niit += i
#     i += 1
# print("Niilber:", niit)



# 17. Хэрэглэгчээс эерэг бүхэл тоо авна. Тэр тоо хэдэн цифртэйг ол.
# N = int(input("Eyreg buhel too: "))
# too = 0
# while N > 0:
#     N = N // 10
#     too += 1
# print("Tsifriin too:", too)



# 18. Өгсөн эерэг бүхэл тооны цифрүүдийн нийлбэрийг ол.
# N = int(input("Eyreg buhel too: "))
# niit = 0
# while N > 0:
#     digit = N % 10
#     niit += digit
#     N = N // 10
# print("Tsifruudiin niilber:", niit)



# 19. 1-ээс 20 хүртэл явна. Тоо 5 болоход давталтыг шууд зогсоо.
# for i in range(1, 21):
#     if i == 5:
#         break
#     print(i)



# 20. 10-аас 100 хүртэл явж, 7-д хуваагдах хамгийн эхний тоог олмогц давталтаас гар.
# for i in range(10, 101):
#     if i % 7 == 0:
#         print(i)
#         break



# 21. Нууц тоо таах. secret = 8. Хэрэглэгч тоо оруулсаар `8` оруулмагц давталтыг зогсоо.
# secret = 8
# while True:
#     too = int(input("Too oruul: "))
#     if too == secret:
#         print("Zuv taalaa!")
#         break



# 22. Хэрэглэгчээс тоо дахин дахин авна. `0` оруулмагц `break` ашиглан зогсоо.
# while True:
#     too = int(input("Too oruul: "))
#     if too == 0:
#         break
#     print(too)



# 23. Хэрэглэгчээс тоо дахин дахин авна. `0` оруулах хүртэл өмнө оруулсан бүх 
#     тооны нийлбэрийг ол.
# niit = 0
# while True:
#     too = int(input("Too oruul: "))
#     if too == 0:
#         break
#     niit += too
# print("Niilber:", niit)



# 24. 1-ээс 10 хүртэл хэвлэхдээ `5`-ыг хэвлэхгүй `continue` ашиглан алгас.
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)



# 25. 1-ээс 20 хүртэл явна. Тэгш тоо таарах бүрт `continue` хийж,
#     зөвхөн сондгой тоонуудыг хэвлэ.
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)



# 26. 1-ээс 30 хүртэл тоонуудыг хэвлэх боловч 3-т хуваагддаг тоог хэвлэхгүй.
# for i in range(1, 31):
#     if i % 3 == 0:
#         continue
#     print(i)



# 27. Хэрэглэгч 5 ширхэг тоо оруулна. Сөрөг тоо оруулбал `continue` 
#     ашиглан алгасаад, зөвхөн 0 болон эерэг тоонуудын нийлбэрийг ол.
# niit = 0
# for i in range(5):
#     too = int(input("Too oruul: "))
#     if too < 0:
#         continue
#     niit += too
# print("Niilber:", niit)



# 28. 1-ээс дээш тоонуудыг шалгаж явна. 7-д хуваагдах тоо бүрийг хэвлэнэ.
#     5 ширхэг ийм тоо олмогц `break` хий.
# i = 2
# too = 0
# while True:
#     if i % 7 == 0:
#         print(i)
#         too += 1
#     if too == 5:
#         break
#     i += 1



# 29.   Хэрэглэгчээс тоо дахин дахин авна.
#       - `0` → давталтыг бүрэн зогсооно.
#       - Сөрөг тоо → `continue`.
#       - Сондгой тоо → `continue`.
#       - Эерэг тэгш тоо → хэвлэнэ.
# while True:
#     too = int(input("Too oruul: "))
#     if too == 0:
#         break
#     if too < 0:
#         continue
#     if too % 2 != 0:
#         continue
#     print(too)



# 30.  secret = 17
#      Хэрэглэгч тоо таана.
#      - Оруулсан тоо `17`-оос бага бол `Бага байна`
#      - Их бол `Их байна`
#      - `17` бол `Зөв таалаа` гэж хэвлээд `break`
#      - Сөрөг тоо оруулбал `Сөрөг тоо оруулахгүй` гээд `continue`
# secret = 17
# while True:
#     too = int(input("Taah too: "))
#     if too < 0:
#         print("Surug too oruulahgui")
#         continue
#     if too < secret:
#         print("Baga baina")
#     elif too > secret:
#         print("Ih baina")
#     else:
#         print("Zuv taalaa!")
#         break


