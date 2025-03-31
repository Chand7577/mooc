# Write your solution here




username=input("Whom should i sign this to:")
fileName=input("Where shall i save it:")


with open(fileName,"w") as file:
    file.write(f"Hi {username}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")