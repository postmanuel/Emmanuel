# # # # # # # # # java = input("enter java score")
# # # # # # # # # python = input("enter python score")
# # # # # # # # #
# # # # # # # # # total = float(java) + float(python)
# # # # # # # # # print(total)
# # # # # # # # #
# # # # # # # # # print("")
# # # # # # # # #
# # # # # # # # # num = 45
# # # # # # # # # num_sqrt = num ** 0.5
# # # # # # # # # print(num_sqrt)
# # # # # # # # import random
# # # # # # # #
# # # # # # # # print(random.randint(0, 32))
# # # # # # # #
# # # # # # # # x = 33
# # # # # # # # y = 12 * 0.622
# # # # # # # # team = x
# # # # # # # # x = y
# # # # # # # # y = team
# # # # # # # # print(f"the value of x  : {x}")
# # # # # # # #
# # # # # # # # print(f"the value of y: {y} ")
# # # # # # #
# # # # # # # # year = input("Enter a year")
# # # # # # # # #nnif(year % 4) == 0:
# # # # # # # #     if(year % 100) == 0:
# # # # # # # #         if(year % 400) ==0:
# # # # # # # #             print("that is a leap year ".format(year))
# # # # # # # #         else:
# # # # # # # #             print(" that's not a leap year".format(year))
# # # # # # #
# # # # # # # # num = 12
# # # # # # # # for i in range(1,21):
# # # # # # # #     print(num, "x", i, "=", num * i)
# # # # # # #
# me = 10
# # # # # # # #
# for i in range (1,13):
#     print(me, "+", i, "=", me + i)
import time
import unittest
from audioop import add


# # # # # # #
# # # # # # numbers = [1, 2, 3, 4, 5]
# # # # # # sum = 0
# # # # # #
# # # # # # for num in numbers:
# # # # # #     sum += num
# # # # # #
# # # # # # print("Sum:", sum)
# # # # #
# # # # # numbers = [1, 2, 3, 4, 5]
# # # # # sum =0
# # # # # index = 0
# # # # #
# # # # # while index < len(numbers):
# # # # #     sum += numbers[index]
# # # # #     index += 1
# # # # #
# # # # # print(sum)
# # # #
# # # # hymns = ["Rugged Cross", "Calvary", "Assurance", "Zion"]
# # # #
# # # # minister = ["Boakye", "Sowah", "Obed", "Cosmos", "Nine"]
# # # #
# # # # elder = []
# # # #
# # # # print(hymns.index("Zion"))
# # # # print(hymns[0:3])
# # # # print(hymns[-4:-1])
# # # # print(len(hymns))
# # # # print(len(minister))
# # # # hymns.append("Higher Ground")
# # # # hymns.extend(minister)
# # # # hymns[2:2] = ["Argument", "Ancient word"]
# # # # hymns[1:2] = ["Rock of Ages", "What A Saviour"]
# # # # hymns.sort()
# # # # hymns.sort(key=str.upper)
# # # # print(hymns)
# # # #
# # #
# # # choir = {
# # #         "Vocal singers": "Christian singer",
# # #         "Harmonious": "Kwan pa"
# # # }
# # #
# # # print(choir)
# #
# # for x in range(0,100,10):
# #     print(x)
# #
# #
#
# names = ["Postmanuel", "Pabi", "Khalifa"]
# actions = ["Eat", "Code", "Sleep"]
# for x in names:
#     for y in actions:
#         print(x + " " + y + " 😂")
#
#

# def sum(l, b):
#     print(+l + b)
#
#
# sum(+34, 45)

# def multiple(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#     multiple("Abraham", "Samuel", "Job")


# arr = [1,4,5,2,3,5,8]
# if 9 not in arr:
#     pass
# else:
#     print("wrong")
#
#
# Age = 23
#
# if Age < 18:
#  print("Welcome")

# name = input( "Enter name" )
# Age = int( input( "Enter age" ) )
#
# if name == "James":
#     print( "Login successfully" )

# day = "Sunday"
#
# match day:
#     case "Sunday":
#         print("Have a great Church Service")
#     case "Monday":
#         print("Have a great Monday!")
#     case "Tuesday":
#         print("Have a great Tuesday!")
#     case "Wednesday":
#         print("Have a great Wednesday!")
#     case "Thursday":
#         print("Have a great Thursday")
#     case "Friday":
#         print("Have a great Friday")
#     case _:
#         print("Have a great day!")

# user_input = input("Enter a number: ")
#
# match user_input:
#     case  1:
#         print("The number is positive.")
#     case -1:
#         print("The number is negative.")
#     case 0:
#         print("The number is zero.")
#     case _:
#         print("Invalid input.")
# fa = "good morning"
#
# names = [" James", " Scarlett", " Emmanuel", " Hanna", " Claudia", " Alhaji"]
#
# for i_item in names:
# print(fa  + i_item)

# Iterate over a list of numbers and print the square of each number

#
# names = ["Matthew",  "Luke", "John"]
# actions = ["Code", "Eat", " Pray ", "Sleep"]
#
#
# # for action in actions:
# #         for name in names:
# #            print(name + " " + action)
#
# # Print the numbers from 1 to 10, but skip the even numbers
# # i = 9
# # while i <= 10:
# #     # if i % 2 == 0:
# #     #     continue
# #     time.sleep(1)
# #     print(i)
# #     i += 1
# #
# # else:
# #     print("the loop is finish")
# # # for i in range(10):
# # #     if i > 5:
# # #         break
# # #     print(i)
# # i = 10
# # while True:
# #  break
# #  print("the number is " + format(i))
# #  i+=1
#
# def average(numbers):
#
#   sum = 0
#   for number in numbers:
#     sum += number
#   return sum / len(numbers)
#
# # Example usage:
#
# numbers = [1, 2, 3, 4, 5]
# print(average(numbers))
#
# def add(x, y):
#
#   return x + y
#
# # Example usage:
#
# print(add(-134, 23))
#
# import unittest
#
# def add(a, b):
#     return a + b

#
# class TestAddFunction( unittest.TestCase ):
#     def test_add_two_positive_numbers(self):
#         self.assertEqual( add( 1, 2 ), 3 )
#
#     def test_add_two_negative_numbers(self):
#         self.assertEqual( add( -1, -2 ), -3 )
#
#     def test_add_zero_to_a_number(self):
#         self.assertEqual( add( 0, 10 ), 10 )
#
#
# if __name__ == '__main__':
#     unittest.main()


# f = open("my_file.txt", "w")
# f.write("This is a line of text.")
# print(f)
# f.close()

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed")
except TypeError:
    print("Invalid operation type")
except:
   print("An unknown error occurred")
