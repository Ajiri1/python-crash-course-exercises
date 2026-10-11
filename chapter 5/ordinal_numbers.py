numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

for number in numbers:
    if number == 1:
        ordinal = "st"
    elif number == 2:
        ordinal = "nd"
    elif number == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    
    print(str(number) + ordinal)