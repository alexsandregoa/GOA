#if აღნიშნავს ფუნქცია რომელიც რომელიც ცალკე სხვა მითითებულ input-ის სახელზე სხვა პასუხს გამოიტანს მაგალითად
age = int(input("Enter your age: "))
if age > 18:
    print("big man")
else:
    print("kid")
print(                         )
#if აღნიშნავს ფუნქცია რომელიც რომელიც ცალკე სხვა მითითებულ input-ის სახელზე სხვა პასუხს გამოიტანს მაგალითად
#elif else და if-ის გაერთინაბული ფუნქციაა
#elif else-თვის if-ში
#თუ if აღნიშნავს ფუნქცია რომელიც რომელიც ცალკე სხვა მითითებულ input-ის სახელზე სხვა პასუხს გამოიტანს მაშინ else აღნიშავს ფუნქციას,რომელიც სხვა პასუხს გამოიტანს თუ input-ში if-ის პასუხს არ ჩავწერთ
print(                            )
age = int(input("Enter your age: "))
if age > 18:
    print("University")
elif age > 7:
    print("School")
else:
    print("Kindergarten")
print(                             )
grade = int(input("Enter your grade: "))
if grade > 100:
    print("A group")
elif grade < 80 and grade > 99:
    print("B group")
else:
    print("D or C")
print(                             )
name = input("Enter your name: ")
if name != "a" and name != "e" and name != "i" and name != "o" and name != "u" and name != "y":
    print("name without Vowels")
else:
    print("name with Vowels")
print(                                )
age = int(input("Enter your age: "))
if age+40 > 40:
    print("You are old")
else:
    print("You will be old soon")