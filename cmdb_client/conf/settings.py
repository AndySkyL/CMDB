import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE = 'agent'

ENGINE_DICT = {
    'agent':'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SSHHandler',
    'salt': 'src.engine.salt.SaltHandler',
    'aliyun': 'src.engine.aliyun.AliyunHandler',

}


PLUGIN_DICT = {
    'disk':'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.NIC',
    'cpu': 'src.plugins.cpu.Cpu',
    'basic': 'src.plugins.basic.Basic',
    'board': 'src.plugins.main_board.MainBoard',

}


# SSH 客户端模式配置信息

SSH_PRIVATE_KEY= 'SSH私钥'

SSH_PORT = '22'

SSH_USER = 'user'

# 开启DEBUG模式

DEBUG = True

LOGGER_PATH = os.path.join(BASE_DIR,'log','info.out')
LOGGER_NAME = 'cmdb'

CERT_PATH = os.path.join(BASE_DIR,'conf','cert')


# API验证的key

API_KEY = '123456'

RAS_PUB_KEY = b'LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JR0pBb0dCQUlvd3RjKzZiaERNbjFyUkRzRmJKSnZNQ0pvcWV4VkN3L3VzenMzRHBEbWtRbG1QeHdEWks3RlkKWUV0czA1SWxzazlBRHZWQWlwaGJBWWJodC9PdTJnN2dqU01CS2VQakpvK2swZzc1L1VyS3lCKzdRUEo1MUw5MQozSktJZTNtVGNzU3YrclJsOVBOVWppR1pQVG10WjFyQ1daejdwemEweDNUV04zcXhFall4QWdNQkFBRT0KLS0tLS1FTkQgUlNBIFBVQkxJQyBLRVktLS0tLQo='