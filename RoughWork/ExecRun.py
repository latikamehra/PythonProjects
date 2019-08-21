'''
Created on Aug 20, 2019

@author: latikamehra
'''

import ParentClass
import ChildClass1
import ChildClass2

dir1 = "A"
dir2 = "B"
dir3 = "C"
dir4 = "D"

pc = ParentClass.Manage(dir1, dir2)

cc1 = ChildClass1.Child1(pc)
cc1.prnt1(dir3)

cc2 = ChildClass2.Child2(pc)
cc2.prnt1(dir3)