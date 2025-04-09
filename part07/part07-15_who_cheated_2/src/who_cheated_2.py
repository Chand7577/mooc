from datetime import datetime

# Function to calculate the difference between two times in seconds
def get_difference(start_time, end_time):
    time_format = "%H:%M"
    start_time = datetime.strptime(start_time, time_format)
    end_time = datetime.strptime(end_time, time_format)
    
    time_difference = abs(start_time - end_time)
    total_seconds = int(time_difference.total_seconds())
    
    return total_seconds


def final_points():
    students_info={}
    final_points={}

    # Read start times data
    with open('start_times.csv') as file1:
        
        for line in file1:
            line = line.strip().split(";")
            name = line[0]
            start_time = line[1]
            students_info[name]={}
            students_info[name]['start_time']=start_time
    
        
    # Read submissions data and match with start times
    with open('submissions.csv') as file2:
       

        for line in file2:
            line = line.strip().split(";")
            name = line[0] 
            current_task=line[1]
            point=line[2] 
            end_time = line[-1] 

            if 'submissions' not in students_info[name]:
                students_info[name]['submissions']={}

            start_time=students_info[name]['start_time']
            if get_difference(start_time,end_time)>10800:
                continue

            if current_task in students_info[name]['submissions']:
                if point<students_info[name]['submissions'][current_task]['point']:
                    continue
            
            data={
                "point":point
               
            }
            students_info[name]['submissions'][current_task]=data
            

    for name,data in students_info.items():
        points=0
        for value in data['submissions'].values():
            points+=int(value['point'])


        final_points[name]=points


    return final_points

       

if __name__=="__main__":
    print(final_points())
