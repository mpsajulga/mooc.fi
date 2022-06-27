students = int(input("How many students on the course: "))
group_size = int(input("Desired group size? "))

groups_formed_even = students//group_size
groups_formed_odd = (students//group_size)+1

if (students % 2 == 0) and (group_size % 3 != 0):
    print(f"Number of groups formed: {groups_formed_even}")
else:
    print(f"Number of groups formed: {groups_formed_odd}")