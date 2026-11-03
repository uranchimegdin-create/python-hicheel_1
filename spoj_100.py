# 1.
# a, b = map(int, input("input :").split())
# c = a+b
# print(c)


# 2.
# a, b, c = map(int, input("Input: ").split())
# c=a + b + c
# print(c)


# 3.
# a = int(input())
# print(a**3, (a **2) *6)


# 4.
# a, b = map(int, input("input: ").split())
# print((a+b)*2+4, a + a + b + b)


# 5.
# a = int(input())
# y = 3 *a-5
# print(y )


# 6.
# a = int(input())
# y = 4 *(a**2) - 3 * a + 5
# print(y)


# 7.
# a, b, c = map(int, input("input:").split())
# print((a+b+c)%11)


# 8.
# a = int(input())
# print((a//10) %10)


# 9
# a = int(input())
# e = a // 10
# j = a % 10
# print(e * j)


# 10.
# a, b ,c= map(int, input("input: ").split())
# print ((a + b + c) %10)


# 1.1
# a = int(input())
# b = a // 60
# v = a % 60
# print(b, v)

# 12
# c = int(input())
# s = c // 3600
# a = c // 3600 // 60
# b = c % 60
# print(s, a, b)

# 13.
# a, b= map(int, input().split())
# print(a*60+b)


# 14.
# a = int(input("TOOGOO UG: "))
# b = a // 24
# print(b , a%24)



# 15.
# a,b = map(int, input().split())
# print(a*24+b)


# 16.
# s = int(input())
# print(s // 12, s % 12)


# 17.
# s,c = map(int, input().split())
# print(s*12+c) 


# 18.
# a = list(map(int, input().split()))
# print(max(a))


# 19.
# a = list(map(int, input().split()))
# print(min(a))

# 20.
# a = list(map(int, input().split()))
# print(max(a))


# 21.
# a = list(map(int, input().split()))
# print(min(a))


# 22.
# a = list(map(int, input().split()))
# s = 0
# for i in range(len(a)):
#     if a[i]>80:
#         s +=a[i]
# print(s)



# 23.
# a = list(map(int, input().split()))
# s = 1
# for i in range(len(a)):
#     if a[i]<5:
#         s *=a[i]
# print(s)


# 24.
# a = list(map(int, input("list ug: ").split()))
# t = 0
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         t +=a[i]
# print(t)


# 25.
# a = list(map(int, input().split()))
# t = 1
# for i in range(len(a)):
#     if a[i] % 2 != 0:
#         t *=a[i]
# print(t)


# 26.
# a = list(map(int, input().split()))
# t = 0
# for i in range(len(a)):
#     if a[i] == 5:
#         t +=1
# print(t)


# 27.
# a = list(map(int, input().split()))
# for i in range(len(a)):
#     if a[i] % 3 == 0:
#         print(a[i])


# 28.
# a = list(map(int, input().split()))
# t = 0
# for i in range(len(a)):
#     if a[i] % 11 != 0:
#         t += a[i]
# print(t)


# 29.
# a = int(input())
# if a > 10:
#     print("Yes")
# else:
#     print("No")

# task 30
# a = int(input())
# if a <= 5:
#     print("yes")
# else:
#     print("No")



# 31.
# a = int(input())
# b = int(input())
# n = int(input())
# if a % 2 ==0:
#     print("yes")
# else:
#     print("no")
# if b % 2 == 0:
#         print("yes")
# else:
#          print("no")
# if n % 2 == 0:
#             print("yes")
# else:
#             print("no")



# 32.
# print("IOI")



# 33.
# for i in range(3):
#     print("IOI")



# 34.
# n = int(input())
# for i in range(n):
#     print("IOI")



# 35.
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s += i
# print(s)


# 36.
# n = int(input())
# fact = 1 
# i = 1
# while i <=n:
#     fact*= i
#     i+=1
# print(fact)



# 37.
# n = int(input())
# s = 0
# i = 1
# while i <= 100:
#     s += n
#     i +=1
# print(s)


# 38.
# n, a = map(int, input().split())
# print(n*a)

# task 39
# n = int(input())
# print(2 **n)



# 40.
# a,n = map(int, input().split())
# print(a ** n)


# 41.
# a = int(input())
# if a > 3:
#     print("Tsentssen")
# else:
#     print("Tseneegui")


# 42.
# a = int(input())
# if a >= 5 :
#     print("tsenssen")
# elif a >= 4:
#     print("Sain")
# elif a >= 3:
#     print("Dund")
# elif a >= 2:
#     print("Muu")
# else:
#     print("unasan")



# 43.
# score = int(input())
# if score < 0 or score > 100:
#     print("invalid score")
# elif score >= 89:
#     print("A")
# elif score >= 79:
#     print("B")
# elif score >= 69:
#     print("C")
# elif score >= 59:
#     print("D")
# else:
#     print("F")



# 44.
# n = int(input())
# if 1 <= n <= 7 : 
#     print("Friday")

#  task 45
# n = int(input())
# if 2 <= n <=4:
#     print("Spring")
# elif 5 <= n <= 7:
#     print("Summer")
# elif 8 <= n <= 10:
#     print("Autumn")
# else:
#     print("Winter")



# 46.
# a , b , c = map(int, input().split())
# if (a + b> c) and (a + c > b) and (b + c > a):
#     print("Yes")
# else:
#     print("No")


# 47.
# n = int(input())
# for i in range (1,11):
#     print(n, "*", i , "=", n* i)



# 48.
# a,n = map(int, input().split())
# for n in range(1,11):
#     print(a, "*", n, "=", a**n)


# 49.
# a, b, c= map(int, input().split())
# n = a*b-c
# print(a)



# 50.
# f,k = map(int, input().split())
# n = int(input())
# floor = (n-1) // k +1
# door = (n-1) % k +1
# print(floor, door)


# 51.
# f,k,m = map(int, input().split())
# n = int(input())
# a = f * m
# floor = (n - 1) // a +1
# door = (n-1) %a // m +1
# orts = (n -1) % m +1
# print(floor, door, orts)


# 52.
# n = int(input())
# print( n* (n + 1) // 2)



# 53.
# n = int(input())
# print( n* (n + 1) * ( 2 * n + 1)// 6)



# 54.
# n = int(input())
# print (((n+1)// 2)** 2)



# 55.
# n = (input())
# print(n[0] )



# 56.
# n = (input())
# a = 0
# for i in n:
#     a +=int(i)
# print(a)



# 57.
# n = (input())
# a = 0
# for i in n :
#     if int(i) % 2 == 0:
#         a +=int(i)
# print(a)



# 58.
# n = (input())
# a = 0
# for i in n :
#     if int(i) % 2 != 0:
#         a +=1
# print(a)



# task 59
# n , m= input().split()
# a = n.count(m)
# print(a) 



# 60.
# n = [4,6,3,2]
# print(max(n))



# 61.
# n = [9,6,4,9]   
# print(min(n))



# 62.
# s = input().split()
# r = s[::-1]
# res = int(r)
# print(res)



# 63.
# n = int(input("TOOGOO UG: "))
# a = str(n) [::-1]
# print(a)
    


# 64.
# n = int(input())
# if n ** 2 != 0:
#     print("Yes")
# else:
#     print("No")



# 65.
# n = int(input())
# while n != 0 and n % 3 == 0:
#     n = n// 3
# print(n)



# 66.
# n = int(input())
# i = 1
# while n% i == 0:
#     n = n // i
#     if n == 1:
#         break
#     i += 1
# if n ==1:
#     print(i)
# else:
#     print("No")



# 67.
# a, n = map(int, input().split())
# while n != 0:
#     a,n = n, a %n
# print(a)



# 68.
# a, b = map(int, input().split())
# if a == 0 or b == 0:
#     print(0)
# else:
#     x,y = a,b
#     while b != 0:
#         a,b = b, a% b
#     f = a
#     l = (x // f) * y
# print(l)



# 69.
# a, b = map(int, input().split())
# x, y = a, b
# while y != 0:
#     x, y = y, x % y
# g = x
# print(f"{a // g}/{b // g}")



# 70.
# n = int(input())
# for i in range(n):
#     print(n, end="")
# print()  



# 71.
# n = int(input())
# for n in range(n):
#     print(n, end=" ")
# print()  



# 72.
# n = int(input())
# for i in range(9, n -1, -1):
#     print(i)



# 73.
# n = int(input())
# for i in range(n):
#     for j in range(1, n + 1):
#         print(j, end="")
# print()



# 74.
# n = int(input())
# row = " ".join(map(str, range(n, 0, -1)))
# for n in range(n):
#     print(row)



# 75.
# n = int(input())
# for i in range(n, 0, -1):
#     row = " ".join(map(str, range(1, i + 1)))
#     print(row)



# 76.
# n = int(input())
# for i in range(1, n + 1):
#     row = " ".join(map(str, range(n, n - i, -1)))
#     print(row)



# 77.
# n = int(input())
# for i in range(n, 0, -1):
#     row = " ".join(map(str, range(i, 0, -1)))
#     print(row)



# 78.
# k = int(input())
# a = (k + 3) * (k + 2) * (k + 1) // 6
# print(a)



# 79.
# a,b,c = map(int, input().split())
# if a * a + b*b == c*c:
#     print("Right")
# elif a*a + b *b < c*c:
#     print("Obsute")
# else:
#     print("Acute")



# 80.
# a,b, c = map(int, input().split())
# max_val = a
# if b >max_val :
#     max_val = b
# elif c > max_val :
#     max_val = c
# else:
#     pass
# lcm = max_val
# while True:
#     if lcm % a == 0:
#         if lcm % b == 0:
#             if lcm % c == 0:
#                 print(lcm)
#                 break
#             else:
#                 lcm += max_val
#         else:
#             lcm += max_val
#     else:
#         lcm += max_val




# 81.
# a,b = map(int, input().split())
# while a > 0:
#     if b > 0:
#         if a >= b:
#             side = b
#             count = a // b
#             print(side,count)
#             a = a % b
#         else:
#             side = a
#             count = b // a
#             print(side, count)
#             b = b % a
#     else:
#         break



# 82.
# n = int(input())
# if n > 0 :
#     new = n * 10 + 1
#     an = new * new
#     print(an)
# else:
#     print()



# 83.
# a, b = map(float, input().split())
# target = a * a + b * b
# c = target / 2.0
# while True:
#     diff = c * c - target
#     if diff < 0:
#         diff = -diff
#     else:
#         pass
#     if diff < 0.000001:
#         break
#     else:
#         c = 0.5 * (c + target / c)
# print(c)




# 84.
# a, b, c = map(float, input().split())
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)



# 85.
# L = float(input())
# PI = 3.141592
# S = (L ** 2) / (4 * PI)
# print(S)



# 86.
# x1, x2 = map(int, input().split())
# dist1 = ((x1 - x2) ** 2) ** 0.5
# x1_2d, y1_2d, x2_2d, y2_2d = map(int, input().split())
# dist2 = ((x1_2d - x2_2d) ** 2 + (y1_2d - y2_2d) ** 2) ** 0.5
# x1_3d, y1_3d, z1_3d, x2_3d, y2_3d, z2_3d = map(int, input().split())
# dist3 = ((x1_3d - x2_3d) ** 2 + (y1_3d - y2_3d) ** 2 + (z1_3d - z2_3d) ** 2) ** 0.5
# print(dist1)
# print(dist2)
# print(dist3)




# 87.
# a, b = map(float, input().split())
# arithmetic_mean = (a + b) / 2
# geometric_mean = (a * b) ** 0.5
# print(arithmetic_mean, geometric_mean)



# 88.
# n = int(input())
# total_sum = (n * (n + 1) // 2) ** 2
# print(total_sum)




# 89.
# r = float(input())
# PI = 3.141592
# area = PI * (r ** 2)
# circumference = 2 * PI * r
# print(area, circumference)




# 90.
# n = int(input())
# total_sum = 0
# for i in range(n):
#     num = int(input())
#     total_sum += num
# print(total_sum)




# 91.
# n = int(input())
# total_sum = 0
# count = 0
# while count < n:
#     element = int(input()) 
#     if element > 0:
#         total_sum += element 
#     count += 1
# print(total_sum)



# 92.
# n = int(input()) 
# bad_grades_count = 0  
# for _ in range(n):
#     score = int(input())  
#     if score < 60:
#         bad_grades_count += 1 
# print(bad_grades_count)  



# 93.
# n = int(input())
# odd_count = 0     
# even_count = 0   
# for _ in range(n):
#     num = int(input())  
#     if num % 2 != 0:
#         odd_count += 1  
#     else:
#         even_count += 1 
# if odd_count > even_count:
#     print("YES")
# else:
#     print("NO")




# 94.
# n = int(input())
# a = list(map(int, input().split()))
# print(max(a))



# 95.
# n = int(input())
# a = list(map(int, input().split()))
# print(min(a))



# 96.
# n = int(input())
# elements = list(map(int, input().split()))
# target = int(input())
# count = elements.count(target)
# print(target, count)




# 97.
# n = int(input())
# elements = list(map(int, input().split()))
# max_value = max(elements)
# max_index = elements.index(max_value) + 1
# print(max_value, max_index)




# 98.
# n = int(input())
# a = list(map(int, input().split()))
# max_v= max(a)
# count = a.count(max_v)
# print(max_v, count)




# 99.
# n = int(input())
# elements = list(map(int, input().split())) 
# target = int(input())
# found = False
# for x in elements:
#     if x == target:
#         found = True
#         break  
# if found:
#     print("YES")
# else:
#     print("NO")



# 100.
# n = int(input())
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i  
#     print(i , "!=", factorial )

