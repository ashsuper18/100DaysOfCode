# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nam1= name1.lower()
nam2 = name2.lower()

combinedname = nam1+nam2

t= combinedname.count("t")
r= combinedname.count("r")
u= combinedname.count("u")
e= combinedname.count("e")
sum1= t+r+u+e
l= combinedname.count("l")
o= combinedname.count("o")
v= combinedname.count("v")
e= combinedname.count("e")
sum2= (l+o+v+e)
vald = str(sum1)+str(sum2)
total = int(vald)
if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total<=60:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")




