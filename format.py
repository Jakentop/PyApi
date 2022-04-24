import pandas as pd

def base_result_format(res):
  """公共返回状态"""
  print("接口调用返回信息：")
  return pd.DataFrame({
    "是否成功":[res['success']],
    "状态码":[res['code']],
    "消息":[res['message']]
  })