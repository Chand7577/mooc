import math
# Write your solution here



def get_station_data(filename:str):
    station_data={}

    with open(filename) as file:
            
            for line in file:
                line=line.strip().split(";")
                if line[0]=="Longitude":
                    continue
                
                station_data[line[3]]=(float(line[0]),float(line[1]))

    return station_data


def cal_distance(longitude1:int,latitude1:int,longitude2:int,latitude2:int):
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

     

def distance(stations:dict,station1:str,station2:str):

    long1=stations[station1][0]
    lat1=stations[station1][1]
    long2=stations[station2][0]
    lat2=stations[station2][1]

     
    
    return cal_distance(long1,lat1,long2,lat2)



def greatest_distance(stations:dict):
    distances={}
     
    for outerkey,value in stations.items():

        for key,value in stations.items():
            if outerkey!=key:
                d=distance(stations,outerkey,key)
                distances[d]=(key,outerkey)

    station1=distances[max(distances)][0]
    station2=distances[max(distances)][1]
    
    return(station1,station2,max(distances))

if __name__=="__main__":

    stations=get_station_data('stations1.csv')
    # d=distance(stations, "Designmuseo", "Hietalahdentori")
    # print(d)
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(d)

# for key,value in stations.items():
#     print(key,value)

    station1,station2,greatest=greatest_distance(stations)
    print(f"{station1} {station2} {greatest}")