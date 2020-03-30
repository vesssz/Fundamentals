data = input().split(", ")



def check_valid(username):
    check = True
    for i in username:
        if i == "_" or i == "-" or i.isalnum():
            continue
        else:
            check = False
            break
    return check


def check_lenght(username):
    if 3 <= len(username) <= 16:
        return True
    else:
        return False


for username in data:
    if check_lenght(username) and check_valid(username):
        print(username)
