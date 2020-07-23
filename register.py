import json


def new_Dr():
    '''生成一个空用户.'''
    return {'标准寻访次数': 0,
            '干员列表': {},
            '物品': {}
            }


def register(user_name, ID, loc=''):
    '''注册新用户
    register（用户名，QQ号，素材存放位置） 根据用户QQ判断是否注册过 返回str（提示信息）'''
    filename = loc + '用户数据\\user.txt'
    try:
        with open(filename) as file_object:
            user_list = json.load(file_object)
    except:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
    if str(ID) in user_list.keys():
        return '用户已注册'
    else:
        user_list[str(ID)] = user_name
        with open(filename, 'w') as file_object:
            json.dump(user_list, file_object)
        filename = loc + '用户数据\\' + str(ID) + '.json'
        with open(filename, 'w') as file_object:
            json.dump(new_Dr(), file_object)
        return 'Dr.' + user_name
