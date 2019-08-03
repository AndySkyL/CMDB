from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api import service
from django.http import JsonResponse
import hashlib,json
import time
from django.conf import settings
from .utils.decrypt import decrypt


def gen_key(ctime):
    key = "{}|{}".format(settings.API_KEY, ctime)
    md5 = hashlib.md5()
    md5.update(key.encode('utf-8'))
    return md5.hexdigest()


SING_RECORD = {}

class AuthView(APIView):
    def dispatch(self, request, *args, **kwargs):
        ret = {'status': True, 'msg': '66666'}
        key = request.GET.get('key')
        ctime = request.GET.get('ctime')
        now = time.time()

        sign = gen_key(ctime)

        # 时间的判断
        if now - float(ctime) > 3:
            ret['status'] = False
            ret['msg'] = '认证超时'
            return JsonResponse(ret)

        if sign in SING_RECORD:
            ret['status'] = False
            ret['msg'] = '认证已使用'
            return JsonResponse(ret)

        if key != sign:
            ret['status'] = False
            ret['msg'] = '验证不通过'
            return JsonResponse(ret)
        SING_RECORD[sign] = None

        if ret['status']:
            return super().dispatch(request,*args,**kwargs)
        else:
            return JsonResponse(ret)



class Asset(AuthView):
    def get(self, request):
        host_list = ['host1', 'host2']

        return Response(host_list)  # 自动进行序列化

    def post(self, request):

        info = json.loads(decrypt(request.body).decode('utf-8'))
        action_type = info.get('type')
        print(info)
        ret = {'status': True, 'error': None, 'hostname': None}

        if action_type == 'create':

            # 新增主机信息

            server_dict = {}
            server_dict.update(info['basic']['data'])
            server_dict.update(info['cpu']['data'])
            server_dict.update(info['board']['data'])

            # 将字典装换为关键字参数的形式： name=value, 存入到数据库中,返回此条记录对象
            server = models.Server.objects.create(**server_dict)

            # 新增磁盘信息

            disk_info = info['disk']['data']
            disk_list = []
            for i in disk_info.values():
                i['server'] = server
                disk_list.append(models.Disk(**i))

            models.Disk.objects.bulk_create(disk_list)

            # 新增内存信息

            memory_info = info['memory']['data']
            memory_list = []
            for i in memory_info.values():
                i['server'] = server
                memory_list.append(models.Memory(**i))

            models.Memory.objects.bulk_create(memory_list)

            # 新增网卡信息
            nic_info = info['nic']['data']
            nic_list = []
            for name, i in nic_info.items():
                i['server'] = server
                i['name'] = name
                nic_list.append(models.NIC(**i))

            models.NIC.objects.bulk_create(nic_list)

        ## ****************************** 更新资产信息 ****************************
        elif action_type == 'update':
            # 更新资产信息

            # 查找要修改的主机
            hostname = info['basic']['data']['hostname']
            server_list = models.Server.objects.filter(hostname=hostname)
            server = server_list.first()

            service.process_basic(info, server_list)
            service.process_disk(info, server)
            service.process_memory(info, server)
            service.process_nic(info, server)



        ## ****************************** 更新主机和资产信息 ****************************

        elif action_type == 'host_change':
            # 更新资产信息和主机名
            print('更新资产信息和主机名')

            #### 更新主机名
            cert = info.get('cert')
            server_list = models.Server.objects.filter(hostname=cert)
            server = server_list.first()
            server.hostname = info['basic']['data']['hostname']
            server.save()
            service.process_basic(info, server_list)
            service.process_disk(info, server)
            service.process_memory(info, server)
            service.process_nic(info, server)

        ret['hostname'] = info['basic']['data']['hostname']
        return Response(ret)

