import random
name = input("Give me everybody's name, seperated by comma and space : ")
names = name.split(", ")
# lenght_items = len(names)
# choose_random_name = random.randint(0,lenght_items-1)
# get_names = names[choose_random_name]
get_names = random.choice(names)
print(f"{get_names},is going to buy a meal")