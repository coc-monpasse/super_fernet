import pytest
from faker import Faker
from super_fernet.super_fernet import SuperFernet

key=b'xzZ2QDNB26y1wj4Iukpw8m2ggEaGuu1_8tPYSBAKHzU='
fake=Faker()


def test_list_encryptions():
    sf=SuperFernet(key)
    for _ in range(10):
        normal_list=[fake.text(),fake.text(),fake.text()]
        list_encrypted=sf.encrypt_list(normal_list)
        list_decrypted=sf.decrypt_list(list_encrypted)
        assert normal_list==list_decrypted
        assert 1 ==0