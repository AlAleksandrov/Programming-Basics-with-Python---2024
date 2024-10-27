budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
rams_count = int(input())

price_video_card = 250
price_processor = video_cards_count * price_video_card * 0.35
price_ram = video_cards_count * price_video_card * 0.1

discount = 0.0
if video_cards_count > processors_count:
    discount = 0.15

price_all = video_cards_count * price_video_card + processors_count * price_processor + rams_count * price_ram
price_all *= (1-discount)

if budget >= price_all:
    price_left = budget - price_all
    print(f'You have {price_left :.2f} leva left!')
else:
    price_needed = price_all - budget
    print(f'Not enough money! You need {price_needed :.2f} leva more!')
