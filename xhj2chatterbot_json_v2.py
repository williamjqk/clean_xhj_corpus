import chatterbot
import json
import re
# test1 = [['你好','我不好'],['你说啥','呵呵']]
# dict1 = {'mycorpus': test1}
# json.dumps(dict1, ensure_ascii=True or False)

data_path = '/Users/fhr/Documents/dataset/'
xhj_filename = data_path + 'xiaohuangji50w_nofenci.conv'

with open(xhj_filename, 'r') as f:
    xhj_input = f.read()

xhj_l = xhj_input.split('E\n')
# re.split('M |\n',xhj_l[-1])
xhj_l2 = [[x2 for x2 in re.split('M |\n', x1) if x2] for x1 in xhj_l if x1]
len(xhj_l2)
q_l = [x[0] for x in xhj_l2]
q_set = set(q_l)
len(q_set)

# %%
xhj_d = {'xiaohuangji': xhj_l2}
# with open('xiaohuangji.corpus.json', 'w') as f:
#     # json.dump(xhj_d, f, ensure_ascii=False)
#     json.dump(xhj_d, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))
num = 45
size = int(len(xhj_l2)/num)
for i in range(45):
    file_name = 'xhj45/xiaohuangji'+str(i+1)
    xhj_d1 = {'xiaohuangji'+str(i+1): xhj_l2[i*size:(i+1)*size]}
    with open(file_name, 'w') as f:
        json.dump(xhj_d1, f, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': '))
