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
        if len(x[0]) > 1:
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
# xhj_d = {'xiaohuangji': xhj_l2}
# sample_name = datetime.now().strftime('%Y%m%d-%H%M')
file_name = 'xhj45/xiaohuangji_'+'for_tuling'
# xhj_d1 = {'xiaohuangji_query': [x[0] for x in xhj_l4]}
xhj_l5 = list(set([x[0] for x in xhj_l4]))
with open(file_name, 'w') as f:
    # json.dump(xhj_d1, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))
    f.writelines('\n'.join(xhj_l5))

# dst_file_name = '/Users/fhr/anaconda/lib/python3.6/site-packages/chatterbot_corpus/data/chinese/xhj45/xiaohuangji'\
#                 +sample_name
# copyfile(file_name, dst_file_name)
