import rsa
import base64
from django.conf import settings

def decrypt(value):
    key_str = base64.standard_b64decode(settings.RSA_PRI_KEY)
    pk = rsa.PrivateKey.load_pkcs1(key_str)

    length = len(value)

    val_list = []
    for i in range(0, length, 128):
        tp1 = value[i:i + 128]
        val = rsa.decrypt(tp1, pk)
        val_list.append(val)

    return b''.join(val_list)