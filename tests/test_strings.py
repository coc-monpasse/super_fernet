#!/usr/bin/env python

"""Tests for `super_fernet` package."""

import pytest
from faker import Faker
from super_fernet.super_fernet import SuperFernet

key=b'xzZ2QDNB26y1wj4Iukpw8m2ggEaGuu1_8tPYSBAKHzU='
fake=Faker()


def test_string_encryptions():
    sf=SuperFernet(key)
    for _ in range(1000):
        normal_string=fake.text()
        string_encrypted=sf.encrypt_string(normal_string)
        string_decrypted=sf.decrypt_string(string_encrypted)
        assert normal_string==string_decrypted
        