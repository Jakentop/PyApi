from function import *

# template
def query_track_detail(data, log=True):
    """查询跟踪单详情"""
    url = convert_env('demo') + '/'
    return invoke(data, url, log)
