main = []
swapped = True 
sorter = int(input("how many numbers would you like to sort ? "))

for i in range(sorter):
    numbers = float(input("Enter number you want to sort: "))
    main.append(numbers)

while swapped:
    swapped = False 
    for i in range(len(main) -1):
        if main[i] > main[i + 1]:
            swapped = True 
            main[i], main[i + 1] = main[i + 1], main[i]

print (f"Sorted: {main}")
    