# requests 第三方库
import requests
"""
爬虫：scrapy框架/ requests+beautiful soap
 urllib:
 1.中文先要quote
   url = quote(url,safe = '/:?=&'
 2.读取语句
   read()
   读出来的内容是字节码，需要先str(result_str,encoding='utf-8')
 3.404抛异常处理
"""


class HTTP:
    """
       staticmethod/classmethod都是静态函数装饰器
       后者用到了类变量
       这里没有用到类变量用前者
       封装成类以后好扩展
    """
    @staticmethod
    def get(url, return_json=True):
        # 静态函数，没用到self
        r = requests.get(url)
        # r中是返回信息的一个封装，不仅仅是想要的内容json
        if r.status_code != 200:
            # 三元表达式简化代码
            # 正常情况的特例处理
            return {} if return_json else ''
        return r.json() if return_json else r.text
    pass

