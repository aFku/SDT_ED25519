import hashlib
import os
import binascii

def change_string_with_int(string: str, index, number: int):
    tmp = list(string)
    tmp[index] = hex(number)[-1]
    return ''.join(tmp)

p = pow(2, 448) - pow(2, 224) - 1

base = 224580040295924300187604334099896036246789641632564134246125461686950415467406032909029192869357953282578032075146446173674602635247710, 298819210078481492676017930443930673437544040154080242095928241372331506189835876003536878655418784733982303233503462500531545062832660

Private_key_bytes = 57
Public_key_bytes = Private_key_bytes
Signature_bytes = Private_key_bytes + Public_key_bytes

# Secret key is random
Private_key = binascii.b2a_hex(os.urandom(8*Private_key_bytes))
print("Private key:", Private_key)
# Public key generation
Public1 = hashlib.shake_256()
Public1.update(Private_key)
print("Hashed:     ", Public1.hexdigest(114))
Public2 = Public1.hexdigest(114)
Public3 = Public2[-114:]
print("Lower 57:   ", Public3)
########################################################################################
Public4 = []
for index in range(1, len(Public3), 2):
    num1 = int(Public3[index-1], 16)
    num2 = int(Public3[index], 16)
    num3 = num1 << 4 | num2
    if len(str(hex(num3))[2:]) < 2:
        Public4.append('0' + str(hex(num3))[2:])
    else:
        Public4.append(str(hex(num3))[2:])

tmp = str(hex(int(Public4[0], 16) & 0b11111100))
if len(tmp) < 4:
    tmp = '0' + tmp[2:]
else:
    tmp = tmp[2:]
Public4[0] = tmp

for index, octet in enumerate(Public4[1:]):
        tmp = str(hex(int(octet, 16) | 0b10000000))
        if len(tmp) < 4:
            tmp = '0' + tmp[2:]
        else:
            tmp = tmp[2:]

        Public4[index+1] = tmp



print(Public4)
x = bytearray()
for q in Public4:
    tmp = int(q, 16)
    x.append(tmp)

print(x)
print(int.from_bytes(x, 'little'))

#Public3 = binascii.unhexlify(Public3)
#a = int.from_bytes(Public3[:57], "little")
#print(a)





