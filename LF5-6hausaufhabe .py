with open("data.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        print(parts[0], parts[1])
