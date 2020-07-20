import json
import os


def account_termination(ID, loc = ''):
    filename = loc + '用户数据\\user.txt'
    try:
        with open(filename) as file_object:
            user_list = json.load(file_object)
    except:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
    if str(ID) in user_list.keys():
        user_name = user_list[ID]
        del user_list[ID]
        with open(filename, 'w') as file_object:
            json.dump(user_list, file_object)
        filename = loc + '用户数据\\' + str(ID) + '.json'
        os.remove(filename)
        print('Dr.' + user_name + '已离职，相关档案已销毁且无法恢复')
    else:
        print('用户不存在')    