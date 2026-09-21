import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
"""它会初始化 Django，包括加载项目配置、注册应用、准备请求处理中间件等，然后返回一个可调用的应用对象，赋给 application"""