# **********************************  这里是程序的配置文件，请不要修改settings.py  *******************************************

# 程序安全密钥，决定着程序的各项加密安全性，请在部署项目时更换。
# 文末有生成脚本。
SECRET_KEY = "xxx"

# 调试模式开关，在生产环境中请务必关闭
DEBUG = False

# 请在此处定义您的前端和后端地址
FRONTEND_ADDR = 'xxx'
BACKEND_ADDR = 'xxx'

# 程序中管理员和商户重置的默认密码，请不要泄露。
# 文末有生成脚本。
ADMIN_DEFAULT_PASS = 'xxx'
SHOP_DEFAULT_PASS = 'xxx'

# 指定可以运行本项目的主机/域名。
ALLOWED_HOSTS = ['xxx']

# 指定信任源，定义的源可以发起跨站请求，请勿滥用以防止遭受跨站攻击。
CSRF_TRUSTED_ORIGINS = [
    'xxx',
]

# 指定允许的跨域资源请求地址，在配置中的地址可以请求后端资源。
CORS_ORIGIN_WHITELIST = [
    "xxx",
]

# 数据量配置，支持不同类型的数据库
DATABASES = {
    'default': {
        # 数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxx',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': 'xxx.xxx.xxx.xxx',
    }
}

# 缓存配置，定义 Redis 缓存选项。
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://xxx.xxx.xxx.xxx:xxx/xxx",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# STMP 服务器配置，用于系统发送邮件。
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = '587'
# 发件用户
EMAIL_HOST_USER = 'xxx'
# 用户密钥，在邮箱设置中获取
EMAIL_HOST_PASSWORD = 'xxx'

# 密钥生成脚本，用于生成 SECRET_KEY, ADMIN_DEFAULT_PASS 和 SHOP_DEFAULT_PASS。
# import secrets
# import string
# characters = string.ascii_letters + string.digits + string.punctuation
# secure_key = ''.join(secrets.choice(characters) for i in range(50)) # 生成长度为50位
# print(secure_key)
