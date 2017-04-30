import re


def voter_id(data):
    # Exactly 8 numbers to follow National Card ID
    return bool(re.match('^(\d{8})$', str(data)))


def password(data):
    # Minimum 8 chars, 1 upper, 1 lower, 1 symbol, 1 numeric
    return bool(re.match('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', str(data)))


def name(data):
    # Portuguese names
    return bool(re.match('^[A-Za-zÀ-ú]{1,20}( [A-Za-zÀ-ú]{1,20}){1,20}$', str(data)))


def email(data):
    # General email
    return bool(re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', str(data)))


def city(data):
    # Portuguese cities
    return bool(re.match('^[A-Za-zÀ-ú]+( [A-Za-zÀ-ú]+)*$', str(data)))
