import time

from look_for import look_for
from register import register

loc = ''
#loc = 'C:\\BaiduNetdiskDownload\\方舟模拟器\\Arknights\\Arknights\\'
#素材绝对路径

register('admin','admin_id')
while(1):
    time.sleep(1)
    print(look_for('admin_id'))