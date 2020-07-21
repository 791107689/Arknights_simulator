from PIL import Image
import random
import json

#look_for(QQ,素材位置) 寻访 返回值为储存干员信息的dict
#look_for_ten(QQ,素材位置) 十连 返回值为list（储存十连结果） 并生成十连结果图像（但图像存在问题）

def look_for(ID,loc = ''):

    inf = {}   

    # 干员爆率
    six_star = 0.02
    five_star = 0.08
    four_star = 0.5
    three_star = 0.4

    filename = loc+ '用户数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_data = json.load(file_object)
    except FileNotFoundError as e:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    n = user_data['标准寻访次数']


    real_six_star = six_star*n + six_star
    real_five_star = ( (1-real_six_star) / (1-six_star) ) * five_star
    real_four_star = ( (1-real_six_star) / (1-six_star) ) * four_star
    real_three_star = ( (1-real_six_star) / (1-six_star) ) * three_star

    n += 1
    user_data['标准寻访次数'] = n


    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object)

    p = random.random()

    if p <= real_six_star:
        filename = loc + r'标准寻访\标准寻访_六星.txt'
        user_data['标准寻访次数'] = 0
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
    #print(card_list)

    filename = loc+ '用户数据\\' + ID + '.json'
    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object)
    
    inf['干员'] = random.choice(card_list)

    return inf

def look_for_ten(ID,loc = ''):
    result = []

    for i in range(10):
        result.append(look_for(ID,loc)['干员'])


    size_x = 151
    size_y = 443
    box = (371, 0, 371 + size_x ,0 + size_y)
    target = Image.new('RGB', (size_x*10 , size_y))

    for i in range(10):
        pic = loc + '立绘\\' + str(result[i]) + '.png'
        img = Image.open(pic)
        region = img.crop(box)
        target.paste(region,(i*size_x,0,i*size_x + size_x,size_y))

    target.save('result.png')
    return result

#猎蜂、阿消、空爆立绘已修正
