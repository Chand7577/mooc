from datetime import datetime


def get_difference(start_time, end_time):
    time_format = "%H:%M"
    start_time = datetime.strptime(start_time, time_format)
    end_time = datetime.strptime(end_time, time_format)
    
    time_difference = abs(start_time - end_time)
    total_seconds = int(time_difference.total_seconds())
    
    return total_seconds


def cheaters():
  
    cheaters=set()

    # Read start times data
    with open('start_times.csv') as file1:
        start_times = {}
        for line in file1:
            line = line.strip().split(";")
            name = line[0]
            start_time = line[1]
            start_times[name] = start_time
    
        
 
    with open('submissions.csv') as file2:
        for line in file2:
            line = line.strip().split(";")
            name = line[0]  
            end_time = line[-1] 
            
            # Check if start time is available for the student
            if name in start_times:
                start_time = start_times[name]
              
                if get_difference(start_time, end_time) > 10800:
                    cheaters.add(name)
    
   
    return list(cheaters)

if __name__ == "__main__":
    print(cheaters())
