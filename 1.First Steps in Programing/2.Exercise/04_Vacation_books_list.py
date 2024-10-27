all_pages_in_the_book = int(input())
pages_for_one_hour = int(input())
days_for_reading_the_book = int(input())

all_hours_for_reading_the_book = all_pages_in_the_book // pages_for_one_hour
total_hours_for_reading_a_book = all_hours_for_reading_the_book // days_for_reading_the_book


print(total_hours_for_reading_a_book)
