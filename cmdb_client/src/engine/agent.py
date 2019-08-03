from src.engine.base import BaseHandler
from src.plugins import get_server_info
import requests, json, os,time
from conf import settings
from lib.api_auth import gen_key
from lib.encrypt import encrypt


class AgentHandler(BaseHandler):

    def cmd(self, command, hostname=None):
        import subprocess
        return subprocess.getoutput(command)

    def handler(self, hostname=None):
        print('agent')
        # 资产采集
        info = get_server_info(self, hostname)

        # 数据分析

        if not os.path.exists(settings.CERT_PATH):
            # 新增
            info['type'] = 'create'


        else:
            with open(settings.CERT_PATH, 'r', encoding='utf-8') as f:
                cert = f.read()

            hostname = info['basic']['data']['hostname']

            if cert == hostname:
                # 主机名没变 更新资产信息
                info['type'] = 'update'

            else:
                # 主机名变了，更新资产信息,并提交旧的主机名
                info['type'] = 'host_change'
                info['cert'] = cert

        # 资产上报

        ctime = time.time()
        r1 = requests.post(
            url='http://127.0.0.1:8000/api/asset/',
            params={'key':gen_key(ctime),'ctime':ctime},
            data=encrypt(json.dumps(info).encode('utf-8')),
            headers={
                'content-type': 'application/json'
            }
        )

        # 保存唯一标识

        data = r1.json()
        print(data)

        if data.get('status'):
            with open(settings.CERT_PATH, 'w', encoding='utf-8')as f:
                f.write(data.get('hostname'))
