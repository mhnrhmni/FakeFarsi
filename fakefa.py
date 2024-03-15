import random


# Function to read names from a file
def read_names(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


# Function to read last names from a file
def read_last_names(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().split("  \n  \n")


# Function to generate a fake first name
def fake_name():
    print(random.choice(names).strip())


# Function to generate a fake last name
def fake_last_name():
    print(random.choice(last_names))


# Function to generate a fake full name
def fake_full_name():
    full_name = random.choice(names).strip() + " " + random.choice(last_names)
    print(full_name)


# Read names from a file
names = read_names('اسامی.txt')

# Read last names from a file
last_names = read_last_names('نام خانوادگی.txt')

fake_last_name()
fake_name()
fake_full_name()