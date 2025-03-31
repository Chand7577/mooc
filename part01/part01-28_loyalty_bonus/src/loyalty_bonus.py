# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points=(float(points*0.1)+points)

    print("Your bonus is 10 %")

else:
    points =(points*0.15)+points
    print("Your bonus is 15 %")

print("You now have", points, "points")