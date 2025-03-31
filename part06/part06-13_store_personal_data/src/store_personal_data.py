# Write your solution here


def store_personal_data(person:tuple):
    with open('people.csv','a') as file:
        file.write(f"{person[0]};{person[1]};{person[2]}")


if __name__=="__main__":
    store_personal_data(("amrit",23,23.2))