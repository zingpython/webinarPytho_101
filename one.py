large_dep = 0.25
small_dep = 0.10

large = float(input("How many large btls do you have:"))
# print(type(large))
small = float(input("How many small btls do you have:"))

refund = (large_dep*large)+(small_dep*small_dep)
print(refund)