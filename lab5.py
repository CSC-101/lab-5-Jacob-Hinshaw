import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:data.Time, time2:data.Time) -> data.Time:
    time3 = data.Time(0,0,0)
    time3.hour = time1.hour + time2.hour
    time3.minute = time1.minute + time2.minute
    time3.second = time1.second + time2.second
    while time3.second > 59:
        time3.minute += 1
        time3.second -= 60
    return time3

# Part 4
def is_descending(input_list:list[float]) -> bool:
    for i in range(len(input_list)-1):
        if input_list[i] < input_list[i+1]:
            return False
    return True

# Part 5
#def largest_between

# Part 6
