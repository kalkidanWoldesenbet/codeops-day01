# total = 1300
# number_of_employees = 3

def split_bill(total, people, tip_rate=0.10):
    total_with_tip= total + (total * tip_rate)
    per_person = total_with_tip / people
    return per_person

# employees = ["Abebe", "Almaz", "Kebede"]
# share = split_bill(total, number_of_employees)

# for name in employees:
#     print(f"{name}should pay {share:.2f} ETB")
bill_total = float(input("Enter the bill total in ETB: "))
number_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage (for example, 10 for 10%): ")) / 100

employees = []

for i in range(number_of_people):
    name = input(f"Enter name of employee {i + 1} : ")
    employees.append(name)

share = split_bill(bill_total, number_of_people, tip_percentage)

for name in employees:
    print(f"{name} should pay {share:.2f} ETB ")