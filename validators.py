"""Pure input-validation helpers for the signup API.

Deliberately free of Flask imports: these are the easiest thing in the repo
to unit-test directly (test_validators.py), and the Coder agent can rewrite
this file without having to touch any routing code.
"""
import re

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email):
    return bool(email) and bool(EMAIL_REGEX.match(email))
