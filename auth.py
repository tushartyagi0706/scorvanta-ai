import csv
import os

FILE = "users.csv"

def register_user(username, password):
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password"])

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password])


def authenticate_user(username, password):
    if not os.path.exists(FILE):
        return False

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                return True
    return False