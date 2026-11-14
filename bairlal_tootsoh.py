# 1. Автобусны нийт эгнээний тоо болон нэг эгнээнд байгаа суудлын тоо
#    мэдэгдэж байвал өгөгдсөн суудлын дугаар нь хэддүгээр эгнээний хэд дэх суудал болохыг ол.
#    Жич: Эгнээ бүр дэх суудлын тоо ижил.
# n, m = map(int, input("EGNEE BA 1 EGNEENII SUUDLIIN TOO?: ").split())
# k = int(input("OLOH SUUDLIIN TOO?: "))
# egnee = (k - 1) // m + 1
# suudal = (k - 1) % m + 1
# print(egnee, suudal)


# 2. Архивын нийт шүүгээний тоо болон нэг шүүгээнд байрлах хавтасны тоо
#    мэдэгдэж байвал өгөгдсөн хавтасны дугаар нь хэддүгээр 
#    шүүгээний хэд дэх хавтас болохыг ол.
#    Жич: Шүүгээ бүр ижил тооны хавтастай байна.
# n, m = map(int, input("SHUUGEENII TOO, NEG SHUUGEEND BAIGAA HAVTAS: ").split())
# k = int(input("HAVTASNII DUGAAR: "))
# shuugee = (k - 1) // m + 1
# havtas = (k - 1) % m + 1
# print(shuugee, havtas)


# 3. Сургалтын төв хэдэн бүлэгтэй болон нэг бүлэгт хэдэн сурагч
#    байгааг мэдэгдэж байвал өгөгдсөн сурагчийн 
#    дугаар нь хэддүгээр бүлгийн хэд дэх сурагч болохыг ол.
#    Жич: Бүлэг бүр ижил тооны сурагчтай байна.
# n, m = map(int, input("BULEGIIN TOO, NEG BULEGT BAIGAA SURAGCH: ").split())
# k = int(input("SURAGCHIN DUGAAR: "))
# buleg = (k - 1) // m + 1
# suragch = (k - 1) % m + 1
# print(buleg, suragch)



# 4. Зогсоол хэдэн давхартай болон нэг давхарт хэдэн машины байртай нь
#    мэдэгдэж байвал өгөгдсөн машины байр хэддүгээр давхрын хэд дэх байр болохыг ол.
#    Жич: Давхар бүр дэх машины байрны тоо ижил.
# n, m = map(int, input("DAVHRIIN TOO, NEG DAVHART BAIGAA MASHINII BAIR: ").split())
# k = int(input("MASHINII BAIRNII DUGAAR: "))
# davhar = (k - 1) // m + 1
# bair = (k - 1) % m + 1
# print(davhar, bair)


# 5. Спортын ордны секторын тоо, нэг секторт байгаа эгнээний тоо болон нэг эгнээнд
#    байгаа суудлын тоо мэдэгдэж байвал өгөгдсөн суудлын дугаар нь 
#    хэддүгээр секторын, хэддүгээр эгнээний, хэд дэх суудал болохыг ол.
#    Жич: Сектор бүр ижил тооны эгнээтэй бөгөөд эгнээ бүр дэх суудлын тоо ижил.
# n, m, p = map(int, input("SEKTOR, EGNEE, SUUDAL: ").split())
# k = int(input("SUUDLIIN DUGAAR: "))
# sektor = (k - 1) // (m * p) + 1
# egnee = ((k - 1) % (m * p)) // p + 1
# suudal = (k - 1) % p + 1
# print(sektor, egnee, suudal)

