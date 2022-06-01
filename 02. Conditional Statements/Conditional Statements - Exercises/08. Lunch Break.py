from math import ceil

movie = input()
movie_len = int(input()) #60
break_len = int(input())

lunch_time = break_len / 8
rest_time = break_len / 4
time_for_movie = break_len - lunch_time - rest_time
difference = abs(movie_len - time_for_movie)

if movie_len <= time_for_movie:
    print(f"You have enough time to watch {movie} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie}, you need {ceil(difference)} more minutes.")