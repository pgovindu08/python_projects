import pandas

colors = ["Gray","Cinnamon","Black"]

squirel_data = pandas.read_csv("Central_Park_Data.csv")
squirel_colors = squirel_data["Primary Fur Color"]

occurances = []

for color in colors:
    count_num = squirel_colors.value_counts()[f"{color}"]
    occurances.append(count_num)

csv_dic = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count": occurances
}

new_data = pandas.DataFrame(csv_dic)

new_data.to_csv("color_count.csv")



