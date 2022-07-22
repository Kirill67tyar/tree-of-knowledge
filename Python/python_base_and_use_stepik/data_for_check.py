# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())

from pprint import pprint as pp
import sys
import builtins

"""
Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No

----------------------------------------------------------------
10
classA : classB classC classD classG classH
classB : classC classE classG classH classK classL
classC : classE classD classH classK classL
classE : classD classF classK classL
classD : classG classH
classF : classK
classG : classF
classH : classL
classK : classH classL
classL
38
classK classD
classD classA
classG classD
classH classA
classE classE
classH classG
classE classL
classB classD
classD classL
classD classG
classD classE
classA classF
classA classC
classK classA
classA classH
classK classD
classH classB
classK classB
classD classL
classG classG
classA classH
classK classL
classG classE
classB classA
classC classK
classK classL
classC classL
classG classC
classD classD
classC classG
classE classA
classF classK
classB classG
classH classL
classL classF
classH classG
classD classA
classH classL
{'classE': ['classD', 'classF', 'classK', 'classL'], 'classH': ['classL'], 'classK': ['classH', 'classL'], 'classG': ['classF'], 'classC': ['classE', 'classD', 'classH', 'classK', 'classL'], 'classB': ['classC', 'classE', 'classG', 'classH', 'classK', 'classL'], 'classA': ['classB', 'classC', 'classD', 'classG', 'classH'], 'classF': ['classK'], 'classD': ['classG', 'classH'], 'classL': []}
Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
Yes
No
No
Yes
No
Yes
Yes
Yes
No
Yes
No
No
Yes
Yes
No
No
No
Yes
Yes
No
Yes
No
No
No
Yes
Yes
Yes
No

"""

yes_no = """
Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
Yes
No
No
Yes
No
Yes
Yes
Yes
No
Yes
No
No
Yes
Yes
No
No
No
Yes
Yes
No
Yes
No
No
No
Yes
Yes
Yes
No
"""
yes_no = enumerate(yes_no.split('\n'))
for i, ans in yes_no:
    print(f'{i} - {ans}')