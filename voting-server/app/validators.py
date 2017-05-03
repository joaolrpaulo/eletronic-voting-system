import re


def has_valid_body(json, fields, functions):
    return all([func(json.get(field)) for field, func in zip(fields, functions)])


def get_body_errors(json, fields, functions):
    missing = [field for field in fields if not json.get(field)]
    malformed = [field for field, func in zip(fields, functions) if json.get(field) and not func(json.get(field))]
    errors = {}
    if missing:
        errors['missing'] = missing
    if malformed:
        errors['malformed'] = malformed
    return errors


def voter_id(data):
    # Exactly 8 numbers to follow National Card ID
    return bool(re.match('^(\d{8})$', str(data)))


def password(data):
    # Minimum 8 chars, maximum 64 chars, 1 upper, 1 lower, 1 symbol, 1 numeric
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
    # Title can have letters, numbers and symbols
    return bool(re.match('^[ -~À-ú]{1,50}$', str(data)))


def description(data):
    # Description can have letters, numbers and symbols
    return bool(re.match('^[ -~À-ú]{1,1000}$', str(data)))


def image(data):
    # General file-system path
    return bool(re.match('^/[\w+/]+\.(png|jpg|jpeg)$', str(data)))


def ts(data):
    # Unix timestamp
    return bool(re.match('^[0-9]{1,10}$', str(data)))
