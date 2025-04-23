# Write your solution here
import json


def menu():
    print('0 quit')
    print('1 search for player')
    print('2 teams')
    print('3 countries')
    print('4 players in team')
    print('5 players from country')
    print('6 most points')
    print('7 most goals')


def getName(datas: dict):
    name = input("name:")
    info = datas[name]
    team = datas[name]['team']
    assists = datas[name]['assists']
    goals = datas[name]['goals']
    print()
    print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {assists + goals:>3}")
    print()


def getTeams(datas: dict):
    teams = sorted(set([datas[data]['team'] for data in datas]))

    for team in teams:
        print(team)

    print()


def getCountries(datas: dict):
    countries = sorted(set([datas[data]['nationality'] for data in datas]))
    print()
    for country in countries:
        print(country)

    print()


def getPlayersInTeam(datas: dict):
    user_team = input('team:')
    print()
    grouped_teams = {data: datas[data] for data in datas if datas[data]['team'] == user_team}
    points = []
    for team in grouped_teams:
        assists = grouped_teams[team]['assists']
        goals = grouped_teams[team]['goals']
        points.append((assists + goals, team))

    for point in sorted(points, reverse=True):
        name = point[1]
        assists = grouped_teams[point[1]]['assists']
        goals = grouped_teams[point[1]]['goals']
        print(f"{name:<20} {user_team:>3} {goals:>3} + {assists:>2} = {assists + goals:>3}")

    print()


def getPlayersFromCoun(datas: dict):
    country = input('country:')
    print()
    grouped_teams = {data: datas[data] for data in datas if datas[data]['nationality'] ==country}
    points = []

    for team in grouped_teams:
        assists = grouped_teams[team]['assists']
        goals = grouped_teams[team]['goals']
        
        points.append((assists + goals, team))

    for point in sorted(points, reverse=True):
        name = point[1]
        country_=grouped_teams[point[1]]['team']
        assists = grouped_teams[point[1]]['assists']
        goals = grouped_teams[point[1]]['goals']
        print(f"{name:<20} {country_:>3} {goals:>3} + {assists:>2} = {assists + goals:>3}")

    print()


def getMostpoints(datas: dict):
    players=int(input("how many:"))
    grouped_teams = {data: datas[data] for data in datas }
    points = []
   
    for team in grouped_teams:
        assists = grouped_teams[team]['assists']
        goals = grouped_teams[team]['goals']
        
        points.append((assists + goals, team))

    for point in sorted(points, reverse=True)[:players]:
        
        name = point[1]
        country_=grouped_teams[point[1]]['team']
        assists = grouped_teams[point[1]]['assists']
        goals = grouped_teams[point[1]]['goals']
        print(f"{name:<20} {country_:>3} {goals:>3} + {assists:>2} = {assists + goals:>3}")

    print()



def getMostGoals(datas: dict):
    players=int(input("how many:"))
    grouped_teams = {data: datas[data] for data in datas }
    
    players_data=[]
    for team in grouped_teams:
        assists = grouped_teams[team]['assists']
        goals = grouped_teams[team]['goals']
        games=grouped_teams[team]['games']
        team_=grouped_teams[team]['team']
        name=team
        
        players_data.append(( goals,games,assists,team_,name))


    
  
    for i in range(players):
        goals,games,assists,team,name = sorted(players_data,key=lambda player:(-player[0],player[1]))[i]
        print(f"{name:<20} {team:>3} {goals:>3} + {assists:>2} = {goals + assists:>3}")
    
    print()


def main():
    filename = input("filename:")

    with open(filename) as file:
        datas = json.load(file)
        datas = {data['name']: {key: value for key, value in data.items() if key != "name"} for data in datas}

    print(f"read the data of {len(datas)} players")
    print()
    print('commands:')
    menu()
    print()

    while True:
        command = int(input("command:"))
        if command == 1:
            getName(datas)

        elif command == 2:
            getTeams(datas)

        elif command == 3:
            getCountries(datas)

        elif command == 0:
            break

        elif command == 4:
            getPlayersInTeam(datas)

        elif command == 5:
            getPlayersFromCoun(datas)

        elif command == 6:
            getMostpoints(datas)

        elif command == 7:
            getMostGoals(datas)


main()
