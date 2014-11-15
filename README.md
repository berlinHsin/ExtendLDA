ExtendLDA
=========

This is just a little extension of lda 

Reference : https://pypi.python.org/pypi/lda

I create some function for better use , including :
  
  1. saveMm -> save matrix of word occurence  . Input : ([[0,1,....]...],filename)
  2. loadMm -> load matrix of word occurence  . Input : (filename) , Output: numpy.array([[0,1,...]...])
  3. saveDict -> save dictionary of word .      Input : (['banana','word'....],filename) 
  4. loadDict -> load dictionary of word .      Input : (filename) ,  Output(['banana','word'....])
  5. saveModel -> save LDA model .              Input : (model, filename) 
  6. loadModel -> load LDA model .              Input : (filename) , Output(model)
  7. showTopic -> show topics that trained by lda .  Input : (model , dictionary , num=8) 


--

I think there would be better way to extend lda module , but I'm not good at this .
If you have better way , just clone and modify it , thanks!
