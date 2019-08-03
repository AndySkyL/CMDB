from .base import BasePlugin
import os,re,traceback
from lib.response import BaseResponse
from lib.log import logger

class Disk(BasePlugin):

    def win(self,handler,hostname=None):

        ret=handler.cmd('vol',hostname)[:10]
        return ret

    def linux(self,handler,hostname=None):

        # 添加异常处理
        response = BaseResponse()

        try:
            if self.debug:
                # 读取文件信息
                with open(os.path.join(self.base_dir,'files','disk.out')) as f:
                    ret = f.read()
            else:
                ret=handler.cmd('ipconfig',hostname)[:10]
            response.data = self.parse(ret)
        except Exception as e:

            msg = traceback.format_exc()
            logger.error(msg)
            response.error = msg

            response.status = False
        return response.dict       # 返回解析后的结果



    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False

