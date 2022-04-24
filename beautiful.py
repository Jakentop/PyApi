from typing import Dict
import json
from IPython.display import display_javascript,display,display_html,Javascript,HTML
import uuid
from string import Template
import re

f=open('template.html','r',encoding='utf8')
template=f.read()
f.close()
def render(data:dict):
    if isinstance(data,Dict):
        data=json.dumps(data,ensure_ascii=False,indent=2)
    id=str(uuid.uuid4()).replace('-','')
    # print(re.findall("\n",data))
    height='350px' if len(re.findall("\n",data))>30 else 'auto'
    params={
        "uid":id,
        "data":data,
        "height":height
    }
    txt=Template(template).substitute(**params)
    display(HTML(data=txt))