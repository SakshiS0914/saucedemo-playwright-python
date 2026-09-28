import random


def generate_user():
    random_number = random.randint(1000, 9999)

    return {
        "first_name": f"John{random_number}",
        "last_name": f"Doe{random_number}",
        "postal_code": f"1{random_number}"
    }