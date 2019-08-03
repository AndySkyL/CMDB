from conf import settings
from lib.import_class import import_string


def run():
    engine_path = settings.ENGINE_DICT.get(settings.ENGINE)   # 获取到引擎的名称对应类的路径
    engine_class = import_string(engine_path)
    obj = engine_class()
    obj.handler()

