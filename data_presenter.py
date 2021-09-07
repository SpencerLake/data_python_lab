open_file = open("CupcakeInvoices.csv")

for invoices in (open_file):
    print(invoices)

open_file.seek(0)

for flavs in open_file:
    flavs = flavs.rstrip('\n').split(",")
    print(flavs[2])

# open_file.seek(0)

# chocolate = 0
# vanilla = 0
# strawberry = 0

# for flavs in open_file:
#     flavs = flavs.rstrip('\n').split(",")
#     for total in flavs:
#         if total == "Chocolate":
#             chocolate += 1
#         elif total == "Vanilla":
#             vanilla += 1
#         elif total == "Strawberry":
#             strawberry += 1

# print("chocolate:", chocolate)
# print("Vanilla:", vanilla)
# print("Strawberry:", strawberry)

open_file.seek(0)

for line in open_file:
    # print(line)
    value = line.rstrip('\n').split(",")
    # print(value)
    total = int(value[3]) * float(value[4])
    print(total)

open_file.seek(0)

total = 0

for line in open_file:
    # print(line)
    value = line.rstrip('\n').split(",")
    # print(value)
    total += int(value[3]) * float(value[4])
    
print(total)


open_file.close()