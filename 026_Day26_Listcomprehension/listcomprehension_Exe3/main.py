
with open("026_Day26_Listcomprehension\listcomprehension_Exe3/file1.txt") as file1:
    f1data = file1.readlines()
    list1 = [int(number.strip()) for number in f1data]
# print(list1)


with open("026_Day26_Listcomprehension\listcomprehension_Exe3/file2.txt") as file2:
    f2data = file2.readlines()
    list2 = [int(number.strip()) for number in f2data]
# print(list2)


result = [n for n in list1 if n in list2]
# result = [int(num) for num in f1data if num in f2data]

print(result)
