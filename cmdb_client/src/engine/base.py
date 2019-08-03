from src.plugins import get_server_info
import requests, json
from concurrent.futures import ThreadPoolExecutor

class BaseHandler():
    """
    定义一个基类， 约束派生类的行为
    定义handler方法
    """
    def cmd(self,command,hostname=None):
        raise NotImplementedError('cmd() must be implemented')

    def handler(self):
        raise NotImplementedError('handler() must be implemented')


class SSHandSaltHandler(BaseHandler):
    def handler(self, hostname=None):
        print('ssh')

        # 先从服务端获取未采集主机列表
        r1 = requests.get(
            url='http://127.0.0.1:8000/api/asset/',

        )
        hostlist = r1.json()

        # 使用线程，创建线程，并行执行获取到结果后就提交
        pool = ThreadPoolExecutor(20)

        # 提交任务
        for hostname in hostlist:
            print(hostname)
            pool.submit(self.task, hostname)

    def task(self, hostname):
        info = get_server_info(self, hostname)
        r1 = requests.post(
            url='http://127.0.0.1:8000/api/asset/',
            data=json.dumps(info).encode('gbk'),
            headers={
                'content-type': 'application/json'
            }
        )

        print(r1)
        print(r1.text)