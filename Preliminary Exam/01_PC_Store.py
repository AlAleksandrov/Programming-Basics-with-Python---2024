usd_price_processor = float(input())
usd_price_video_card = float(input())
usd_price_ram_memory = float(input())
count_ram_memory = int(input())
discount_percentage = float(input())

total_price_ram_memory = usd_price_ram_memory * count_ram_memory
total_price = (total_price_ram_memory + (usd_price_processor + usd_price_video_card) * (1 - discount_percentage)) * 1.57

print(f"Money needed - {total_price:.2f} leva.")
