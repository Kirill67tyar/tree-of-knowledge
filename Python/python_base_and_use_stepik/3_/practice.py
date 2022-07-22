from pprint import pprint as pp

# ---------------------------------- analizetools
from analizetools.analize import *

#     'p_dir', 'p_mro',
#     'p_glob', 'p_loc', 'p_type',
#     'p_content', 'show_doc',
#     'delimiter', 'show_builtins',
# ---------------------------------- analizetools


import time


start = time.time()
r = list(range(1000000))
def compare(calc):
    start = time.time()
    ls = calc()
    ls.append(10000000000)
    return time.time() - start

def buit_in_func():
    return list(map(str, r))
def ls_comp():
    return [str(i) for i in r]

data = []
for i in range(100):
    # data.append(compare(buit_in_func))
    data.append(compare(ls_comp))

print(sum(data))
print(sum(data)/len(data))

"""
для map 
X10
# 1.6098692417144775
# 0.16098692417144775
X100
15.379510402679443
0.15379510402679444


для list comprohension X10
1.766075849533081
0.1766075849533081
X100
18.53659987449646
0.1853659987449646
"""

