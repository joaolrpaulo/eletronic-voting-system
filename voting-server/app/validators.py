import re


def voter_id(data):
    # Exactly 8 numbers to follow National Card ID
    return bool(re.match('^(\d{8})$', str(data)))


def password(data):
    # Minimum 8 chars, Maximum, 64 chars, 1 upper, 1 lower, 1 symbol, 1 numeric
    return bool(re.match('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,64}$', str(data)))


def name(data):
    # Portuguese names
    return bool(re.match('^[A-Za-zÀ-ú ]{1,150}$', str(data)))


def email(data):
    # General email
    return bool(re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', str(data)))


def city(data):
    # Portuguese cities
    return bool(re.match('^[A-Za-zÀ-ú ]{1,100}$', str(data)))


def title(data):
    return bool(re.match('^[ -~]{1,50}$', str(data)))


def description(data):
    return bool(re.match('^[ -~]{1,1000}$', str(data)))


def image(data):
    return bool(re.match('^\/[\w+/]+\.(png|jpg|jpeg)$', str(data)))


def ts(data):
    return bool(re.match('^[0-9]{1,10}$', str(data)))
