from stark.service.stark import site, StarkConfig, get_choice_text, Option
from api import models
from django.utils.safestring import mark_safe
from stark.forms.forms import StarkModelForm
from stark.forms.widgets import DatePickerInput
from django.shortcuts import HttpResponse, render, redirect


class ServerModelForm(StarkModelForm):
    class Meta:
        model = models.Server
        fields = "__all__"
        widgets = {
            'latest_date': DatePickerInput(attrs={'class': 'date-picker'})
        }


# 注册model

class BusinessUnitConfig(StarkConfig):
    list_display = [StarkConfig.display_checkbox, 'id', 'name']

    action_list = [StarkConfig.multi_delete]

    # 模糊搜索

    search_list = ['id', 'name']  # 添加搜索框和要匹配的搜索范围

    # 排序
    order_by = ['name', '-id']  # 可以指定一个或多个排序条件，使用 - 表示倒


site.register(models.BusinessUnit, BusinessUnitConfig)

class BusinessUnitConfig1(StarkConfig):
    list_display = [StarkConfig.display_checkbox, 'id', 'name']
    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(pk=1)

site.register(models.BusinessUnit, BusinessUnitConfig1,'v1')

class ServerConfig(StarkConfig):
    model_form_class = ServerModelForm

    def server_detail(self, request, pk):

        server_disks = models.Disk.objects.filter(server_id=pk).order_by('slot')
        server_memorys = models.Memory.objects.filter(server_id=pk).order_by('slot')
        server_nics = models.NIC.objects.filter(server_id=pk)

        return render(request, 'server/server_detail.html',
                      {'server_disks': server_disks, 'server_memory': server_memorys, 'server_nics': server_nics})

    def server_record(self, request, pk):

        server_records = models.AssetRecord.objects.filter(server_id=pk).order_by('-create_at')

        return render(request, 'server/server_record.html', {'server_records': server_records})

    def extra_url(self, header=None, row=None):
        from django.conf.urls import url

        urlpatterns = [
            url(r'^server_detail/(\d+)/', self.server_detail),
            url(r'^server_record/(\d+)/', self.server_record),
        ]

        return urlpatterns

    def show_detail(self, header=None, row=None):
        if header:
            return '查看详情'
        return mark_safe('<a href="/stark/api/server/server_detail/{}">查看</a>'.format(row.pk))  # 通过跳转页面展示

    def show_records(self, header=None, row=None):
        if header:
            return '历史变更记录'
        return mark_safe('<a href="/stark/api/server/server_record/{}">查看</a>'.format(row.pk))  # 通过跳转页面展示

    def show_status(self, header=None, row=None):
        if header:
            return '主机状态'
        color_dict = {
            1: 'green',
            2: 'blue',
            3: 'red',
            4: 'yellow'
        }
        return mark_safe('<span style="background-color: {};color:white;padding: 2px">{}</span>'.format(
            color_dict.get(row.device_status_id), row.get_device_status_id_display()))

    list_display = [
        StarkConfig.display_checkbox, 'id', 'hostname', show_status, 'os_platform', 'os_version', 'idc', show_detail,
        show_records]

    search_list = ['hostname', 'os_version', 'idc__name']

    list_filter = [
        Option('business_unit', is_multi=True, condition={'pk__in': [1.3]}),
        Option('device_status_id', is_choice=True, text_func=lambda x: x[1], value_func=lambda x: x[0])

    ]

    action_list = [StarkConfig.multi_delete]


site.register(models.Server, ServerConfig)
