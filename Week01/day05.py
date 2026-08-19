# Basic Data Structures
# Lists are ordered and mutable
family = ["Father","Son","Daughter","Wife"]
print(family[-2]) #Right to Left
print(family[0])  #Left to Right
family.append("Grandmom")
family.remove("Grandmom")
family.pop()
print(family)
for family in family:
    print(family)

# Tuples are ordered by immutable
mat = (2,3)
print(2,3)

# Dictionaries are key value pairs
personal_data = {"name":"Jane","age":25,"Edu":"Engineer"}
print(personal_data)
personal_data["age"] = 34
personal_data["Company"] = "abc"
print(personal_data)
for key,value in personal_data.items():
    print(key,value)

# Set is unordered unique value only
set_test = {1,2,4,5,4,4} #removes duplicates
set_test1 = {1,2,4,5,6,4}
print(set_test & set_test1) # intersection
print(set_test - set_test1) # union
print(set_test | set_test1) # Difference