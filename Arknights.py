import time
from look_for import look_for
from register import register
from item import item_add
from item import item_del
from item import item_check


register('admin','admin_id')
while(1):
    time.sleep(1)
    print(look_for('admin_id'))
    print(item_add('admin_id' ,'测试物品'))
    print(item_del('admin_id' ,'测试物品'))
    print(item_check('admin_id'))
