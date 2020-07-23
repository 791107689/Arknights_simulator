import json
import os


def account_termination(ID, loc=''):
    '''删除一个账户。'''
    filename = loc + '用户数据\\user.txt'
    if not os.path.exists(filename):
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
    with open(filename) as file_object:
        user_list = json.load(file_object)

    if str(ID) in user_list.keys():
        user_name = user_list[ID]
        del(user_list[ID])
        with open(filename, 'w') as file_object:
            json.dump(user_list, file_object)
        filename = loc + '用户数据\\' + str(ID) + '.json'
        os.remove(filename)
        return 'Dr.' + user_name + '已离职，相关档案已销毁且无法恢复'
    else:
        return '用户不存在'
