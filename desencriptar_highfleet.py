# desencriptar_highfleet.py
# Original code by: https://gist.github.com/blluv

# Open the encrypted file
with open("./english.seria_enc", "rb") as f:
    data = list(f.read())

a = 0
b = 2531011

# Decrypt using XOR + PRNG
while a < len(data):
    data[a] = (b ^ (b >> 15) ^ data[a]) & 0xff
    b = (b + 214013) & 0xffffffff
    a += 1

# Save the result to a new file
with open("english_decrypted.seria", "wb") as f:
    f.write(bytes(data))

print("File decrypted! Saved as 'english_decrypted.seria'")

# Important: Make sure the file 'english.seria_enc' is in the same folder as this script.
