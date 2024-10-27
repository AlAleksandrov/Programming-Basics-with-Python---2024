import math

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_one_meter = float(input())

water_resistance = (math.floor(distance_in_meters / 15) * 12.5)

swimming_seconds = distance_in_meters * seconds_for_one_meter + water_resistance

if swimming_seconds < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {swimming_seconds :.2f} seconds.')
else:
    seconds_left = swimming_seconds - record_in_seconds
    print(f'No, he failed! He was {seconds_left :.2f} seconds slower.')
