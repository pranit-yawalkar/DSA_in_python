jan_temp = []

with open("nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(",")
        try:
            temp = int(tokens[1])
            jan_temp.append(temp)
        except:
            print("Invalid temp, ignore it!")
print(jan_temp)
print(sum(jan_temp[:7])/len(jan_temp[:7]))
print(max(jan_temp[:10]))

jan_temp = {}
with open("nyc_weather.csv") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        try:
            temp = int(tokens[1])
            jan_temp[day] = temp
        except:
            print("Invalid tmep! Ignore it!")

print(jan_temp)
print(jan_temp["9-Jan"])
print(jan_temp["4-Jan"])
