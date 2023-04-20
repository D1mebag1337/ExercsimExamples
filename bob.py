def resp1():
    return "Calm down, I know what I'm doing!"
def resp2():
    return "Sure."
def resp3():
    return "Whoa, chill out!"
def resp4():
    return "Whatever."
def resp4():
    return "Sure."
def response(hey_bob):
    if str.endswith(hey_bob,"?"):
        if str.isupper(hey_bob):
            return resp3()
        return resp4()
    if str.isupper(hey_bob):
        return
    if str == "":
        return "Fine. Be that way!"
    if not str.isalnum(hey_bob):
        return "Whatever."
    return


