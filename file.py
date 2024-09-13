import os

people = []

# Directory containing subdirectories of people's images
DIR = '/home/karthik/opencv/people/'

# Populate the `people` list with names (directories)
for person in os.listdir(DIR):
    if os.path.isdir(os.path.join(DIR, person)):  # Ensure it's a directory
        people.append(person)



print(people)