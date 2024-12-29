# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59



seconds = int(input("Enter the number of seconds (от 0 до 8 639 999): "))

if not (0 <= seconds < 8640000):
    print("Error: number must be between 0 and 8 639 999.")
else:
    days, remaining_seconds = divmod(seconds, 24 * 60 * 60)
    hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)
    minutes, seconds = divmod(remaining_seconds, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дня"
    else:
        day_word = "дней"

    result = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(result)
