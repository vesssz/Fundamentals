
counter_succcess = 0

def check_name(name):
    check = False
    if len(name) >= 3:
        if name[0].isupper():
            check = True
            for i in name[1:]:
                if i.isupper():
                    check = False
    return check


def check_password(password):
    result = True
    for i in password[:5]:
        if not i.isalpha():
            result = False
    if password[-1].isalpha():
        result = False
    return result

n = int(input())


for _ in range(n):
    if_success = True
    line = input()
    if line[:2] == "U$" and line[-3:] == "P@$":
        striped = line[2:-3]
        if "U$P@$" in striped:
            tokens = striped.split("U$P@$")
            name = tokens[0]
            password = tokens[1]
            if check_password(password) and check_name(name):
                print("Registration was successful")
                print(f"Username: {name}, Password: {password}")
                counter_succcess += 1
            else:
                if_success = False
        else:
            if_success = False

    else:
        if_success = False
    if not if_success:
        print("Invalid username or password")

print(f"Successful registrations: {counter_succcess}")

