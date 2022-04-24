from operator import inv
from pkgutil import extend_path
from re import L
import grequests
from unicodedata import name
from pytest import param
import requests
import json
import pymysql
import beautiful
from env import *




pymysql.connect(host='www.jaken.top', port=3306,
                user='root', passwd='jaken123')


def invoke(data, url, log, name='', type='basic'):
    """
    指派执行器
    type: basic为默认值，param为get请求的链接转换形式
    """
    if type == 'basic' and convert_env('proxy_enable') == True:
        return proxy_req(data, url, log, name)
    elif type == 'param' and convert_env('proxy_enable') == True:
        return proxy_req_param(data, url, log, name)
    elif type == 'basic' and convert_env('proxy_enable') == False:
        return req(data, url, log, name)
    elif type == 'param' and convert_env('proxy_enable') == False:
        return req_param(data, url, log, name)



def req(data, url, log, name=''):
    """内部直连调用"""
    if log is True:
        print(
            "=============================================================================================================")
        print("url:"+url)
        print("payload:")
        beautiful.render(data)
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    r = json.loads(response.text)
    if log is True:
        print("response:")
        beautiful.render(r)
        print(
            "=============================================================================================================")
    return r


def req_param(data: dict, url, log, name=''):
    """内部直连调用，转换参数"""
    return req({}, req_param_build(data, url, log, name), log, name)


def req_param_build(data: dict, url, log, name=''):
    """参数构建转换方法"""
    li = []
    for key, value in data.items():
        li.append(str(key)+"="+str(value))
    li = '&'.join(li)
    url += '?'+li
    return url


def proxy_req(data: dict, url, log, name=''):
    """代理作为跳板访问"""
    req_data = {
        "jsonParam": json.dumps(data),
        "interfaceName": url,
        "url": url,
        "body": json.dumps(data),
        "requestType": "POST"
    }
    if log is True:
        print(
            "=============================================================================================================")
        print("env: 代理")
        print("url:"+url)
        print("payload:" + json.dumps(data, indent=4, ensure_ascii=False))
    payload = json.dumps(req_data)
    headers = {
        'Content-Type': 'application/json'
    }
    cookies = {i.split("=")[0]: i.split("=")[-1]
               for i in convert_env('proxy_cookie').split("; ")}
    response = requests.request(
        "POST", convert_env('proxy_url'), headers=headers, cookies=cookies, data=payload)
    r = json.loads(response.text)
    r = json.loads(r['data']['result'])
    if log is True:
        print("response:" + json.dumps(r, indent=4, ensure_ascii=False))
        print(
            "=============================================================================================================")
    return r


def proxy_req_param(data: dict, url, log, name=''):
    return proxy_req({}, req_param_build(data, url, log, name), log, name)
