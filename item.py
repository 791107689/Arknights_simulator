import json
from register import new_Dr

#item_add(QQ,物品名称，素材位置，添加数量)

def item_add(ID ,item_name:str , loc:str = '' , n:int = 1):
    #TODO:用os.exists改写所有try语句，因为try语句虽然能捕获异常，但是太低效了

    #检查用户注册
    filename = loc+ '用户数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            file_object.close()
    except FileNotFoundError:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    #读取数据
    filename = loc+ '用户数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
            file_object.close()
    except FileNotFoundError:
        with open(filename, 'w') as file_object:
            user_data = new_Dr()
            json.dump(user_data, file_object)
            file_object.close()

    #更改数据
    if item_name in user_data:
        user_data['物品'][item_name] += n
    else:
        user_data['物品'][item_name] = n


    #更改数据
    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object)
        file_object.close()

    return '成功添加' + item_name + '*' + str(n)


def item_del(ID ,item_name:str , loc = '' , n = 10000):
    #检查用户注册
    filename = loc+ '用户数据\\' + ID + '.json'

    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
            file_object.close()
    except FileNotFoundError:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    #读取数据
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
            file_object.close()
    except FileNotFoundError:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
            file_object.close()

    #更改数据
    if not (item_name in user_data)or(user_data[item_name] - n < 0):
        return item_name + '数量不足'
    else:
        user_data[item_name] -= n

    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object)
        file_object.close()
    return '成功删除' + item_name + '*' + str(n)

def item_check(ID ,loc = '' ):
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    #检查用户注册
    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
            file_object.close()
    except FileNotFoundError:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    #读取数据
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
            file_object.close()
    except FileNotFoundError:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
            file_object.close()

    try:
        return str(user_data)
    except KeyError:
        return '无物品'#TODO:这段没看懂：user_data不是个字典吗？str一个字典为什么会KeyError
