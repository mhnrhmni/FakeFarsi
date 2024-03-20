import random


# Function to read names from a file
def read_names(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


# Function to read last names from a file
def read_last_names(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().split("  \n  \n")


# Function to generate a complete fake profile
def complete():
    f = fake_name()
    l = fake_last_name()
    n = f + " " + l
    a = fake_age()
    p = fake_phone()
    e = fake_email(f, l)
    s = f"نام و نام خانوادگی : {n} \nسن : {a} \nشماره تلفن : {p} \nایمیل : \n{e}"
    return s


# Function to generate a fake first name
def fake_name():
    return random.choice(names).strip()


# Function to generate a fake last name
def fake_last_name():
    return random.choice(last_names)


# Function to generate a fake full name
def fake_full_name():
    full_name = random.choice(names).strip() + " " + random.choice(last_names)
    return full_name


# Function to generate a fake age
def fake_age():
    return random.randint(10, 99)


# Function to generate a fake phone number
def fake_phone():
    phone_number = "09"
    index2 = ["1", "3", "9"]
    phone_number += random.choice(index2)
    for i in range(8):
        phone_number += str(random.randint(0, 9))
    return phone_number


# Function to translate Persian characters to English
def translator(text):
    mapping = {
        "آ": "a",
        "ا": "a",
        "ب": "b",
        "پ": "p",
        "ت": "t",
        "ث": "s",
        "ج": "j",
        "چ": "ch",
        "ه": "h",
        "خ": "kh",
        "د": "d",
        "ذ": "z",
        "ر": "r",
        "ز": "z",
        "س": "s",
        "ش": "sh",
        "ص": "s",
        "ظ": "z",
        "ط": "t",
        "ع": "a",
        "غ": "gh",
        "ق": "gh",
        "ف": "f",
        "ک": "k",
        "گ": "g",
        "ل": "l",
        "م": "m",
        "ن": "n",
        "و": "v",
        "ی": "i",
        "ء": "a",
        "ئ": "e",
        "ي": "i",
        "ح": "h",
        "ض": "z",
        "ك": "k"
    }

    for key, value in mapping.items():
        text = text.replace(key, value)

    return text


# Function to generate a fake email
def fake_email(name, lastname):
    email = translator(name) + translator(lastname) + str(random.randint(1, 999)) + "@gmail.com"
    return email.replace(" ", "")


# Read names from file
names = read_names('اسامی.txt')


# Read last names from file
last_names = read_last_names('نام خانوادگی.txt')
