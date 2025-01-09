import random
from data import male_names, female_names, l_names


class FakeFarsi:
    def __init__(self):
        self.names = male_names + female_names
        self.last_names = l_names

    def fake_name(self):
        """Generate a fake first name."""
        return random.choice(self.names).strip()

    def fake_last_name(self):
        """Generate a fake last name."""
        return random.choice(self.last_names)

    def fake_full_name(self):
        """Generate a fake full name."""
        return f"{self.fake_name()} {self.fake_last_name()}"

    def fake_age(self):
        """Generate a fake age."""
        return random.randint(10, 99)

    def fake_phone(self):
        """Generate a fake phone number."""
        phone_number = "09"
        index2 = ["1", "3", "9"]
        phone_number += random.choice(index2)
        for _ in range(8):
            phone_number += str(random.randint(0, 9))
        return phone_number

    def translator(self, text):
        """Translate Persian characters to English."""
        mapping = {
            "آ": "a", "ا": "a", "ب": "b", "پ": "p", "ت": "t", "ث": "s", "ج": "j", "چ": "ch", "ه": "h",
            "خ": "kh", "د": "d", "ذ": "z", "ر": "r", "ز": "z", "س": "s", "ش": "sh", "ص": "s", "ظ": "z",
            "ط": "t", "ع": "a", "غ": "gh", "ق": "gh", "ف": "f", "ک": "k", "گ": "g", "ل": "l", "م": "m",
            "ن": "n", "و": "v", "ی": "i", "ء": "a", "ئ": "e", "ي": "i", "ح": "h", "ض": "z", "ك": "k"
        }
        for key, value in mapping.items():
            text = text.replace(key, value)
        return text

    def fake_email(self, name, lastname):
        """Generate a fake email address."""
        email = self.translator(name) + self.translator(lastname) + str(random.randint(1, 999)) + "@gmail.com"
        return email.replace(" ", "")

    def generate_fake_profile(self):
        """Generate a complete fake profile."""
        f = self.fake_name()
        l = self.fake_last_name()
        n = f"{f} {l}"
        a = self.fake_age()
        p = self.fake_phone()
        e = self.fake_email(f, l)
        s = f"نام و نام خانوادگی : {n} \nسن : {a} \nشماره تلفن : {p} \nایمیل : \n{e}"
        return s


# Example usage
if __name__ == "__main__":
    generator = FakeFarsi()
    print(generator.generate_fake_profile())