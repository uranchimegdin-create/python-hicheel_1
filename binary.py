# 1. 
# lst=[5,10,15,20,25,30,35]
# target = int(input())
# left = 0
# right = len(lst)-1
# while left <= right:
#     mid = (left + right) // 2 
#     if lst[mid] == target:
#         print("olloo")
#         break
#     elif lst[mid]< target:
#         left = mid + 1
#     else : 
#         right = mid - 1


# # 
# BYNARY.SEARCH BODLOGOGOGOGOGO.


# 1. Хэрэглэгчээс нэг тоо авч, жагсаалтад байгаа эсэхийг шалга. Байвал `Олдлоо`,
#    байхгүй бол `Олдсонгүй` гэж хэвлэ.
# lst=[3, 7, 12, 18, 25, 31, 40]
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI")



# 2. Хэрэглэгчээс тоо авч, олдсон тооны индексийг хэвлэ. Байхгүй бол `-1` хэвлэ.
# lst=[5, 10, 15, 20, 25, 30]
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI")



# 3. Binary Search ашиглан `4` тоог олж, индексийг нь хэвлэ.
# lst=[4, 9, 14, 19, 24, 29, 34]
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI")



# 4.  hamgiin svvvlchiiin тоог хайж, индексийг хэвлэ.
# lst=list(map(int,input("jagsaaltaa ug: ").split(",")))
# a = lst[-1]
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==a:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < a:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI") 



# 5. Хэрэглэгчээс тоо авч хай. Олдохгүй бол `Хайж буй тоо байхгүй` гэж хэвлэ.
# lst=list(map(int,input("jagsaaltaa ug: ").split(",")))
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("haisan too chini algaaaaaa") 



# 6. Хэрэглэгчийн оруулсан тоог Binary Search ашиглан хайж, 
#    хэдэн удаа `mid` шалгасныг хэвлэ.
# lst=list(map(int,input("jagsaaltaaa ug: ").split()))
# target=int(input("taah toogoo ug: "))
# count=0
# left=0
# right=len(lst)-1
# while left <= right:
#     mid = (left+right)//2
#     count+=1
#     if lst[mid]==target:
#         return count
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# return -1
# else:
#     print("haisan too chini algaaaaaa") 



# 6. Хэрэглэгчийн оруулсан тоог Binary Search ашиглан хайж, хэдэн удаа 
#   `mid` шалгасныг хэвлэ.
# def binary(ist,target):
#     count=0
#     left=0
#     right=len(lst)-1
#     while left <= right:
#         mid = (left+right)//2
#         count+=1
#         if lst[mid]==target:
#             return count
#         elif lst[mid] < target:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1
# lst=list(map(int,input("jagsaaltaaa ug: ").split(",")))
# lst.sort()
# target=int(input("taah toogooon ug: "))
# print(benary(lst,target))



# 7.  Хэрэглэгчээс оноо авч, тухайн оноо жагсаалтад байгаа эсэхийг шалга. 
#     Байвал индексийг нь хэвлэ.
# scores = list(map(int, input("Onoonuudaa oruul: ").split()))
# target = int(input("Haih onoo: "))
# scores.sort()
# left = 0
# right = len(scores) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if scores[mid] == target:
#         print("Oldloo! Index:", mid)
#         found = True
#         break
#     elif scores[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if found == False:
#     print("Oldsongui")
 

# 8. Хэрэглэгч барааны код оруулна. Код олдвол `Бараа бүртгэлтэй`,
#    үгүй бол `Бараа бүртгэлгүй` гэж хэвлэ.
# code=list(map(int,input("BARAANUUDIIN CODE ORUUL: ").split()))
# target=int(input("HAIH CODE UG: "))
# left=0
# right=len(code)-1
# while left <= right:
#     mid=(left+right)//2
#     if code[mid]==target:
#         print("BARAA BURTGELTEIII", mid)
#         break
#     elif code[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("BARAA BURTGELGUI BNA")


# 9. Хэрэглэгчээс номын дугаар авч, олдвол индексийг нь хэвлэ. Олдохгүй бол `-1` хэвлэ.
# dugaar=list(map(int,input("NOMNUUDIIN DUGAAR ORUUL: ").split()))
# target=int(input("HAIH DUGAAR UG: "))
# left=0
# right=len(dugaar)-1
# while left <= right:
#     mid=(left+right)//2
#     if dugaar[mid]==target:
#         print(f"NOM BURTGELTEIII,INDEX NI: {mid}")
#         break
#     elif dugaar[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print(-1)


# 10. Хэрэглэгчээс тоо авч Binary Search ашиглан хай. Олдвол индексийг,
#     олдохгүй бол `Олдсонгүй` гэж хэвлэ. Мөн хайлтын явцад 
#     left`, `right`, `mid` утгуудыг алхам бүрд хэвлэ.
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# target = int(input("Haih too: "))
# numbers.sort()
# left = 0
# right = len(numbers) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     print("left =", left, "right =", right, "mid =", mid)
#     if numbers[mid] == target:
#         print("Index:", mid)
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if found == False:
#     print("Олдсонгүй")



# 11. Хэрэглэгчээс тоо авч, тухайн тоо олон давтагдсан байсан ч
#     хамгийн **эхний** индексийг Binary Search ашиглан ол.
# def binary_search_first(arr, target):
#     left = 0
#     right = len(arr) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             result = mid
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# nums = list(map(int, input("Toonuudaa oruul: ").split()))
# target = int(input("Haih toogoo oruul: "))
# print(binary_search_first(nums, target))



# 13. 
# def search_insert(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left
# nums = list(map(int,input("JAGSAALT UG: ").split()))
# target = int(input("Toogoo oruul: "))
# print(search_insert(nums, target))



# 14. Хэрэглэгчээс тоо авч, түүнээс **бага** хамгийн ойр тоог 
#     Binary Search-ийн логик ашиглан ол. Ийм тоо байхгүй бол `Байхгүй` гэж хэвлэ.
# def find_closest_smaller(nums, target):
#     left = 0
#     right = len(nums) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] < target:
#             result = nums[mid]
#             left = mid + 1
#         else:
#             right = mid - 1
#     if result == -1:
#         return "Байхгүй"
#     return result
# nums =  list(map(int,input("JAGSAALT UG: ").split()))
# target = int(input("Toogoo oruul: "))
# print(find_closest_smaller(nums, target))



# 16.  Хэрэглэгчээс `a`, `b` гэсэн хоёр тоо авч, тус бүрийг Binary Search 
#      ашиглан хай. Олдсон тоо бүрийн индексийг хэвлэ.
# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# nums = [1, 3, 5, 7, 9, 11, 13]
# a = int(input("a = "))
# b = int(input("b = "))
# print("a index:", binary_search(nums, a))
# print("b index:", binary_search(nums, b))


# 17.  Жагсаалт **буурах** дарааллаар эрэмбэлэгдсэн. Энэ нөхцөлд
#      зөв ажиллах Binary Search бич.
# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# nums = list(map(int,input("JAGSAALT UG: ").split()))
# target = int(input("Haih too: "))
# print(binary_search(nums, target))




# 18.  `binary_search(numbers, target)` нэртэй функц бич.
#       - Тоо олдвол индексийг буцаана.
#       - Олдохгүй бол `-1` буцаана.
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# numbers = list(map(int,input("JAGSAALT UG: ").split()))
# target = int(input("HAIH TOO UG: "))
# print(binary_search(numbers,target))   
   


 
# 19. Хэрэглэгчээс тоо авч, тухайн тоо жагсаалтад хэдэн удаа байгааг ол. Binary Search 
#     ашиглан эхний болон сүүлийн байрлалыг тодорхойлж бод.
# def first_position(nums, target):
#     left = 0
#     right = len(nums) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             result = mid
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# def last_position(nums, target):
#     left = 0
#     right = len(nums) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             result = mid
#             left = mid + 1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# nums = list(map(int, input("Toonuudaa oruul: ").split()))
# target = int(input("Haih too: "))
# first = first_position(nums, target)
# last = last_position(nums, target)
# if first == -1:
#     print("Oldsongui")
# else:
#     count = last - first + 1
#     print("Ehnii bairlal:", first)
#     print("Suuliin bairlal:", last)
#     print("Davhardsan too:", count)
   



# 20.
# numbers = list(map(int, input("Toonuudaa oruul: ").split()))
# target = int(input("Haih too: "))

# # Linear Search
# linear_count = 0
# for i in range(len(numbers)):
#     linear_count += 1

#     if numbers[i] == target:
#         linear_index = i
#         break
# else:
#     linear_index = -1


# # Binary Search

# left = 0
# right = len(numbers) - 1
# binary_count = 0
# binary_index = -1
# while left <= right:
#     mid = (left + right) // 2
#     binary_count += 1
#     if numbers[mid] == target:
#         binary_index = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print("Linear Search:")
# print("Index:", linear_index)
# print("Shalgasan too:", linear_count)
# print("Binary Search:")
# print("Index:", binary_index)
# print("Shalgasan too:", binary_count)
# if linear_count < binary_count:
#     print("Linear Search iluu hurdan")
# elif binary_count < linear_count:
#     print("Binary Search iluu hurdan")
# else:
#     print("Adilhan shalgalt hiisen")



