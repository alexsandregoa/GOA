# and -> and ოპერატორობაში ორი ოპერატ მოკლე მაგალითად ორივე პირობა არის True (მართალია) და მაშინ გამოიტანს True 
# False მაშინ გამომიტანს False მაგალითად

print(True and True)  # True
print(True and False) # False
print(False and False) # False
print(False and True) # False

# or -> or ოპერატორის შემთხვევაში თუ ერთი პირობა მაინც არის True (მართალი) და იქედან გამოიტანს True,
# თუ კი ორივე პირობა არიყვს False (მცდარი) მაშინ იმ შემთხვევაშიც გამოიტანს False ს

print(True or True)   # True
print(True or False)  # True
print(False or False) # False
print(False or True) # True
print(                                  )
print(15>3 or 15<3)#or აღნიშნავს ან მაგალიტად იგივეა რაც მე გარეთ არ გავალ თუ არ იწვიმებს ან არ იქნება სეტყვა
print(                                               )
print(15>4 or 15 <9 and 12 > 3 or 0<19)#ტერმილალში გამოვა True