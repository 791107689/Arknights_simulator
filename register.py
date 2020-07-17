import json

def register(user_name,ID,loc = ''):
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
            json.dump({'标准寻访次数':0}, file_object)
        return 'Dr.' + user_name
