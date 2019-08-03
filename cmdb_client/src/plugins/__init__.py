from conf.settings import PLUGIN_DICT
from lib.import_class import import_string


def get_server_info(handler,hostname=None):
    """
    通过配置 采集信息
    """
    info = {}

    for name, path in PLUGIN_DICT.items():
        plugin_class = import_string(path)  # 获取到要采集的主机项
        obj = plugin_class()
        info[name] = obj.process(handler,hostname)
    return info
