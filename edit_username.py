import json

#edit_username(新用户名，QQ，素材存放位置) 返回值str（提示信息）

def edit_username(new_user_name, ID, loc = ''):
    msg_fail = '有点新意好不好嘛'
    msg_success = '更改成功~'
    msg_unregiter = '请先注册'
    
    filename = loc + '用户数据\\user.txt'
    try:
        with open(filename) as file_object:
            user_list = json.load(file_object)
    except:
        with open(filename, 'w') as file_object:
            json.dump({}, file_object)
    if str(ID) in user_list.keys():
        if new_user_name == user_list[str(ID)]:
            return msg_fail
        else:
            user_list[str(ID)] = new_user_name
            with open(filename, 'w') as file_object:
                json.dump(user_list, file_object)
            return msg_success
    else:
        return msg_unregiter
