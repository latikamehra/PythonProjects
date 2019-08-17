'''
Created on Aug 15, 2019

@author: latikamehra
'''

tagList = {}

tagList['collect'] = ['DateTimeOriginal', 'Model', 'WhiteBalance', 'MeteringMode', 'Flash', 'ColorSpace', 'ExifImageHeight']

tagList['compare'] = ['DateTimeOriginal', 'Model', 'WhiteBalance', 'MeteringMode', 'Flash', 'ColorSpace']

tagList['required'] = ['DateTimeOriginal']


tagList['all'] = ['DateTimeOriginal', 'Model', 'ExposureTime', 'CompressedBitsPerPixel', 'ShutterSpeedValue', 
           'ApertureValue', 'ExposureBiasValue', 'MaxApertureValue', 'MeteringMode', 'Flash', 'FocalLength', 'ColorSpace', 
           'ExifImageWidth',  'FocalPlaneXResolution', 'Orientation', 'YCbCrPositioning', 'ExifImageHeight', 
           'FocalPlaneYResolution', 'FocalPlaneResolutionUnit', 'SensingMethod', 'XResolution', 'YResolution', 
            'FNumber', 'CustomRendered', 'ResolutionUnit', 'ExposureMode', 'FlashPixVersion', 'WhiteBalance',
             'DigitalZoomRatio', 'SceneCaptureType', 'ExifOffset']