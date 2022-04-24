
# 导入哪个配置就是哪个配置
from profiles.default import *

# default可以为空
default = 'local'

__cur_env = None


def acvite_profile(profile: str,double: str=True):
    """设置活动分支"""
    t = env.get(profile)
    if t == None:
        raise Exception("找不到环境变量")
    global __cur_env
    __cur_env = {**global_env, **t}
    print('===============================active profile:%s========================================'%(profile))
    if double:
        input()


def set_temp_env(key, value):
    """设置临时环境变量"""
    __cur_env[key] = value


def convert_env(key):
    """获取环境变量，如果没有则初始化"""
    if __cur_env == None:
      __init_env()
    r=__cur_env[key]
    if r==None:
      raise Exception("没有找到对应环境变量:"+key)
    return r

def __init_env():
  if default!=None:
    acvite_profile(default)
  else :
    global __cur_env
    __cur_env = {**global_env}