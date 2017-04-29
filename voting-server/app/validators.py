import re

def matcher(data, regExp):
    return True if re.match(regExp, data) else False


def voter_id(data):
    # Exactly 8 numbers to follow National Card ID
    return matcher(str(data), '^(\d{8})$')


def password(data):
    # Minimum 8 Chars, 1 Upper, 1 Lower, 1 Symbol, 1 Numeric
    return matcher(data, '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')


def name(data):
    # Portuguese Name Validation
    return matcher(data, '^[A-Za-zÀ-ú]{1,20}( [A-Za-zÀ-ú]{1,20}){1,20}$')


def email(data):
    # General email validation
    return matcher(data, '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')


def city(data):
    return matcher(data, '^[A-Za-zÀ-ú]+( [A-Za-zÀ-ú]+)*$')
