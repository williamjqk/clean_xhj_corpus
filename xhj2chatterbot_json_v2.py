import chatterbot
import json
import re
from shutil import copyfile
from datetime import datetime

# test1 = [['你好','我不好'],['你说啥','呵呵']]
# dict1 = {'mycorpus': test1}
# json.dumps(dict1, ensure_ascii=True or False)

data_path = '/Users/fhr/Documents/dataset/'
xhj_filename = data_path + 'xiaohuangji50w_nofenci.conv'

with open(xhj_filename, 'r') as f:
    xhj_input = f.read()

xhj_l = xhj_input.split('\nE')
# re.split('M |\n',xhj_l[-1])
xhj_l2 = [[x2 for x2 in re.split('\nM ', x1) if x2] for x1 in xhj_l if x1]
len(xhj_l2)
q_l = [x[0] for x in xhj_l2]
q_set = set(q_l)
len(q_set)


xhj_l3 = []
for x in xhj_l2:
    # print(x)
    if len(x) != 2:
        continue
    if re.search('[\u4e00-\u9fa5]', x[0])!=None and re.search('[\u4e00-\u9fa5]', x[1])!=None:
        if len(x[0]) > 2:
            xhj_l3.append(x)
print(len(xhj_l3))

# num = 2
# list1 = [1,2,3,4]
# import random
# random.sample(list1,num)
# re.search('a','bc') == None
num = -1#20000
import random
if num > 0:
    xhj_l4 = random.sample(xhj_l3,num)
else:
    xhj_l4 = xhj_l3
xhj_d = {'xiaohuangji': xhj_l2}
sample_name = datetime.now().strftime('%Y%m%d-%H%M')
file_name = 'xhj45/xiaohuangji_'+sample_name
xhj_d1 = {'xiaohuangji_sample': xhj_l4}
with open(file_name, 'w') as f:
    json.dump(xhj_d1, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))

dst_file_name = '/Users/fhr/anaconda/lib/python3.6/site-packages/chatterbot_corpus/data/chinese/xhj45/xiaohuangji'\
                +sample_name
copyfile(file_name, dst_file_name)

# from datetime import datetime
# type(datetime.now().strftime('%Y%m%d-%H%M'))
# datetime.now().strftime('%Y%m%d-%H%M')
# %%
# xhj_l2[2760:2763]
# dict1 = {}
# count = 0
# for qa in xhj_l2:
#     # print(qa[0], qa[1])
#     count += 1
#     # print(count)
#     if len(qa) != 2:
#         continue
#     if qa[0] not in dict1:
#         dict1[qa[0]] = {'response': [qa[1]], 'r_count': 1}
#     else:
#         dict1[qa[0]]['response'].append(qa[1])
#         dict1[qa[0]]['r_count'] += 1
# len(dict1)
#
# dict2 = {}
# for qa in xhj_l2:
#     # print(qa[0], qa[1])
#     count += 1
#     # print(count)
#     if len(qa) != 2:
#         continue
#     if qa[1] not in dict2:
#         dict2[qa[1]] = {'response': [qa[0]], 'r_count': 1}
#     else:
#         dict2[qa[1]]['response'].append(qa[0])
#         dict2[qa[1]]['r_count'] += 1
# len(dict2)
# dict2['= =']
#
#
# def gen_corpus_dict(q_l):
#     return









#
#
# # %%
# xhj_d = {'xiaohuangji': xhj_l2}
# # with open('xiaohuangji.corpus.json', 'w') as f:
# #     # json.dump(xhj_d, f, ensure_ascii=False)
# #     json.dump(xhj_d, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))
# num = 45
# size = int(len(xhj_l2)/num)
# for i in range(45):
#     file_name = 'xhj45/xiaohuangji'+str(i+1)
#     xhj_d1 = {'xiaohuangji'+str(i+1): xhj_l2[i*size:(i+1)*size]}
#     with open(file_name, 'w') as f:
#         json.dump(xhj_d1, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))
