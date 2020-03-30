def check_password(password):
    result = True
    for i in password[:5]:
        if not i.isalpha():
            result = False
    if password[-1].isalpha():
        result = False
    return result

print(check_password("shaje2"))





