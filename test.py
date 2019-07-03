import nltk
from nltk import word_tokenize
import os,sys
#nltk.download('punkt')

pcorpus = dict()
pcorpus1 = dict()

lines_lang1 = open("data_lang1.txt", "r").readlines()
lines_lang2 = open("data_lang2.txt", "r").readlines()

# lines_lang1 = open("d:\Download\EM_Translation-master\data_lang1.txt", "r").readlines()
# lines_lang2 = open("d:\Download\EM_Translation-master\data_lang2.txt", "r").readlines()

for line1, line2 in zip(lines_lang1, lines_lang2):
    sentence1 = tuple(word_tokenize("NULL " + line1.strip("\n")))
    sentence2 = tuple(word_tokenize("NULL " + line2.strip("\n")))
    pcorpus[sentence1] = sentence2
#print (pcorpus)

forDic={}
engDic={}
for i in pcorpus.keys():
        for word in i:
                engDic[word]=0
        for word in pcorpus[i]:
                forDic[word]=0
translation_probs = {}
for en in engDic.keys():
        translation_probs[en]={}
        for fo in forDic.keys():
                translation_probs[en][fo]=round(1.0/len(engDic),3)
                translation_probs[en][fo]=0.1

def init_params():
        totalf={}
        count={}
        for i in forDic.keys():
                totalf[i]=0
        for i in engDic.keys():
                count[i]={}
                for j in forDic.keys():
                        count[i][j]=0
        return totalf,count
#print(translation_probs["ok-voon"])
#{'NULL': 0.04, 'at-voon': 0.19, 'bichat': 0.08, 'dat': 0.07, 'at-drubel': 0.17, 'pippat': 0.11, 'rrat': 0.08, 'krat': 0.08, 'sat': 0.17, 'lat': 0.08}

num_epochs = 10

for i in range(num_epochs):
        stotal={}
        totalf,count = init_params()
        for sen in pcorpus.keys():
                for eword in sen:
                        stotal[eword]=0
                        for fword in pcorpus[sen]:
                                stotal[eword]+=translation_probs[eword][fword]
                for eword in sen:
                        for fword in pcorpus[sen]:                               
                                # stotal(e1)=t(e1|f1)+t(e1|f2)...t(e1|fn)
                                # count(e1|f1)=t(e1|f1)/stotal(e1)，是翻译成e1的所有f中，f1翻译成e1的比例
                                count[eword][fword]+=translation_probs[eword][fword]/stotal[eword]
                                totalf[fword]+=translation_probs[eword][fword]/stotal[eword]
        for fword in forDic.keys():
                for eword in engDic.keys():
                        translation_probs[eword][fword]=count[eword][fword]/totalf[fword]
                        # 这里的totalf是对应于count的求和
                        # 例如t(e1|f1)=count(e1|f1)/sum(count(e|f1)) 表示在f1翻译成所有e中，f1翻译成e1的比例
                        # temp=0
                        # for e in engDic.keys():
                        #         temp+=count[e][fword]
                        # print(temp-totalf[fword]) 0

print(translation_probs)