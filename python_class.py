# 1. Phone` class үүсгээрэй.
# **Атрибут:**
# - `brand` — утасны нэр
# - `battery` — цэнэгийн хувь
# **Method:**
# - `use_phone()` — цэнэгийг 10-аар бууруулна.
# - `charge()` — цэнэгийг 20-оор нэмэгдүүлнэ.
# - `show_battery()` — одоогийн цэнэгийг хэвлэнэ.
# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery
#     def use_phone(self):
#         self.battery -= 10
#     def charge(self):
#         self.battery += 20
#     def show_battery(self):
#         print(self.brand, "цэнэг:", self.battery, "%")
# p1 = Phone("iPhone", 80)
# p1.show_battery()
# p1.use_phone()
# p1.show_battery()
# p1.charge()
# p1.show_battery()


# 2. Product` class үүсгээрэй.
# **Атрибут:**
# - `name` — бүтээгдэхүүний нэр
# - `price` — нэгж үнэ
# - `quantity` — ширхэг
# **Method:**
# - `sell(amount)` — бүтээгдэхүүний тоог өгсөн хэмжээгээр бууруулна.
# - `show_total()` — үлдсэн барааны нийт үнийг хэвлэнэ.
# Хэрэв зарах гэж буй барааны тоо үлдэгдлээс их байвал `Бараа хүрэлцэхгүй` гэж хэвлээрэй.

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def sell(self, amount):
#         if amount <= self.quantity:
#             self.quantity -= amount
#             print(amount, "ширхэг бараа зарагдлаа")
#         else:
#             print("Бараа хүрэлцэхгүй")
#     def show_total(self):
#         total = self.price * self.quantity
#         print("Бүтээгдэхүүн:", self.name)
#         print("Үлдсэн тоо:", self.quantity)
#         print("Нийт үнэ:", total)
# p1 = Product("Laptop", 2500000, 10)
# p1.show_total()
# p1.sell(3)
# p1.show_total()
# p1.sell(10)


# 3. Athlete` class үүсгээрэй.
# **Атрибут:**
# - `name` — тамирчны нэр
# - `points` — авсан оноо
# **Method:**
# - `add_points(points)` — оноог нэмнэ.
# - `lose_points(points)` — оноог хасна.
# - `show_points()` — одоогийн оноог хэвлэнэ.

# class Athlete:
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points
#     def add_points(self, points):
#         self.points += points
#     def lose_points(self, points):
#         self.points -= points
#     def show_points(self):
#         print("Name:", self.name)
#         print("Points:", self.points)
# a1 = Athlete("Bat", 50)
# a1.show_points()
# a1.add_points(20)
# a1.show_points()
# a1.lose_points(10)
# a1.show_points()



# 4. Movie` class үүсгээрэй. Хоёр кино үүсгээд тус бүрийн мэдээллийг хэвлээрэй.
# **Атрибут:**
# - `title` — киноны нэр
# - `rating` — үнэлгээ
# - `views` — үзсэн хүний тоо
# **Method:**
# - `add_view()` — үзсэн хүний тоог 1-ээр нэмнэ.
# - `update_rating(new_rating)` — үнэлгээг өөрчилнө.
# - `show_info()` — киноны мэдээллийг хэвлэнэ.
 
# class Movie:
#     def __init__(self, title, rating, views):
#         self.title = title
#         self.rating = rating
#         self.views = views
#     def add_view(self):
#         self.views += 1
#     def update_rating(self, new_rating):
#         self.rating = new_rating
#     def show_info(self):
#         print("KINONII NER:", self.title)
#         print("UNELGEE:", self.rating)
#         print("UZEGCH:", self.views)
# m1 = Movie("Avatar", 9.0, 1000)
# m2 = Movie("Titanic", 8.5, 800)
# m1.add_view()
# m1.update_rating(9.5)
# m1.show_info()
# print()
# m2.add_view()
# m2.update_rating(9.0)
# m2.show_info()



# 5. GameCharacter` class үүсгээрэй.
# **Атрибут:**
# - `name` — дүрийн нэр
# - `health` — амь
# - `damage` — довтолгооны хүч
# **Method:**
# - `attack(enemy)` — дайсны амийг өөрийн довтолгооны хүчээр бууруулна.
# - `show_health()` — дүрийн амийг хэвлэнэ.

# class GameCharacter:
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage
#     def attack(self, enemy):
#         enemy.health -= self.damage
#         print(self.name, "attacked", enemy.name)
#     def show_health(self):
#         print(self.name, "health:", self.health)
# c1 = GameCharacter("Knight", 100, 20)
# c2 = GameCharacter("Dragon", 150, 30)
# c1.attack(c2)
# c1.show_health()
# c2.show_health()



# 6. `Wallet` class үүсгээрэй.
# **Атрибут:**
# - `owner` — эзэмшигчийн нэр
# - `balance` — мөнгөний үлдэгдэл
# **Method:**
# - `add_money(amount)` — мөнгө нэмнэ.
# - `pay(amount)` — төлбөр төлнө.
# - `show_balance()` — үлдэгдлийг хэвлэнэ.
# Хэрэв үлдэгдлээс их мөнгө төлөх гэж байвал `Мөнгө хүрэлцэхгүй` гэж хэвлээрэй.

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def add_money(self, amount):
#         self.balance += amount
#     def pay(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Tulbur tulugdsun")
#         else:
#             print("Mungu hureltsehgui")
#     def show_balance(self):
#         print("Owner:", self.owner)
#         print("Balance:", self.balance)
# w1 = Wallet("Bat", 50000)
# w1.show_balance()
# w1.add_money(20000)
# w1.show_balance()
# w1.pay(30000)
# w1.show_balance()
# w1.pay(60000)



# 7. LibraryBook` class үүсгээрэй.
# **Атрибут:**
# - `title` — номын нэр
# - `available` — ном байгаа эсэх (`True` эсвэл `False`)
# **Method:**
# - `borrow()` — номыг зээлд авна.
# - `return_book()` — номыг буцаана.
# **Шаардлага:**
# - Ном байгаа үед зээлж болно.
# - Ном зээлэгдсэн үед дахин зээлэх боломжгүй.
# - Буцаасан үед дахин зээлж болно.

# class LibraryBook:
#     def __init__(self, title, available):
#         self.title = title
#         self.available = available
#     def borrow(self):
#         if self.available == True:
#             self.available = False
#             print("Nom zeeld avagdlaa")
#         else:
#             print("Nom ali hediin zeeldegdsen baina")
#     def return_book(self):
#         self.available = True
#         print("Nom butsaagdlaa")
#     def show_info(self):
#         print("Title:", self.title)
#         print("Available:", self.available)
# b1 = LibraryBook("Python", True)
# b1.show_info()
# b1.borrow()
# b1.show_info()
# b1.borrow()
# b1.return_book()
# b1.show_info()
# b1.borrow()



# 8. Exam` class үүсгээрэй.
# **Атрибут:**
# - `student_name` — сурагчийн нэр
# - `score` — оноо
# - `max_score` — боломжит дээд оноо
# **Method:**
# - `get_percentage()` — авсан онооны хувийг олно.
# - `check_result()` — авсан хувиас хамаарч үр дүн хэвлэнэ.
# **Шаардлага:**
# - 90% ба түүнээс дээш бол `Маш сайн`
# - 80% ба түүнээс дээш бол `Сайн`
# - 60% ба түүнээс дээш бол `Тэнцсэн`
# - 60%-аас бага бол `Тэнцээгүй`

# class Exam:
#     def __init__(self, student_name, score, max_score):
#         self.student_name = student_name
#         self.score = score
#         self.max_score = max_score
#     def get_percentage(self):
#         return self.score / self.max_score * 100
#     def check_result(self):
#         percent = self.get_percentage()
#         if percent >= 90:
#             print("Mash sain")
#         elif percent >= 80:
#             print("Sain")
#         elif percent >= 60:
#             print("Tentsen")
#         else:
#             print("Tentseegui")
# s1 = Exam("Bat", 85, 100)
# s2 = Exam("Anu", 45, 60)
# s3 = Exam("Bold", 55, 100)
# print("Student:", s1.student_name)
# print("Percentage:", s1.get_percentage(), "%")
# s1.check_result()
# print()
# print("Student:", s2.student_name)
# print("Percentage:", s2.get_percentage(), "%")
# s2.check_result()
# print()
# print("Student:", s3.student_name)
# print("Percentage:", s3.get_percentage(), "%")
# s3.check_result()



# 9. Employee` class үүсгээрэй.
# **Атрибут:**
# - `name` — ажилтны нэр
# - `salary` — үндсэн цалин
# - `bonus` — урамшуулал
# **Method:**
# - `add_bonus(amount)` — урамшуулал нэмнэ.
# - `get_total_salary()` — үндсэн цалин болон урамшууллыг нэмж хэвлэнэ.

# class Employee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#     def add_bonus(self, amount):
#         self.bonus += amount
#     def get_total_salary(self):
#         total = self.salary + self.bonus
#         print("Name:", self.name)
#         print("Total salary:", total)
# e1 = Employee("Bat", 2000000, 300000)
# e1.get_total_salary()
# e1.add_bonus(200000)
# e1.get_total_salary()


# 10. `CartItem` class үүсгээрэй.
# **Атрибут:**
# - `name` — барааны нэр
# - `price` — нэгж үнэ
# - `quantity` — тоо ширхэг
# **Method:**
# - `increase_quantity(amount)` — тоо ширхэгийг нэмнэ.
# - `decrease_quantity(amount)` — тоо ширхэгийг хасна.
# - `get_total_price()` — нийт үнийг хэвлэнэ.
# Гурван өөр барааны объект үүсгээд бараа бүрийн нийт үнийг хэвлээрэй.

# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def increase_quantity(self, amount):
#         self.quantity += amount
#     def decrease_quantity(self, amount):
#         if amount <= self.quantity:
#             self.quantity -= amount
#         else:
#             print("Too shirheg hureltsehgui")
#     def get_total_price(self):
#         total = self.price * self.quantity
#         print("Name:", self.name)
#         print("Total price:", total)
# item1 = CartItem("Laptop", 2500000, 2)
# item2 = CartItem("Mouse", 50000, 5)
# item3 = CartItem("Keyboard", 120000, 3)
# item1.increase_quantity(1)
# item2.decrease_quantity(2)
# item3.increase_quantity(2)
# item1.get_total_price()
# print()
# item2.get_total_price()
# print()
# item3.get_total_price()



# 11. Computer` class үүсгээрэй.
# **Атрибут:**
# - `brand` — үйлдвэрлэгч
# - `ram` — RAM хэмжээ
# - `storage` — багтаамж
# **Method:**
# - `upgrade_ram(amount)` — RAM-ийг нэмэгдүүлнэ.
# - `upgrade_storage(amount)` — багтаамжийг нэмэгдүүлнэ.
# - `show_info()` — бүх үзүүлэлтийг хэвлэнэ.

# class Computer:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#     def upgrade_ram(self, amount):
#         self.ram += amount
#     def upgrade_storage(self, amount):
#         self.storage += amount
#     def show_info(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram, "GB")
#         print("Storage:", self.storage, "GB")
# c1 = Computer("Dell", 8, 256)
# c1.upgrade_ram(8)
# c1.upgrade_storage(256)
# c1.show_info()



# 12. Account` class үүсгээрэй.
# **Атрибут:**
# - `owner` — данс эзэмшигч
# - `balance` — мөнгөний үлдэгдэл
# **Method:**
# - `deposit(amount)` — мөнгө нэмнэ.
# Дараа нь `SavingsAccount` class үүсгэж `Account` class-аас өвлүүлээрэй.
# **Нэмэлт атрибут:**
# - `interest_rate` — жилийн хүүгийн хувь
# **Шаардлага:**
# - `super()` ашиглана.
# - `add_interest()` method бичиж, үлдэгдэл дээр хүү нэмнэ.

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#     def add_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         self.balance += interest
# a1 = SavingsAccount("Bat", 100000, 10)
# a1.deposit(50000)
# a1.add_interest()
# print("EZEMSHIGCH:", a1.owner)
# print("ULDEGDEL:", a1.balance)
# print("JILIIN HUU:", a1.interest_rate, "%")



# 13. `Device` class нь:
# - `brand`
# - `price`
# гэсэн атрибуттай.
# `Laptop` class нь `Device` class-аас өвлөнө.
# **Нэмэлт атрибут:**
# - `ram`
# **Шаардлага:**
# - `super()` ашиглан үйлдвэрлэгч, үнийг хадгална.
# - `show_info()` method нь үйлдвэрлэгч, үнэ, RAM-ийг хэвлэнэ.

# class Device:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# class Laptop(Device):
#     def __init__(self, brand, price, ram):
#         super().__init__(brand, price)
#         self.ram = ram
#     def show_info(self):
#         print("UILDVERLEGCH:", self.brand)
#         print("UNE:", self.price)
#         print("RAM:", self.ram)
# l1 = Laptop("Dell", 2500000, "16GB")
# l1.show_info()



# 14. User` class үүсгээрэй.
# **Атрибут:**
# - `username`
# - `email`
# `Admin` class нь `User` class-аас өвлөнө.
# **Нэмэлт атрибут:**
# - `permission` — эрхийн түвшин
# **Шаардлага:**
# - `super()` ашиглана.
# - `show_info()` method нь хэрэглэгчийн нэр, имэйл, эрхийн түвшнийг хэвлэнэ.

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
# class Admin(User):
#     def __init__(self, username, email, permission):
#         super().__init__(username, email)
#         self.permission = permission
#     def show_info(self):
#         print("Username:", self.username)
#         print("Email:", self.email)
#         print("Permission:", self.permission)
# a1 = Admin("Bat123", "bat@gmail.com", "Full Access")
# a1.show_info()



# 15.  Character` class нь:
#      - `name`
#      - `health`
#      гэсэн атрибуттай.
#      `Mage` class нь `Character` class-аас өвлөнө.
#      **Нэмэлт атрибут:**
#      - `mana` — ид шидийн хүч
#      **Method:**
#      - `cast_spell()` — mana-г 10-аар бууруулна.
#      - Хэрэв mana 10-аас бага бол `Mana хүрэлцэхгүй` гэж хэвлэнэ.
#      - `show_info()` — дүрийн нэр, амь, mana-г хэвлэнэ.

# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
# class Mage(Character):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana
#     def cast_spell(self):
#         if self.mana >= 10:
#             self.mana -= 10
#             print("Spell cast!")
#         else:
#             print("Mana hureltsehgui")
#     def show_info(self):
#         print("Name:", self.name)
#         print("Health:", self.health)
#         print("ID SHIDIIN HUCH:", self.mana)
# m1 = Mage("Gandalf", 100, 30)
# m1.cast_spell()
# m1.show_info()
# m1.cast_spell()
# m1.cast_spell()
# m1.cast_spell()


