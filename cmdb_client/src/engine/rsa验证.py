import rsa
import base64

# ######### 1. 生成公钥私钥 #########
pub_key_obj, priv_key_obj = rsa.newkeys(1024)

pub_key_str = pub_key_obj.save_pkcs1()
pub_key_code = base64.standard_b64encode(pub_key_str)

priv_key_str = priv_key_obj.save_pkcs1()
priv_key_code = base64.standard_b64encode(priv_key_str)

print('公钥：',pub_key_code)
print('私钥：',priv_key_code)


# ######### 2. 加密 #########
def encrypt(value):
    key_str = base64.standard_b64decode(pub_key_code)
    pk = rsa.PublicKey.load_pkcs1(key_str)

    length = len(value)
    val_list = []
    for i in range(0, length, 117):
        tp1 = value[i:i + 117]
        val = rsa.encrypt(tp1.encode('utf-8'), pk)
        val_list.append(val)

    return b''.join(val_list)     # 加密后的数据拼接


# ######### 3. 解密 #########
def decrypt(value):
    key_str = base64.standard_b64decode(priv_key_code)
    pk = rsa.PrivateKey.load_pkcs1(key_str)

    length = len(value)

    val_list = []
    for i in range(0, length, 128):
        tp1 = value[i:i + 128]
        val = rsa.decrypt(tp1, pk)
        val_list.append(val)

    return b''.join(val_list)     # 解密后的数据拼接


# ######### 基本使用 #########
if __name__ == '__main__':
    v = 'maple' * 100
    v1 = encrypt(v)
    print(v1)  # 加密后的数据
    v2 = decrypt(v1)
    print(v2)  # 解密后的数据
