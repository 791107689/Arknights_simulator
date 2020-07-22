import json

#item_add(QQ,物品名称，素材位置，添加数量)

def item_add(ID ,item_name , loc = '' , n = 10000):
    #检查用户注册
    filename = loc+ '用户数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            file_object.close()
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    #读取数据
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
            file_object.close()
    except FileNotFoundError as e:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
            file_object.close()
        user_date = {}
    #更改数据
    try:
        user_date[str(item_name)] += n
    except KeyError as e:
        try:
            user_date[str(item_name)] = n
        except KeyError as e:
            user_date = {}
            user_date[str(item_name)] = n

    
    #更改数据
    with open(filename, 'w') as file_object:
        json.dump(user_date, file_object)
        file_object.close()

    return '成功添加' + str(item_name) + '*' + str(n)


def item_del(ID ,item_name , loc = '' , n = 10000):
    #检查用户注册    
    filename = loc+ '用户数据\\' + ID + '.json'

    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
            file_object.close()
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    #读取数据
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
            file_object.close()
    except FileNotFoundError as e:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
            file_object.close()
    #更改数据
    try:
        if (user_date[str(item_name)] - n) < 0 :
            return str(item_name) + '数量不足'
        else:
            user_date[str(item_name)] -= n
    except KeyError as e:
        return str(item_name) + '数量不足'

    with open(filename, 'w') as file_object:
        json.dump(user_date, file_object)
        file_object.close()
    return '成功删除' + str(item_name) + '*' + str(n)

def item_check(ID ,loc = '' ):
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    #检查用户注册   
    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
            file_object.close()
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    #读取数据
    filename = loc+ '用户数据\\物品数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
            file_object.close()
    except FileNotFoundError as e:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
            file_object.close()

    try:
        return str(user_date)
    except KeyError as e:
        return '无物品'
