def mentes(name, password):
    with open('Users.txt', "a", encoding='utf-8') as file:
        file.write(name + ";" + password + "\n")

def log():
    with open('Users.txt', "r", encoding='utf-8') as file:
        for row in file:
            data = row.strip().split(';')
            return data