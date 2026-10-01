# Name =(input("Enter your name: "))

# print(f"Good Afternoon, {Name}")


# letter = '''Dear <|Name|>,
# \tyou are selected!
# \t<|Date|>'''
# print(letter.replace("<|Name|>","SYED AARIZ").replace("<|Date|>", "19 Aug 2026"))


# Name = syed  aariz latief
# print()

# fruits = []
# f1 = input("Enter your fruit: ")
# fruits.append(f1)
# f2 = input("Enter your fruit: ")
# fruits.append(f2)
# f3 = input("Enter your fruit: ")
# fruits.append(f3)
# f4 = input("Enter your fruit: ")
# fruits.append(f4)
# f5 = input("Enter your fruit: ")
# fruits.append(f5)
# f6 = input("Enter your fruit: ")
# fruits.append(f6)
# f7 = input("Enter your fruit: ")
# fruits.append(f7)

# print(fruits)



# marks = []
# f1 = int(input("Enter marks: "))
# marks.append(f1)
# f2 = int(input("Enter marks: "))
# marks.append(f2)
# f3 = int(input("Enter marks: "))
# marks.append(f3)
# f4 = int(input("Enter marks: "))
# marks.append(f4)
# f5 = int(input("Enter marks: "))
# marks.append(f5)
# f6 = int(input("Enter marks: "))
# marks.append(f6)
# f7 = int(input("Enter marks: "))
# marks.append(f7)
# marks.sort()

# print(marks)

# type = ( 45,65,"aariz")
# type(4) = "aahib"

# numbers = (35,56,78,23)
# print(sum(numbers))

# a = (8,0,0,4,5,0,6,0,7,0,)
# s = a.count(0)
# print(s)


# words = {
#     "kursi" : "chair",
#     "insan" : "human",
#     "angoor" : "grapes"
# }

# word = input("Enter word: ")
# print(words[word])


# d = {}
# name = input("Enter your name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})
# name = input("Enter your name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})
# name = input("Enter your name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})
# name = input("Enter your name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})
# print(d)

# a = int(input("Enter your age: "))
# if(a>=18):
#     print("yes")
# elif(a==0):
#     print("invalid age")
# else:
#     print("no")


# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1: ",a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2: ",a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest number is a3: ",a3)

# elif(a4>a1 and a4>a3 and a4>a2):
#     print("Greatest number is a4: ",a4)



# username = input("Enter you username :")

# if(len(username)<10):
#     print("Your username contains less than 10 characters")

# else:
#     print("All is well")


# l = ["Aariz" , "Aahib" , "Zehran" , "Ammar"]

# name = input("Enter your nam: ")

# if(name in l):
#     print("You are in list")

# else:
#     print("You are not in the list")


# marks = int(input("Enter your marks: "))

# if((marks<=100) and (marks>=90)):
#     print("Grade = Ex")
# elif((marks<=89) and (marks>=80)):
#     print("Grade = A")
# elif((marks<=79) and (marks>=70)):
#     print("Grade = B")
# elif((marks<=69) and (marks>=60)):
#     print("Grade = C")
# elif((marks<=59) and (marks>=50)):
#     print("Grade = D")
# elif((marks<=49)):
#     print("Grade =F")


# import pyjokes
# joke = pyjokes.get_joke()

# print(joke)



# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)


# n = int(input("Enter your number: "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")


# l = ["Harry", "Soham", "Sachin", "Rahul"]
# name = input("Enter your name: ")
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")


# n = int(input("Enter your number: "))
# i = 1
# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1


# n = int(input("Enter your number: "))
# for i in range(2,n):
#     if(n%i) == 0:
#         print("This number is not prime")
#         break
# else:
#     print("This number is prime")


# n = int(input("Enter your number: "))
# i = 1
# sum = 0
# while(1<=n):
#     sum += i
#     i += 1
# print(sum)


# n = int(input("Enter your number: "))
# product = 1
# for i in range(1,n+1):
#     product = product * i
# print(f"The factorial of {n} is {product}")


# n = int(input("Enter your number: "))
# i = 1
# for i in range(1,11):
#     print(f"{n} X {11-i} = {n *(11-i)}")
    


# arr = [10,20,30,40,50,60,70,80,90,100]
# for i in range(-10,7):
#     print(arr[i])



# n = int(input("Enter your number: "))
# for i in range(1 , n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#         print("\n", end="")
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("\n", end="")
#     print("")




#  CHAPTER 8
#  CHAPTER 8
#  CHAPTER 8
#  CHAPTER 8
#  CHAPTER 8
#  CHAPTER 8
#  CHAPTER 8
#  CHAPTER 8

# FUNCTION DEFINITON
# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))

#     average = (a + b + c)/3
#     print(average)
# avg() #FUNCTION CALL
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# print("Thank you")
# avg()
# print("Thank you")


# def goodDay():
#     print("Good Day")
# goodDay()


# def goodDay(name, ending):
#     print("Good Day," + name)
#     print(ending)

# goodDay("AARIZ" , "Thank You")


# def goodDay(name, ending):
#     print("Good Day," + name)
#     print(ending)
#     return "ok"
#     #return ka kaam hai "a" ki value ko decide krna yaha par hm ne "a" ki value "ok" rakhi

# a = goodDay("AARIZ" , "Thank You")
# print(a).


# def goodDay(name, ending="Thank You"):
#     print(f"Good Day , {name}")
#     print(ending)

# goodDay("Aariz")


'''
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x n-1 x......3 x 2 x 1
factorial(n) = n * factorail(n-1)
'''
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter your number: "))
# print(f"The factorial of this number is: {factorial(n)}")

#PROJECT 1
#PROJECT 1
#PROJECT 1
#PROJECT 1
#PROJECT 1
#PROJECT 1
#PROJECT 1


''' 1 for  snake
-1 for water
0 for gun '''

# import random
# computer = random.choice([-1,0,1])
# youstr = input("Enter your choice: ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# you = youDict[youstr]

# print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Its a draw")

# else:
#     if(computer ==-1 and you == 1):
#         print("You Win!")

#     elif(computer == -1 and you == 0):
#         print("You Lose!")

#     elif(computer == 1 and you == -1):
#         print("You Lose!")

#     elif(computer == 1 and you == 0):
#         print("You Lose!")

#     elif(computer == 0 and you == -1):
#         print("You Lose!")

#     elif(computer == 0 and you == 1):
#         print("You Lose!")

#     else:
#         print("Something went wrong!")

'''OR/OR/OR/OR/OR/OR/OR/OR'''

# import random
# computer = random.choice([-1,0,1])
# youstr = input("Enter your choice: ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# you = youDict[youstr]

# print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# if(computer == you):
#     print("Its a draw")

# # else:
# #     if(computer ==-1 and you == 1): (computer - you)= -2
# #         print("You Win!")

# #     elif(computer == -1 and you == 0): (computer - you)=-1
# #         print("You Lose!")

# #     elif(computer == 1 and you == -1): (computer - you)=2
# #         print("You Lose!")

# #     elif(computer == 1 and you == 0): (computer - you)=1
# #         print("You Lose!")

# #     elif(computer == 0 and you == -1): (computer - you)=1
# #         print("You Lose!")

# #     elif(computer == 0 and you == 1): (computer - you)=-1
#         # print("You Lose!")

# else:
#     if((computer - you) == -1 or (computer -you) == 2):
#         print("you lose!")
#     else:
#         print("you win!")



# CHAPTER 9 -FILE IO
# CHAPTER 9 -FILE IO
# CHAPTER 9 -FILE IO
# CHAPTER 9 -FILE IO
# CHAPTER 9 -FILE IO


f = open("file.txt")
data = f.read()
print(data)
f.close()














































