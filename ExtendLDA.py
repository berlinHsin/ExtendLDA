#encoding:utf-8

import numpy , pickle , lda  

class ExtendLDA(lda.LDA):
    def __init__(self,*args):
        pass
    def saveModel(self, obj,filename):
        with open(filename,'wb') as output :
            pickle.dump(obj , output , -1)
    def loadModel(self,filename) :
        file = open(filename,'rb')
        obj = pickle.load(file)
        file.close()
        return obj
    def saveDict(self , dictionary ,filename):
        file = open(filename,'w') 
        for term in dictionary :
            file.write(term+'\n')
        file.close()
    def loadDict(self , filename):
        dictionary = []
        file = open(filename,'r')
        for line in file.readlines():
            dictionary.append(line[:-1])
        file.close()
        return dictionary
    def saveMm(self , Mm , filename):
        numpy.save(filename,Mm) 
    def loadMm(self , filename):
        return numpy.load(filename)
    def showTopic(self,model,dictionary,num=8):
        for i , topic_dist in enumerate(model.topic_word_):
            topic_words = numpy.array(dictionary)[numpy.argsort(topic_dist)][:-num:-1]
            print("Topic {} : {}".format(i , " ".join(topic_words)))

