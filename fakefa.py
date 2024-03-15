with open('اسامی.txt', 'r', encoding='utf-8') as f:
    name = f.read().splitlines()

with open('نام خانوادگی.txt', 'r', encoding='utf-8') as f:
    last_name = f.read().split("  \n  \n")

print(last_name)