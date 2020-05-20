#    HPCC SYSTEMS software Copyright (C) 2019 HPCC Systems.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


from cryptography.fernet import Fernet


def keygen(file):
    key = Fernet.generate_key()
    writebyteliteraltofile(key, file)


def getbyteliteralfromfile(file):
    with open(file, 'rb') as f:
        for line in f:
            rv = line
        return rv


def writebyteliteraltofile(bl, file):
    with open(file, 'wb') as f:
        f.write(bl)


def getkeyfromfile(file):
    return getbyteliteralfromfile(file)


def getencryptedpassfromfile(file):
    return getbyteliteralfromfile(file)


def decryptpassword(encrypted_password, key):
    cipher = Fernet(key)
    bl_password = cipher.decrypt(encrypted_password)
    pt_password = bytes(bl_password).decode("utf-8")
    return pt_password


def encryptpassword(password, key):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode())
