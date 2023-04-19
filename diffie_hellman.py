import math
import secrets
def private_key(p):
    private = secrets.randbelow(p)
    return private

def public_key(p, g, private):
    public = math.pow(g,private) % p
    return public

def secret(p, public, private):
    s = math.pow(public,private) % p
    return s