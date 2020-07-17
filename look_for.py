
import random
import json



def look_for(ID,loc = ''):

    inf = {}   

    six_star = 0.02
    five_star = 0.08
    four_star = 0.5
    three_star = 0.4

    filename = loc+ '用户数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_date = json.load(file_object)
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    n = user_date['标准寻访次数']


    real_six_star = six_star*n + six_star
    real_five_star = ( (1-real_six_star) / (1-six_star) ) * five_star
    real_four_star = ( (1-real_six_star) / (1-six_star) ) * four_star
    real_three_star = ( (1-real_six_star) / (1-six_star) ) * three_star

    n += 1
    user_date['标准寻访次数'] = n


    with open(filename, 'w') as file_object:
        json.dump(user_date, file_object)

    p = random.random()

    if p <= real_six_star:
        filename = loc + r'标准寻访\标准寻访_六星.txt'
        user_date['标准寻访次数'] = 0
        inf['稀有度'] = '★★★★★★'
    elif p <= ( real_six_star + real_five_star ):
        filename = loc + r'标准寻访\标准寻访_五星.txt'
        inf['稀有度'] = '★★★★★'
    elif p <= ( real_six_star + real_five_star + real_four_star ):
        filename = loc + r'标准寻访\标准寻访_四星.txt'
        inf['稀有度'] = '★★★★'
    else:
        filename = loc + r'标准寻访\标准寻访_三星.txt'
        inf['稀有度'] = '★★★'
        
    with open(filename) as file_object:
        str = file_object.read()
        
    card_list = []
    card = ''

    for s in str:
        if s !=  '/':
            card += s
        else:
            card_list.append(card)
            card = ''
    print(card_list)
    filename = loc+ '用户数据\\' + ID + '.json'
    with open(filename, 'w') as file_object:
        json.dump(user_date, file_object)
    
    inf['干员'] = random.choice(card_list)

    return inf
