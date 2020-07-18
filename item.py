import json


def item_add(ID ,item_name , loc = '' , n = 10000):
    
    filename = loc+ '用户数据\\' + ID + '.json'

    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'

    try:
        user_date['物品'][str(item_name)] += n
    except KeyError as e:
        user_date['物品'] = {}
        user_date['物品'][str(item_name)] = n

    with open(filename, 'w') as file_object:
        json.dump(user_date, file_object)
    return '成功添加' + str(item_name) + '*' + str(n)
