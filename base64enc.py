import base64
encoded = base64.b64encode(open("filename.png", "rb").read())
print(encoded)