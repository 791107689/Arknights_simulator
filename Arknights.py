import time
from look_for import look_for_ten
from register import register
from item import item_add
from item import item_del
from item import item_check

loc = ''

register('admin','admin_id')
#进行测试
print(look_for_ten('admin_id'))
print(item_add('admin_id' ,'测试物品'))
print(item_del('admin_id' ,'测试物品'))
print(item_check('admin_id'))
