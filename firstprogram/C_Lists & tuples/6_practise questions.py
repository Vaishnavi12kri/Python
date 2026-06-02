#1.wap to ask the user to enter names of their movies & store them in a list.
# movies = []
# mov1 = input("enter 1st movie: ")
# movies.append(mov1)
# mov2 = input("enter 2nd movie: ")
# movies.append(mov2)
# mov3 = input("enter 3rd movie: ")
# movies.append(mov3)

# print(movies)

#2nd method

# movies = []
# movies.append(input("enter 1st movie: "))
# movies.append(input("enter 2nd movie: "))
# movies.append(input("enter 3rd movie: "))
# print(movies)


# 2.wap to check if a list contains a palindrome of elements.(hints:use copy()methods)
#[1,2,3,2,1]  [1,"abc","abc",1]

list1 = [1,2,1]
list2 = [1,2,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")

# 3. wap to count the number of students with the "A"grade in the following tuple.
# ["C","D","A","B","B","A"]
grade = ["C","D","A","A","B","B","A"]
print(grade.count("A"))

#store the above values in a list & sort them from "A"to"D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)    