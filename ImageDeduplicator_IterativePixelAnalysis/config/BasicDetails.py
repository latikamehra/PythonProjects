'''
Created on Aug 20, 2019

@author: latikamehra
'''


detDict = {}

#detDict['fetch'] = {'Shape' : getattr(tp, 'shape'), 'Dimensions' : getattr(tp, 'ndim'), 'Size' : getattr(tp, 'size')}

#detDict['fetch'] = {'Shape' : 'shape', 'Dimensions' : 'ndim', 'Size' :  'size'}

detDict['compare'] = ['Height', 'Width']

detDict['imgio'] = {'Height' : lambda pic : getattr(pic, 'shape')[0] , 
                    'Width' : lambda pic : getattr(pic, 'shape')[1], 
                    'Layers' : lambda pic : getattr(pic, 'shape')[2] if len(getattr(pic, 'shape')) > 2 else 1}

detDict['exif'] = {'DateTimeOriginal' : lambda img : img['DateTimeOriginal'],
                   'DateTime' : lambda img : img['DateTime'] }

detDict['construct'] = {'Image' : None}

detDict['all'] = detDict['imgio'].copy()

#detDict['all'].update(detDict['exif'])

detDict['all'].update(detDict['construct'])