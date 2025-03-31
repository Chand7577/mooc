# Write your solution here



"""How many students on the course? 8
Desired group size? 4
Number of groups formed: 2"""

students=int(input("How many students on the course?"))
group_size=int(input("Desired group size?"))

groups=(students//group_size)+1 if (students%group_size)!=0 else (students//group_size)

print(f"Number of groups formed: {groups}")


