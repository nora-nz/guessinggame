n = 36
k = 2

rabbits = {
    "immature_rabbits": 1,
    "mature_rabbits": 0,
    "litter": 0
}

for generation in range(n - 1):

        rabbits["litter"] = rabbits["mature_rabbits"] * k
        rabbits["mature_rabbits"] = rabbits["mature_rabbits"] + rabbits["immature_rabbits"]
        rabbits["immature_rabbits"] = rabbits["immature_rabbits"] - rabbits["immature_rabbits"] + rabbits["litter"]

number_of_rabbits = rabbits["immature_rabbits"] + rabbits["mature_rabbits"]
print(number_of_rabbits)
