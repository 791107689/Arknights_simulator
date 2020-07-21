import json

#item_add(QQ,物品名称，素材位置，添加数量) 
#item_del(QQ,物品名称，素材位置，删除数量)
#item_check(QQ,素材位置)
#均返回str（提示信息）
def item_add(ID ,item_name , loc = '' , n = 10000):
    
    filename = loc+ '用户数据\\' + ID + '.json'

    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'

    try:
        user_data['物品'][str(item_name)] += n
    except KeyError as e:
        user_data['物品'] = {}
        user_data['物品'][str(item_name)] = n

    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object)
    return '成功添加' + str(item_name) + '*' + str(n)


def item_del(ID ,item_name , loc = '' , n = 10000):
    
    filename = loc+ '用户数据\\' + ID + '.json'

    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'

    try:
        if (user_data['物品'][str(item_name)] - n) < 0 :
            return str(item_name) + '数量不足'
        else:
            user_data['物品'][str(item_name)] -= n
    except KeyError as e:
        return str(item_name) + '数量不足'

    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object)
    return '成功删除' + str(item_name) + '*' + str(n)

def item_check(ID ,loc = '' ):
    filename = loc+ '用户数据\\' + ID + '.json'

    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    try:
        return str(user_data['物品'])
    except KeyError as e:
        return '无物品'
