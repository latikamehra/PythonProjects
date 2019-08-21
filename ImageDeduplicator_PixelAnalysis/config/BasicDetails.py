'''
Created on Aug 20, 2019

@author: latikamehra
'''


detDict = {}

#detDict['fetch'] = {'Shape' : getattr(tp, 'shape'), 'Dimensions' : getattr(tp, 'ndim'), 'Size' : getattr(tp, 'size')}

detDict['fetch'] = {'Shape' : 'shape', 'Dimensions' : 'ndim', 'Size' :  'size'}

detDict['construct'] = {'Image' : None}

detDict['all'] = detDict['fetch'].copy()

detDict['all'].update(detDict['construct'])