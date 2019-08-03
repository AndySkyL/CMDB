# import requests
# import json
# import time
# import hashlib
#
# KEY = '123456'
#
# ctime = time.time()
#
# print(float(str(ctime)))
#
# def gen_key(ctime):
#     key = "{}|{}".format(KEY, ctime)
#     md5 = hashlib.md5()
#     md5.update(key.encode('utf-8'))
#     return md5.hexdigest()
#
#
# r1 = requests.post(
#     url='http://127.0.0.1:8000/api/test/',
#     params={'key': gen_key(ctime), 'ctime': ctime},
#     data=json.dumps({'a': 'b'}).encode('gbk'),
#     headers={
#         'content-type': 'application/json'
#     }
# )
#
# print(r1.json())

##############################
# class Base(object):
#     def f1(self):
#         print('Base f1')
#         self.f2()
#
#     def f2(self):
#         print('Base f2')
#
# class Foo(Base):
#     def f2(self):
#         print('Foo f2')
#
#
# obj = Foo()
# obj.f1()

#############################

# class Base():
#     def f1(self):
#         super().f1()
#         print('Base f1')
#
#
# class Foo():
#     def f1(self):
#         print('Foo f1')
#
#
# class Bar(Base, Foo):
#     def f1(self):
#         super().f1()
#         print('Bar f1')
#
#
# obj = Bar()
# obj.f1()
