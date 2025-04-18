# encriptar_highfleet.py
# Original code by: Oremirad

# Open the decrypted file
with open("./spanishTraduccion.seria", "rb") as f:
    data = list(f.read())

a = 0
b = 2531011

# Encrypt using XOR + PRNG
while a < len(data):
    data[a] = (b ^ (b >> 15) ^ data[a]) & 0xff
    b = (b + 214013) & 0xffffffff
    a += 1

# Save the result to a new encrypted file
with open("spanish_encrypted.seria_enc", "wb") as f:
    f.write(bytes(data))

print("File encrypted! Saved as 'spanish_encrypted.seria_enc'")

# Important: Make sure the file 'spanishTraduccion.seria' is in the same folder as this script.