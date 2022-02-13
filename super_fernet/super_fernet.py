"""Main module."""

import base64
import binascii
import typing
import os
import time
from cryptography.fernet import Fernet


class SuperFernet:
    def __init__(self, key: bytes, key1: bytes = None) -> None:
        self._crypto = Fernet(key)
        if key1 != None:
            self._multicrypto = Fernet([key, key1])

    @classmethod
    def generate_key(cls) -> bytes:
        return base64.urlsafe_b64encode(os.urandom(32))

    def encrypt_string(self, string: str):
        return self._crypto.encrypt(string.encode())

    def decrypt_string(self, string: bytes):
        return self._crypto.decrypt(string).decode()

    def encrypt_list(self, list: typing.Union[list,set]):
        for i in range(len(list)):
            list[i] = self.encrypt_string(list[i])
        return list

    def decrypt_list(self, list: typing.Union[list,set]):
        for i in range(len(list)):
            list[i] = self.decrypt_string(list[i])
        return list

    def encrypt_dict(self, dict: dict):
        for k, v in dict.items():
            dict[k] = self.encrypt_string(v)
        return dict

    def decrypt_dict(self, dict: dict):
        for k, v in dict.items():
            dict[k] = self.decrypt_string(v)
        return dict


# key = SuperFernet.generate_key()
# mp = SuperFernet(key)
# print(base64.b64decode(base64.b64encode(key)))
# print(key)
# string1 = mp.encrypt_string("hola a todos")
# print(string1)
# string2 = mp.decrypt_string(string1)
# print(string2)

# list1 = mp.encrypt_list(["hueofewa", "pedo", "freagra", "fag917329fwanfiy7greagrea"])
# print(list1)
# list2 = mp.decrypt_list(list1)
# print(list2)