
# Write your solution here:
def order_by_ratings(programme:dict):
    return programme['rating']



def sort_by_ratings(shows:list):

    sorted_by_rat=sorted(shows,key=order_by_ratings,reverse=True)
    return sorted_by_rat



if __name__=="__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]
    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")
