user_input = input("Enter the number of seconds (from 0 to 8640000): ")

number = int(user_input)
if 0 <= number < 8640000:
    days, remainder = divmod(number, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    day_word = "day" if days == 1 else "days"
    print(f"{days} {day_word} {hours_str}:{minutes_str}:{seconds_str}")

else:
    print("Error: The number must be within the range from 0 to 8640000.")
