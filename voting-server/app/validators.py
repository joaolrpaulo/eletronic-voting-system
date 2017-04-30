import re


def voter_id(data):
    # Exactly 8 numbers to follow National Card ID
    return bool(re.match(str(data), '^(\d{8})$'))


def password(data):
    # Minimum 8 chars, 1 upper, 1 lower, 1 symbol, 1 numeric
    return bool(re.match(data, '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'))


def name(data):
    # Portuguese names
    return bool(re.match(data, '^[A-Za-zÀ-ú]{1,20}( [A-Za-zÀ-ú]{1,20}){1,20}$'))


def email(data):
    # General email
    return bool(re.match(data, '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'))


def city(data):
    # Portuguese cities
    return bool(re.match(data, '^[A-Za-zÀ-ú]+( [A-Za-zÀ-ú]+)*$'))
