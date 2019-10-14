# -*- coding: UTF-8 -*-
import warnings


error_codes = []


class _MetaError(type):

    def __new__(cls, name, bases, body):
        qualname = body['__qualname__']
        new_class = type.__new__(cls, name, bases, body)
        if new_class.code in error_codes:
            warnings.warn(f'{qualname} 类的异常代码重复! 请修改！', stacklevel=2)
        else:
            error_codes.append(new_class.code)
        return new_class


class BaseError(Exception, metaclass=_MetaError):
    """ Backyard 业务异常基类 """

    code = 1000
    desc = '内部错误'
    http_status = 500
    alert_sentry = True

    def __init__(self, desc: str=None, data=None, **kwargs):
        self.kwargs = kwargs

        if not desc:
            try:
                desc = self.desc % self.kwargs
            except KeyError:
                desc = f'cannot format exception message: {self.desc}'

        self.message = desc
        self.data = data
        super().__init__(desc)


class ClientException(BaseError):
    code = 40000
    http_code = 403
    desc = '客户端出错：%(reason)s'


class ServerException(BaseError):
    code = 50000
    http_code = 500
    desc = '服务器出错：%(reason)s'
