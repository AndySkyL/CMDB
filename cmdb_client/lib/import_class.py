import importlib


def import_string(engine_path):
    module, engine = engine_path.rsplit('.', maxsplit=1)  # 使用'.'分割字符，获取模块路径和采集方式的类名
    module_class = importlib.import_module(module)  # 导入对应的模块，并获取客户端对象（如 agent.py）
    engine_class = getattr(module_class, engine)  # 获取到agent.py中的类名属性
    return engine_class
