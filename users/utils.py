import random

def get_new_password():
    password_base = "abcdefghjkmnpqrstuvwxyzABCDE-!+$FGHJKLMNPQRSTUVWXYZ123456789"
    password_base_list = list(password_base)
    random_pass = random.sample(password_base_list, 12)
    new_password = ''.join(random_pass)
    return new_password