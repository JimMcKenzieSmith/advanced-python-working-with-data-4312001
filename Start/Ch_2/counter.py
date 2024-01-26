# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# TODO: How many students in class 1 named James?
print("Num students named James:",c1["James"])

# TODO: How many students are in class 1?
print("Number of students in class 1:",sum(c1.values()))
# for k,v in c1.items():
#     print(k,v)

# TODO: Combine the two classes
# c1.update(class2)
print("Number of students in combined:",sum(c1.values()))
c3_list = class1 + class2
c3 = Counter(c3_list)
print("Number of students in combined:",sum(c3.values()))
print("Number of students in combined:",len(c3_list))

# TODO: What's the most common name in the two classes?
print("Most common name:",c3.most_common(3))

# TODO: Separate the classes again
c3.subtract(class2)
print("Most common name:",c3.most_common(1))

# TODO: What's common between the two classes?
print(c1 & c2)
print(class1 & class2)