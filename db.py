# 数据库相关
from tkinter.messagebox import NO
from uuid import uuid5
from db_function import *
from string import Template
import uuid


def init_submit():
    """Demo"""
    exec_sql("Test.Test")