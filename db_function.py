import pymysql
import re
import os
import env

# 初始化链接
db = pymysql.connect(host=env.convert_env('db_url'),
                     port=env.convert_env('db_port'),
                     user=env.convert_env('db_userName'),
                     passwd=env.convert_env('db_passwd'),
                     database=env.convert_env("db_database"))

# 初始化相关数据
sql_map = {}
for root, paths, files in os.walk('sql'):
    for file in files:
        with open(root+'\\'+file, encoding='utf8') as f:
            source = f.read()
            # todo:此处正则有缺陷，意味着如果句子中存在#号就会识别出错
            sqls = re.findall("^# [^\n]*\n([^#]*)", source, flags=re.S | re.M)
            names = re.findall("^# (.*)", source, flags=re.M)
            temp_sql_map = dict(map(lambda x, y: [x, y], names, sqls))
            sql_map[file.split('.')[0]] = temp_sql_map


def exec_sql(key):
    """简单的SQL执行"""
    sqllist = get_sql(key)
    cursor = db.cursor()
    for sql in sqllist:
        cursor.execute(sql)
        # print("execute_success")
    db.commit()
    cursor.close()


def get_sql(key) -> list:
    """获取sql，注意sql中不要有#"""
    keys = key.split('.')
    sqlstr = sql_map[keys[0]][keys[1]]
    sqllist = sqlstr.split(';')
    # print(re.match('^\s+$',sql,flags=re.M))
    # print(sql)
    return list(filter(lambda x: re.match('^\s+$', x) == None, sqllist))


def get_sql_line(key) -> str:
    """获取单行sql"""
    return ';'.join(get_sql(key))+';'
