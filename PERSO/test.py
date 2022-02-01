import hashlib

sha1 = hashlib.sha1()

data = "this is a text"

sha1.update(data.encode("utf-8"))

encode = sha1.hexdigest()

clearpswrd = encode

