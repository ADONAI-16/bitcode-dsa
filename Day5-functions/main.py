def is_leap(year):
    leap = False
    # Why check 400 first?
# Some years (e.g., 2000) are divisible by 400, 100, and 4.
# If we check 100 first, Python would return False immediately,
# which would incorrectly classify 2000 as a non-leap year.
# Therefore, we start with the most specific condition (400),
# then check 100, and finally 4.
#
# Order:
# 400 -> True
# 100 -> False
# 4   -> True
# Else -> False
    if year % 400==0: 
        return True
        
    elif year % 100==0:
        return False
        
    elif year % 4==0:
        return True   
    else:
        return False
     
year = int(input("The year to test: "))
print(is_leap(year))

# Returns the total number of even numbers in the array

def count_even(numbers):

    count=0

    for num in numbers:
        if num % 2==0:
            count+=1
    return count

numbers = [2, 7, 4, 9, 8]

result = count_even(numbers)

print(result)