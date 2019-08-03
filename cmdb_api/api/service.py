from api import models

def process_basic(info,server_list):
    server_dict = {}
    server_dict.update(info['basic']['data'])
    server_dict.update(info['cpu']['data'])
    server_dict.update(info['board']['data'])

    # 更新主机信息
    server_list.update(**server_dict)


def process_disk(info,server):
    ############## 更新磁盘信息 ##############
    disk_info = info['disk']['data']
    disk_query = models.Disk.objects.filter(server=server)  # 获取数据库中的磁盘信息

    disk_info_set = set(disk_info)  # 将从数据库和采集客户端获取到的数据都转化为集合
    disk_query_set = {str(i.slot) for i in disk_query}  # 从数据对象中获取到槽位信息并转化为str类型


    ###### 新增集合

    add_slot_set = disk_info_set - disk_query_set
    disk_list = []
    add_record_list = []
    for slot in add_slot_set:
        disk_info[slot]['server'] = server  # 增加磁盘表中主机外键信息

        # 取出新增硬盘的数据
        row_dict = disk_info[slot]

        # 存储 字段名：字段值
        msg_list = []

        for k,v in row_dict.items():
            verbose_name = models.Disk._meta.get_field(k).verbose_name   # 获取到数据库中的verbose_name
            msg_list.append("{}:{}".format(verbose_name,v))

        # 将信息添加到记录数据列表中
        add_record_list.append(models.AssetRecord(server=server,content='新增硬盘，信息如下:{}'.format(';'.join(msg_list))))

        disk_list.append(models.Disk(**disk_info[slot]))  # 将要写入的数据添加到对象列表中

    if disk_list:
        models.Disk.objects.bulk_create(disk_list)  # 一次性写入
        models.AssetRecord.objects.bulk_create(add_record_list)  # 写入资产记录表

    ###### 删除集合
    del_slot_set = disk_query_set - disk_info_set
    if del_slot_set:
        models.AssetRecord.objects.create(server=server,content='槽位{}的硬盘被移除了'.format(','.join(del_slot_set)))
        models.Disk.objects.filter(server=server, slot__in=del_slot_set).delete()

    ###### 更新集合
    update_record_list = []
    update_dict = {}
    update_slot_set = disk_info_set & disk_query_set
    for slot in update_slot_set:

        row_dict = disk_info[slot]
        disk_obj = models.Disk.objects.get(server=server,slot=slot)
        msg_list = []
        # 将原来的值和新的值进行对比
        for k,v in row_dict.items():
            old = getattr(disk_obj,k)    # 这里取出的old为浮点型，v的值为str

            if str(old) != v:
                update_dict[k] = v
                verbose_name = models.Disk._meta.get_field(k).verbose_name
                msg_list.append('{} 由 {} 变更为 {}'.format(verbose_name,old,v))

        if msg_list:
            obj = models.AssetRecord(server=server,content='槽位{} 变更情况: {}'.format(slot,';'.join(msg_list)))
            update_record_list.append(obj)
            models.Disk.objects.filter(server=server, slot=slot).update(**update_dict)

    if update_record_list:
        models.AssetRecord.objects.bulk_create(update_record_list)




def process_memory(info,server):
    ############## 更新内存信息 ##############
    memory_info = info['memory']['data']
    memory_query = models.Memory.objects.filter(server=server)  # 获取数据库中的内存信息

    memory_info_set = set(memory_info)  # 将从数据库和采集客户端获取到的数据都转化为集合
    memory_query_set = {str(i.slot) for i in memory_query}  # 从数据对象中获取到槽位信息并转化为str类型

    # ———————————————— 进行集合运算（根据内存的槽位slot来确定） ————————————————
    ###### 新增集合

    add_slot_set = memory_info_set - memory_query_set
    memory_list = []
    for slot in add_slot_set:
        memory_info[slot]['server'] = server  # 增加内存表中主机外键信息
        memory_list.append(models.Memory(**memory_info[slot]))  # 将要写入的数据添加到对象列表中
    if memory_list:
        models.Memory.objects.bulk_create(memory_list)  # 一次性写入

    ###### 删除集合
    del_slot_set = memory_query_set - memory_info_set
    if del_slot_set:  # 查询出对应主机中被移除内存的槽位号，删除数据
        models.Memory.objects.filter(server=server, slot__in=del_slot_set).delete()

    ###### 更新集合
    update_slot_set = memory_info_set & memory_query_set
    for slot in update_slot_set:
        models.Memory.objects.filter(server=server, slot=slot).update(**memory_info[slot])


def process_nic(info,server):
    ############## 更新网卡信息 ##############
    nic_info = info['nic']['data']
    nic_query = models.NIC.objects.filter(server=server)

    nic_info_set = set(nic_info)
    nic_query_set = {str(i.name) for i in nic_query}


    ###### 新增集合

    add_name_set = nic_info_set - nic_query_set
    nic_list = []
    for name in add_name_set:
        nic_info[name]['server'] = server
        nic_info[name]['name'] = name  # 需要添加网卡信息
        nic_list.append(models.NIC(**nic_info[name]))
    if nic_list:
        models.NIC.objects.bulk_create(nic_list)

    ###### 删除集合
    del_name_set = nic_query_set - nic_info_set
    if del_name_set:
        models.NIC.objects.filter(server=server, name__in=del_name_set).delete()

    ###### 更新集合
    update_name_set = nic_info_set & nic_query_set
    for name in update_name_set:
        models.NIC.objects.filter(server=server, name=name).update(**nic_info[name])