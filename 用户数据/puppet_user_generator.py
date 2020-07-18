import json
import random
import string

#-----------------------------------------------------------------------------------

# constants
max_len_of_username = 16
smallest_id = 10000
largest_id = 99999999
allowed_characters = string.ascii_letters + string.digits + '-' + '_'

#-----------------------------------------------------------------------------------

# inputs
n_of_users = input('Enter the number of puppet users you want to generate: ')

#-----------------------------------------------------------------------------------

# initialization
puppet_users = {'admin_id':'admin'}  # init users' dictionary

#-----------------------------------------------------------------------------------

# puppet users generation
for i in range(0, int(n_of_users)):
    temp_str = ''  # init temporary string for generating random username
    
    # generate random username with random length from 1 to max_len_of_username
    for j in range(1, max_len_of_username + 1):
        temp_str += random.choice(allowed_characters)
    
    puppet_users[random.randint(smallest_id, largest_id)] = temp_str

#-----------------------------------------------------------------------------------

# json and file handling
with open('用户数据\\user.txt', 'w') as user_file:
    json.dump(puppet_users, user_file)