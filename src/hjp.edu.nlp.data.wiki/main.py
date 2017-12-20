#-*- coding: UTF-8 -*- 
'''
Created on Dec 19, 2017

@Author: hjp

Description: Extracting EnWikipedia files into single text.
'''

from gensim.corpora import WikiCorpus


def enwiki(srcPath, tarPath):
    index = 0
    space = " "    
    
    output = open(tarPath, 'w')
    wiki = WikiCorpus(srcPath, lemmatize=False, dictionary={})
    
    for text in wiki.get_texts():
        output.write(' '.join(text) + '\n')
        index += 1
        if (index % 10000 == 0):
            print("Saved " + str(index) + " articles.")
            
    output.close()
    print("Finished saved " + str(index) + " articles.")
        
    
if __name__ == '__main__':
    srcPath = "/home/hjp/Downloads/model/w2v/enwiki-20171201-pages-articles.xml.bz2"
    tarPath = "/home/hjp/Downloads/model/w2v/enwiki.txt"
    enwiki(srcPath, tarPath)
