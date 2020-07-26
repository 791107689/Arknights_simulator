'''base.py定义了Arknight_Simulator各功能所需要用到的数据类型。
   主要是对输出进行了美观处理。
'''
#干员
class Agent(dict,):
    def __init__(self, *args, **kwargs):
        #name=干员，rare=稀有度，times=获取次数
        l = len(args)
        if l > 0:
            if isinstance(args[0], dict):
                self.update(args[0])
            else:
                self['干员'] = args[0]
        if l > 1:
            self['稀有度'] = args[1]
        if l > 2:
            self['获取次数'] = args[2]

        if 'name' in kwargs:
            self['干员'] = kwargs['name']
        if 'rare' in kwargs:
            self['稀有度'] = kwargs['rare']
        if 'times' in kwargs:
            self['获取次数'] = kwargs['times']

    def __str__(self):
        s = self['干员'] + ' ' + self['稀有度']
        if '获取次数' in self.keys():
            s = s + ' (' + str(self['获取次数']) + ')'
        return s

#干员列表
class AgentList(list,):
    def __init__(self, init_value: list = []):
        for i in init_value:
            self.append(Agent(i))

    def __str__(self):
        return '\n - '+'\n - '.join([str(i) for i in self])

#物品列表
class ItemList(dict,):
    def __init__(self, init_value: dict = {}):
        self.update(init_value)

    def __str__(self):
        return '\n - '+'\n - '.join([str(i[0]) + ' : ' + str(i[1]) for i in self.items()])

#用户
class Dr(dict,):
    def __init__(self, init_value: dict = {}):
        if init_value == {}:
            init_value={
                '标准寻访次数': 0,
                '干员列表': AgentList(),
                '物品': ItemList()
            }
        self.update(init_value)
        if not isinstance(self['干员列表'], AgentList):
            self['干员列表'] = AgentList(self['干员列表'])
        if not isinstance(self['物品'], ItemList):
            self['物品']=ItemList(self['物品'])

    def __str__(self):
        return '\n'.join([str(i[0]) + ' : ' + str(i[1]) for i in self.items()])
