import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# This function takes two inputs of class Time and adds them together, being sure that seconds don't exceed 60,
# and returns the total as class Time
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
# This function checks if the input (of list[float]) has the float values ordered from highest to lowest and
# returns a boolean value.
def is_descending(input_list:list[float]) -> bool:
    for i in range(len(input_list)-1):
        if input_list[i] < input_list[i+1]:
            return False
    return True

# Part 5
def largest_between(input_list:list[int], lower:int, upper:int) -> any:
    if lower < 0 or upper < 0 or upper < lower:
        return None
    bignum = float("-inf")
    bigidx = None
    for idx in range(lower, upper):
        if input_list[idx] > bignum:
            bignum = input_list[idx]
            bigidx = idx
    return bigidx


    #result = 0
    #idx = 1
    #for num in input_list:
    #    if num < input_list[idx] and upper >= idx >= lower:
    #        result = idx - 1
    #    idx += 1

# Part 6
# This function takes an input of list[Point] and finds the point which is furthest from (0,0) and returns it's
# index from the list.
def furthest_from_origin(input_list:list[data.Point]) -> any:
    if not input_list:
        return None
    maxpoint = float("-inf")
    maxidx = None
    #for point in input_list:
    for idx, point in enumerate(input_list):
        pointdist = (point.x**2 + point.y**2)**0.5
        if pointdist > maxpoint:
            maxpoint = pointdist
            maxidx = idx
    return maxidx