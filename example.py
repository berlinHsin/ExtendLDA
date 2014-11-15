#encoding:utf-8

import pymongo , numpy , ExtendLDA , lda

ExtendLDA = ExtendLDA.ExtendLDA()

client   = pymongo.MongoClient('localhost',27017)
db       = client.III
collections = db.blog
cursor = collections.find({})

titles = []
datas  = []
terms  = []
X      = []


for i in cursor :
    titles.append(i['title'])
    datas.append(i)
    for v in i['terms'] :
        if v[0].lower() in terms :
            continue 
        else :
            terms.append(v[0].lower())

for i in datas :
    vocab = dict(i['terms'])
    tmp = []
    for t in terms :
        if t.lower() in vocab :
            tmp.append(vocab[t])
        else :
            tmp.append(0)
    X.append(tmp)

X = numpy.array(X)

ExtendLDA.saveMm(X,'deer')
ExtendLDA.saveDict(terms,'deer.dict')

model = lda.LDA(n_topics=6 , n_iter = 10 , random_state= 1)
model.fit(X)
ExtendLDA.saveModel(model,'deer.pkl')
