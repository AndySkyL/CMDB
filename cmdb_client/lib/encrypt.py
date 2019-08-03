import rsa
import base64
from conf import settings

def encrypt(value):
    key_str = base64.standard_b64decode(settings.RAS_PUB_KEY)
    pk = rsa.PublicKey.load_pkcs1(key_str)

    length = len(value)
    val_list = []
    for i in range(0, length, 117):
        tp1 = value[i:i + 117]
        val = rsa.encrypt(tp1, pk)
        val_list.append(val)

    return b''.join(val_list)