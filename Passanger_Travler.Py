print("\t\t\t\t\t-----------------------------------")
print("\t\t\t\t\t\tWelcome to Red Bus")
print("\t\t\t\t\t-----------------------------------")
travelling_Pasanger = input("Do you Travel in this Bus, Yes or No: ")
travelers = []

while travelling_Pasanger.lower() == "yes":
    num = int(input("\n\tInter The Number of people Traveling: "))

    for _ in range(1, num + 1):
        Pasanger_name = input("\tName: ")
        age = int(input("\tAge: "))
        Gender = input("\tMale or Female: ")
        print("\t\t\t\tNext Pasanger name")
        print("\n")

        traveler = {"Name": Pasanger_name, "Age": age, "Gender": Gender}
        travelers.append(traveler)

    travelling_Pasanger = input("Do you Add More Pasanger? (Yes/No): ")

print("\nFinal Travel Results:")
for index, traveler in enumerate(travelers, start=1):
    print(f"\t\tTraveler {index}:")
    print(f"\t\tName: {traveler['Name']}")
    print(f"\t\tAge: {traveler['Age']}")
    print(f"\t\tGender: {traveler['Gender']}")
    print("\n")