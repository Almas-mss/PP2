from datetime import datetime

# Get the current datetime with microseconds
now = datetime.now()

# Remove microseconds
cleaned_now = now.replace(microsecond=0)

# Print results
print("Original datetime:", now)
print("Datetime without microseconds:", cleaned_now)
