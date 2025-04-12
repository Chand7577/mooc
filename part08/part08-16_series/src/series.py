# Write your solution here:
class Series:
    def __init__(self,title,seasons,genres):
        self.title=title
        self.seasons=seasons
        self.genres=genres
        self.ratings=[]

    
    def __str__(self):
        if len(self.ratings)==0:
            string_value="no ratings"
        else:
            string_value=f"{len(self.ratings)} ratings, average {round(sum(self.ratings)/len(self.ratings),1)} points"
        return (f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{string_value}")
    

    def rate(self,rating):
        self.ratings.append(rating)


def minimum_grade(rating:float,series_list:list):
        series=[]
        for current_serie in series_list:
            if current_serie.ratings[0]>=rating:
                series.append(current_serie)

        return series 

def includes_genre(genre:str,series_list:list):

        series=[]
        for current_serie in series_list:
            for current_genre in current_serie.genres:
                if current_genre==genre:
                    series.append(current_serie)

        return series

        
if __name__=="__main__":
    # s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # s1.rate(5)

    # s2 = Series("South Park", 24, ["Animation", "Comedy"])
    # s2.rate(3)

    # s3 = Series("Friends", 10, ["Romance", "Comedy"])
    # s3.rate(2)

    # series_list = [s1, s2, s3]

    # print("a minimum grade of 4.5:")
    # for series in minimum_grade(4.5, series_list):
    #     print(series.title)

    # print("genre Comedy:")
    # for series in includes_genre("Comedy", series_list):
    #     print(series.title)
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)
