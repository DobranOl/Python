sec = int(input('Input time in seconds: '))
minutes, seconds = divmod(sec, 60)
hours, minutes = divmod(minutes, 60)
print(f"Your time in hours:minutes:seconds is {hours:d}:{minutes:02d}:{seconds:02d}")
