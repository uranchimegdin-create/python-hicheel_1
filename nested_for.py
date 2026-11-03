# 1. nэг ангид N сурагч байна. Сурагч бүр M шалгалт өгсөн. Сурагч
#    бүрийн нийт оноо, дундаж оноог ол.
#    Дундаж нь 60 ба түүнээс дээш бол «Тэнцсэн», бусад үед «Тэнцээгүй» гэж хэвлэ.
# N = int(input("HEDEN NER BNA?: "))
# M = int(input("HEDEN SHALGALT UGSUN?: "))
# for i in range(N):
#     niit = 0
#     for j in range(M):
#         onoo = int(input("ONOO?: "))
#         niit += onoo
#     dundaj = niit / M
#     if dundaj >= 60:
#         hariu = "Tentsen"
#     else:
#         hariu = "Tentseegui"
#     print("Niit onoo:", niit)
#     print("Dundaj onoo:", dundaj)
#     print(hariu)



# 2. Дэлгүүрт N хүн үйлчлүүлнэ. Хүн бүрийн авсан барааны нэгж үнэ, ширхэгээр төлөх дүнг ол.
# Дараа нь өгсөн мөнгийг авна. Мөнгө хүрвэл хариулт, хүрэхгүй бол дутуу мөнгийг хэвлэ.
# ### Оролтын дараалал
# 1. Худалдан авагчийн тоо N (N ≥ 1).
# 2. Хүн бүрийн хувьд: барааны төрлийн тоо M (M ≥ 1).
# 3. Тэр хүний бараа бүрийн нэгж үнэ, ширхэгийг ээлжлэн оруулна.
# 4. Бүх барааг оруулсны дараа тухайн хүний өгсөн мөнгийг оруулна.
# Үнэ, ширхэг эерэг бүхэл тоо; өгсөн мөнгө сөрөг биш байна.

# N = int(input("HEDEN HVN UILCLUULSEN?: "))
# for i in range(N):
#     M = int(input("HEDN TURLIIN BARAA AVSAN?: "))
#     niit = 0
#     for j in range(M):
#         une = int(input("BARAANII UNE ORUUL: "))
#         shirheg = int(input("HEDEN SHIRHEG ABSAN?: "))
#         niit += une * shirheg
#     mungu = int(input("HEDEN TUGRUG TULSUN?: "))
#     print("Niit tulbur:", niit)
#     if mungu >= niit:
#         print("Hariult:", mungu - niit)
#     else:
#         print("Dutuu mung:", niit - mungu)



# 3. N ажилчин тус бүр 5 өдөр ажиллана. Өдөр бүрийн эхний 8 цагийн нэг цагийн хөлс 5000₮,
#    илүү цагийн нэг цагийн хөлс 7500₮ байна. Ажилчин бүрийн 5 өдрийн нийт цалинг ол.

# N = int(input("Ajilchdiin too: "))
# for i in range(N):
#     niit = 0
#     print(i + 1, "-r ajilchnii ajillasan tsag:")
#     for j in range(5):
#         tsag = int(input(str(j + 1) + "-r udur: "))
#         if tsag <= 8:
#             tsalin = tsag * 5000
#         else:
#             tsalin = 8 * 5000 + (tsag - 8) * 7500
#         niit += tsalin
# print("Niit tsalin:", niit)



# 4. N хүний анхны өрийг авна. Хүн бүр M сарын турш сар бүр төлсөн мөнгөө оруулна. Төлөлт 
#    бүрийн дараах үлдэгдэл болон хүн бүрийн нийт төлсөн мөнгийг хэвлэ. Хүү тооцохгүй.

# N = int(input("Humuusiin too: "))
# M = int(input("Sariin too: "))
# for i in range(N):
#     ur = int(input("Anhnii ur: "))
#     niit = 0
#     for j in range(M):
#         tulult = int(input(str(j + 1) + "-r sariin tulult: "))
#         ur -= tulult
#         niit += tulult
#         print("Uldegdel:", ur)
#     print("Niit tulsun mung:", niit)


# 5. Үйлдвэр N өдөр ажиллана. Өдөр бүр M удаагийн үйлдвэрлэлээр гаргасан 
#    бүтээгдэхүүний тоог оруулна. Нэг хайрцагт 12 бүтээгдэхүүн багтана.
#    Өдөр бүрийн нийт бүтээгдэхүүн, бүтэн хайрцаг, үлдэгдлийг ол.
#    Өдрүүдийг тус тусад нь тооцно. Өмнөх өдрийн үлдэгдлийг дараагийн өдөрт нэмж тооцохгүй.

# N = int(input("Udriin too: "))
# M = int(input("Uildverleliin too: "))
# for i in range(N):
#     niit = 0
#     for j in range(M):
#         too = int(input(str(j + 1) + "-r uildverleliin too: "))
#         niit += too
#     hairtsag = niit // 12
#     uldegdel = niit % 12
#     print("Niit buteegdehuun:", niit)
#     print("Buten hairtsag:", hairtsag)
#     print("Uldegdel:", uldegdel)



# 6. Автобус N удаа аялна. Аялал бүр M буудалтай, эхлэхдээ 0 зорчигчтой. Буудал бүрд 
#    эхлээд буусан, дараа нь суусан хүний тоог оруулна. 
#    Буудал бүрийн дараах зорчигч, аялал бүрийн нийт суусан хүний тоо болон 
#    орлогыг ол. Суух бүрд нэг хүн 1000₮ төлнө.

# N = int(input("Ayalliin too: "))
# M = int(input("Buudliin too: "))
# for i in range(N):
#     hun = 0
#     niit = 0
#     print(i + 1, "-r ayalal:")
#     for j in range(M):
#         buusan = int(input("Buusan hun: "))
#         suusan = int(input("Suusan hun: "))
#         hun -= buusan
#         hun += suusan
#         niit += suusan
#         print("Zorchiigch:", hun)
#     orlogo = niit * 1000
#     print("Niit suusan hun:", niit)
#     print("Orlogo:", orlogo)



# 7. 1-ээс N хүртэлх тоо бүрийн бүх эерэг хуваагчийн тоо болон нийлбэрийг ол.
#    Хуваагч гэдэг нь тухайн тоог үлдэгдэлгүй хуваадаг эерэг бүхэл тоо.
#    Жишээлбэл 6-ын хуваагчид нь 1, 2, 3, 6.

# N = int(input("N too: "))
# for i in range(1, N + 1):
#     too = 0
#     niilber = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             too += 1
#             niilber += j
#     print(i, "- Huvaagchiin too:", too)
#     print(i, "- Huvaagchiin niilber:", niilber)



# 8.  1-ээс N хүртэлх эерэг бүхэл тоонуудаас нийлбэр нь 
#     N болох бүх хосыг хэвлэж, хосын тоог ол.
#     Эхний тоо хоёр дахь тооноос бага эсвэл тэнцүү байна. 
#     1 + 5 ба 5 + 1-ийг давхар хэвлэхгүй. Ижил тоонуудтай хос байж болно.

# N = int(input("N too: "))
# too = 0
# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if i + j == N:
#             print(i, "+", j)
#             too += 1
# print("Hosiin too:", too)



# 9. 1000₮ болон 2000₮-ийн дэвсгэрт хангалттай олон байгаа. Яг N төгрөг
#    бүрдүүлэх бүх хувилбарыг олж, тоог хэвлэ.
#    Хувилбар бүрд хоёр төрлийн дэвсгэртээс хэдэн ширхэг ашигласныг харуул. Аль нэгийн 
#    тоо 0 байж болно. Дэвсгэртүүдийн дарааллыг тооцохгүй.

# N = int(input("N mungu: "))
# too = 0
# for i in range(N // 1000 + 1):
#     for j in range(N // 2000 + 1):
#         if i * 1000 + j * 2000 == N:
#             print("1000 tugrug:", i, "shirheg")
#             print("2000 tugrug:", j, "shirheg")
#             too += 1
# print("Niit huvilbar:", too)



# 10. 1-ээс N хүртэлх эерэг бүхэл тоонуудаас үржвэр нь
#     N болох бүх хосыг ол. Эхний тоо хоёр дахь тооноос бага эсвэл тэнцүү байна.
#     Хос бүрийн хоёр дахь тооноос эхний тоог хассан ялгаврыг хэвлэ.
#     Эцэст нь нийт хосын тоог хэвлэ.

# N = int(input("N too: "))
# too = 0
# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if i * j == N:
#             yalgaa = j - i
#             print(yalgaa)
#             too += 1
# print("Niit hos:", too)



