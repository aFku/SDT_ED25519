# SDT Project, ed448

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
Private_key = binascii.b2a_hex(os.urandom(Private_key_bytes))
print("Private key:", Private_key)
# Public key generation
Public1 = hashlib.shake_256()
Public1.update(Private_key)
print("Hashed:     ", Public1.hexdigest(114))
Public2 = Public1.hexdigest(114)
Public3 = Public2[-114:]
print("Lower 57:   ", Public3)
########################################################################################

Public4 = int(Public3[0], 16)
Public4 = Public4 & 1100 #  The two least significant bits of the first octet are cleared
Public3 = change_string_with_int(Public3, 0, Public4)

########################################################################################
########################################################################################

Public5 = int(Public3[-1], 16)
Public5 = Public5 & 0000 # All eight bits the last octet are cleared
Public3 = change_string_with_int(Public3, -1, Public5)
########################################################################################
########################################################################################

for x in range(1, len(Public3)):
    tmp = int(Public3[x], 16)
    tmp = tmp | 1000
    Public3 = change_string_with_int(Public3, x, tmp) # the highest bit of the second to last octet is set

########################################################################################
########################################################################################



#a = int.from_bytes(Public3[:114].encode(), "little")
print(Public3)
Public3 = binascii.unhexlify(Public3)
a = int.from_bytes(Public3[:57], "little")
print(a)
#print(sys.getsizeof(Public3.encode()))






