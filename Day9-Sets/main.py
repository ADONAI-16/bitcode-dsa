

#############################################################################

# SOME CHALLENGES

# 1, find duplicate numbers using sets
def has_duplicates(numbers):
    return len(numbers) == len(set(numbers))
print(has_duplicates([1,2,3,3,3,4,4,5]))
print(has_duplicates([1,2,3,4,5]))

# unique numbers part 2

def common_elts(a,b):
    unique= set(a) & set(b)
    return unique
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(common_elts(a,b))

# Hackerrank prboblem

def count_distinct_stamps(n):
    countries = set()

    for i in range(n):
        country = input()
        countries.add(country)

    return len(countries)


n = int(input())
print(count_distinct_stamps(n))