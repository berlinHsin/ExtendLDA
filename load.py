#encoding:utf-8

import ExtendLDA 
ExtendLDA = ExtendLDA.ExtendLDA()

model = ExtendLDA.loadModel('deer.pkl')
dictionary = ExtendLDA.loadDict('deer.dict')

ExtendLDA.showTopic(model,dictionary)

