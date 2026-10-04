"""Pure input-validation helpers for the signup API.

Deliberately free of Flask imports: these are the easiest thing in the repo
to unit-test directly (test_validators.py), and the Coder agent can rewrite
this file without having to touch any routing code.
"""
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Password must be at least 8 characters, contain at least one letter and one digit
PASSWORD_REGEX = re.compile(r"^(?=.*[A-Za-z])(?=.*\d).{8,}$")


def is_valid_email(email):
    return bool(email) and bool(EMAIL_REGEX.match(email))


def is_strong_password(password):
    """Return True if password is at least 8 characters long and contains
    at least one letter and one digit.
    """
    return bool(password) and bool(PASSWORD_REGEX.match(password))
