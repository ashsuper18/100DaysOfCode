import pandas
data = pandas.read_csv("Squirrel\Squirrel_Data.csv")
color_list = data["Primary Fur Color"].to_list()
gray = 0
cinnamon = 0
black = 0

for color in color_list:
    if color == "Gray" :
        gray +=1
    elif color =="Cinnamon":
        cinnamon +=1
    elif color == "Black":
        black +=1
# print(gray,cinnamon,black)
data_dict = {
    "color" : ["Gray" , "Cinnamon", "Black"],
    "Total" : [gray,cinnamon,black]
}
# print(data_dict)
new_table = pandas.DataFrame(data_dict)
new_table.to_csv("new_table.csv")