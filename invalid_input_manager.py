def validate_name(name):
    return len(name) > 0

def validate_email(email):
    return "@" in email and email.endswith(".com")

def validate_phone(phone):
    return phone.isdigit()
