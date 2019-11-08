from base64 import b64encode
a="Banana"
print(a)
a=b64encode(a.encode())
print(a)
