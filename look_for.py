from item import item_add
from PIL import Image
import random
from time import time
import json

from base import Agent, AgentList, Dr

#初始化随机数发生器
random.seed(time())

#-----------------------------------------------------------------------------------

#look_for(QQ,素材位置) 寻访 返回值为储存干员信息的dict
#look_for_ten(QQ,素材位置) 十连 返回值为list（储存十连结果） 并生成十连结果图像（但图像存在问题）

def look_for(ID,loc = ''):

    # inf(dict)为该次抽取的干员信息
    # '干员'(str):干员名称
    # '稀有度'(str):干员稀有度，用"★"的数量表示
    inf = Agent()

    # 干员爆率
    six_star = 0.02
    five_star = 0.08
    four_star = 0.5
    three_star = 0.4

    # 获取用户数据
    filename = loc+ '用户数据\\' + ID + '.json'
    try:
        with open(filename) as file_object:
            user_data = Dr(json.load(file_object))
    except FileNotFoundError:
        return '请先注册账号\n注册方式：发送“注册 这里填用户名”'
    n = user_data['标准寻访次数']

    # 计算真实爆率
    if n > 50:
        real_six_star = six_star*(n - 50) + six_star
        real_five_star = ( (1-real_six_star) / (1-six_star) ) * five_star
        real_four_star = ( (1-real_six_star) / (1-six_star) ) * four_star
        real_three_star = ( (1-real_six_star) / (1-six_star) ) * three_star
    else:
        real_six_star = 0.02
        real_five_star = 0.08
        real_four_star = 0.5
        real_three_star = 0.4

    # 更新用户标准寻访次数
    n += 1
    user_data['标准寻访次数'] = n
    with open(filename, 'w') as file_object:
        json.dump(user_data, file_object,ensure_ascii=False,indent=4,separators=(',',':'))

    # 决定欧非
    p = random.random()
    if p <= real_six_star:
        filename = loc + r'标准寻访\标准寻访_六星.json'
        user_data['标准寻访次数'] = 0 #保底计算相关
        inf['稀有度'] = '★★★★★★'
    elif p <= ( real_six_star + real_five_star ):
        filename = loc + r'标准寻访\标准寻访_五星.json'
        inf['稀有度'] = '★★★★★'
    elif p <= ( real_six_star + real_five_star + real_four_star ):
        filename = loc + r'标准寻访\标准寻访_四星.json'
        inf['稀有度'] = '★★★★'
    else:
        filename = loc + r'标准寻访\标准寻访_三星.json'
        inf['稀有度'] = '★★★'

    # 获取抽中星级干员列表
    with open(filename,'r') as file_object:
        card_list=json.load(file_object)

    # 抽取干员
    inf['干员'] = random.choice(card_list)
    # inf即为抽取到的干员

    # 获取或初始化干员数据
    try:
        if not (inf['干员'] in [i['干员'] for i in user_data['干员列表']]):
            user_data['干员列表'].append(inf)
    except:
        user_data['干员列表'] = AgentList()
        user_data['干员列表'].append(inf['干员'])
    finally:
        # 搜索整个干员列表，查看该干员是否被抽到过
        filename = loc+ '用户数据\\' + ID + '.json'
        for i in user_data['干员列表']:
            if i['干员'] == inf['干员']:
                #给予物品
                if '获取次数' in i.keys():
                    i['获取次数'] += 1
                    inf['获取次数']=i['获取次数']
                    #更新用户数据
                    with open(filename, 'w') as file_object:
                        json.dump(user_data, file_object)
                    item_add(ID, inf['干员'] + '的信物', loc, 1)  #非首次一定掉落信物
                    if (inf['稀有度'] == '★') or (inf['稀有度'] == '★★'):#中低星级非首次掉落恒定资质凭证
                        item_add(ID, '资质凭证', loc, 1)
                    elif inf['稀有度'] == '★★★':
                        item_add(ID, '资质凭证', loc, 5)
                    elif inf['稀有度'] == '★★★★':
                        item_add(ID, '资质凭证', loc, 30)
                    #高星阶2~6次及>7次掉落不同数量高级凭证
                    elif inf['稀有度'] == '★★★★★':
                        if i['获取次数'] in range(2, 7):
                            item_add(ID, '高级凭证', loc, 5)
                        elif i['获取次数'] > 6:
                            item_add(ID, '高级凭证', loc, 8)
                    elif inf['稀有度'] == '★★★★★★':
                        if i['获取次数'] in range(2, 7):
                            item_add(ID, '高级凭证', loc, 10)
                        elif i['获取次数'] > 6:
                            item_add(ID, '高级凭证', loc, 15)
                else:
                    i['获取次数'] = 1
                    inf['获取次数']=i['获取次数']
                    #更新用户数据
                    with open(filename, 'w') as file_object:
                        json.dump(user_data, file_object)
                    item_add(ID, '高级凭证', loc, 1)#首次抽中掉落干员及高级凭证*1

    return inf

#-----------------------------------------------------------------------------------

def look_for_ten(ID,loc = ''):
    result = AgentList()

    for i in range(10):
        result.append(look_for(ID,loc))

    size_x = 185
    size_y = 450
    box = (415, 0, 415 + size_x ,0 + size_y)
    target = Image.new('RGBA', (size_x*10 , size_y))

    for i in range(10):
        pic = loc + '立绘\\' + str(result[i]['干员']) + '.png'
        img = Image.open(pic)
        region = img.crop(box)
        target.paste(region, (i * size_x, 0, i * size_x + size_x, size_y))


    target.save('result.png')
    return result

#猎蜂、阿消、空爆立绘已修正
