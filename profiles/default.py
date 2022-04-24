# 环境变量名称
global_env = {
    # 代理访问开关，如果为True则所有请求使用代理调用
    "proxy_enable": False,
    # 代理Cookie每次需要粘贴，才可以访问
    "proxy_cookie": "",
    # 代理url
    "proxy_url": "",
    # 数据库配置
    "db_url":"",
    # 数据库userName
    "db_userName":"",
    # 数据库passwd
    "db_passwd":"",
    # 数据库端口
    "db_port":"",
    # 数据库名称
    "db_database":""
}
env = {
    "pre": {
        'demo': "http://localhost:8080"
    },
    "local": {
        'demo': "http://localhost:8080"
    },
    "prod": {
        'demo': "http://localhost:8080"
    }
}