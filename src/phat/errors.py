# Copyright 2022 iiPython

# Metaclasses
class SignatureError(Exception):
    pass

# Subclasses
class DeclinedKeyRequest(Exception):
    pass

class NotAuthenticated(Exception):
    pass

class KeyGenerationError(SignatureError):
    pass

class KeySignatureMismatch(SignatureError):
    pass
