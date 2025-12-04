import time

# Get the current time in seconds since the epoch
now = time.time()
now = int(now)  #don't need factions of seconds

# Calculate total seconds in a day
seconds_in_a_day = 24 * 60 * 60

# Find the number of seconds that have passed today
seconds_today = now % seconds_in_a_day

# Calculate the current hour, minute, and second
hours   = seconds_today // 3600
minutes = (seconds_today % 3600) // 60
seconds = seconds_today % 60

# Print the time in HH:MM:SS format
print(f"{hours:02}:{minutes:02}:{seconds:02}")