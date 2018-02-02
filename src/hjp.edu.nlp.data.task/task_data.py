import os
import codecs
from decimal import Decimal
from nltk.tokenize import word_tokenize

DATA_DIR = '/home/hjp/Downloads/semeval/task2/data_es/'
TRAIN_FILE = 'es_train.txt'
DEV_FILE = 'es_dev.txt'
TEST_FILE = 'es_test.txt'
TRAID_DIR = 'train_txt'
DEV_DIR = 'dev_txt'
TEST_DIR = 'test_txt'



def data_split():
    train_file = []
    labels = {}
    count = 0
    train_label = []
    train_file = []
    with open(os.path.join(DATA_DIR, TRAIN_FILE), encoding='utf-8') as fp:
        for lines in fp:
            print(lines)
            label = lines.split()[0].strip()
            txt = lines.replace(label, '')
            if label not in labels:
                labels[label] = len(labels)
            #train_score.append(score)
            count += 1
            # writing '#count.txt' file
            filename = str(count)+'.txt'
            #print(os.path.join(DATA_DIR+TRAID_DIR, filename))
            fp_train = codecs.open(os.path.join(DATA_DIR+TRAID_DIR, filename), 'a+', 'utf-8')
            train_file.append(filename)
            fp_train.write(txt)
            fp_train.close()
            train_label.append(labels[label])
            # record #count label
        fp_file = codecs.open(DATA_DIR+'train_txt.txt', 'a+', 'utf-8')
        for file in train_file:
            fp_file.write(file + '\n')
        fp_file.close()  
        fp_label = codecs.open(DATA_DIR+'train_label.txt', 'a+', 'utf-8')
        for t in train_label:
            fp_label.write(str(t) + '\n')
        fp_label.close()
        fp.close()
    #print(labels)
    #with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
    #fp = open(os.path.join(DATA_DIR, TEST_FILE), 'r')
    

    dev_file = []
    labels = {}
    count = 0
    dev_label = []
    dev_file = []
    with open(os.path.join(DATA_DIR, DEV_FILE), encoding='utf-8') as fp:
        for lines in fp:
            print(lines)
            label = lines.split()[0].strip()
            txt = lines.replace(label, '')
            if label not in labels:
                labels[label] = len(labels)
            #train_score.append(score)
            count += 1
            # writing '#count.txt' file
            filename = str(count)+'.txt'
            #print(os.path.join(DATA_DIR+TRAID_DIR, filename))
            fp_dev = codecs.open(os.path.join(DATA_DIR+DEV_DIR, filename), 'a+', 'utf-8')
            dev_file.append(filename)
            fp_dev.write(txt)
            fp_dev.close()
            dev_label.append(labels[label])
            # record #count label
        fp_file = codecs.open(DATA_DIR+'dev_txt.txt', 'a+', 'utf-8')
        for file in dev_file:
            fp_file.write(file + '\n')
        fp_file.close()  
        fp_label = codecs.open(DATA_DIR+'dev_label.txt', 'a+', 'utf-8')
        for t in dev_label:
            fp_label.write(str(t) + '\n')
        fp_label.close()
        fp.close()



    test_file = []
    labels = {}
    count = 0
    test_label = []
    test_file = []
    with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
        for lines in fp:
            print(lines)
            label = lines.split()[0].strip()
            txt = lines.replace(label, '')
            if label not in labels:
                labels[label] = len(labels)
            #train_score.append(score)
            count += 1
            # writing '#count.txt' file
            filename = str(count)+'.txt'
            #print(os.path.join(DATA_DIR+TRAID_DIR, filename))
            fp_test = codecs.open(os.path.join(DATA_DIR+TEST_DIR, filename), 'a+', 'utf-8')
            test_file.append(filename)
            fp_test.write(txt)
            fp_test.close()
            test_label.append(labels[label])
            # record #count label
        fp_file = codecs.open(DATA_DIR+'test_txt.txt', 'a+', 'utf-8')
        for file in test_file:
            fp_file.write(file + '\n')
        fp_file.close()  
        fp_label = codecs.open(DATA_DIR+'test_label.txt', 'a+', 'utf-8')
        for t in test_label:
            fp_label.write(str(t) + '\n')
        fp_label.close()
        fp.close()


        
def semeval_data(srcFile, tarFile):
    #with open(tarFile, encoding='utf-8') as wf:
    wrtFile = codecs.open(tarFile, 'a+', 'utf-8') 
    tweet_length = 0
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            if "ID\tTweet\tAffect Dimension" not in line:
                print(line)
                sents = line.split('\t')
                #print(sents[1] + "\t" + sents[3])
                print(sents[3])
                tokens = word_tokenize(sents[1])
                strline = ""
                for i in range(len(tokens)):
                    if len(strline) == 0:
                        strline = tokens[i]
                    else:
                        strline = strline + " " + tokens[i]
                print(sents[3] + "\t" + strline )
                #strline = strline.replace("\\n", "")
                wrtFile.write(sents[3].strip() + "\t" + strline + "\n")
                if len(tokens) > tweet_length:
                    tweet_length = len(tokens)
                print(word_tokenize(sents[1]))
    print(tweet_length)
    
def semeval_test(srcFile, tarFile):
    #with open(tarFile, encoding='utf-8') as wf:
    wrtFile = codecs.open(tarFile, 'a+', 'utf-8') 
    tweet_length = 0
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            if "ID\tTweet\tAffect Dimension" not in line:
                print(line)
                sents = line.split('\t')
                print(sents[1] + "\t" + sents[3])
                print(sents[3])
                tokens = word_tokenize(sents[1])
                strline = ""
                for i in range(len(tokens)):
                    if len(strline) == 0:
                        strline = tokens[i]
                    else:
                        strline = strline + " " + tokens[i]
                print("0\t" + strline )
                #strline = strline.replace("\\n", "")
                wrtFile.write("0\t" + strline + "\n")
                if len(tokens) > tweet_length:
                    tweet_length = len(tokens)
                print(word_tokenize(sents[1]))
    print(tweet_length)
    
    
def semeval_pred(srcFile, preFile, subFile):
    #with open(tarFile, encoding='utf-8') as wf:
    wrtFile = codecs.open(subFile, 'a+', 'utf-8') 
    score = []
    with open(preFile, encoding='utf-8') as f:
        for line in f:            
            score.append(line.strip())
            
    #tweet_length = 0
    index = 0
    with open(srcFile, encoding='utf-8') as f:
        for line in f:
            if "ID\tTweet\tAffect Dimension" in line:
                wrtFile.write(line)
            else:
                if score[index] == '0':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t-3: very negative emotional state can be inferred\n')
                elif score[index] == '1':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t-2: moderately negative emotional state can be inferred\n')        
                elif score[index] == '2':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t-1: slightly negative emotional state can be inferred\n')
                elif score[index] == '3':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t0: neutral or mixed emotional state can be inferred\n')
                elif score[index] == '4':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t1: slightly positive emotional state can be inferred\n')
                elif score[index] == '5':
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t2: moderately positive emotional state can be inferred\n')
                else:
                    sents = line.split('\t')
                    wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t3: very positive emotional state can be inferred\n')
                #sents = line.split('\t')
                #wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t'+ str(float('%.3f' % float(score[index])))+'\n')
#                 if score[index] == '0':
#                     sents = line.split('\t')
#                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t0: no Ar can be inferred\n')
#                 elif score[index] == '1':
#                     sents = line.split('\t')
#                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t1: low amount of Ar can be inferred\n')
#                 elif score[index] == '2':
#                     sents = line.split('\t')
#                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t2: moderate amount of Ar can be inferred\n')
#                 else:
#                     sents = line.split('\t')
#                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t3: high amount of Ar can be inferred\n')
                index += 1


def data_zip(txtFile, outFile):
    
    
    wrtFile = codecs.open(outFile, 'a+', 'utf-8') 
    #tweet_length = 0
    #labels = []
    #index = 0
#     with open(labFile, encoding='utf-8') as f:
#         for line in f:
#             labels.append(str(line))
    with open(txtFile, encoding='utf-8') as f:
        for line in f:
            print(line)
            wrtFile.write("0\t"+line.strip()+"\n")

            
#     wrtFile = codecs.open(outFile, 'a+', 'utf-8') 
#     tweet_length = 0
#     labels = []
#     index = 0
#     with open(labFile, encoding='utf-8') as f:
#         for line in f:
#             labels.append(str(line))
#     with open(txtFile, encoding='utf-8') as f:
#         for line in f:
#             print(line)
#             wrtFile.write(labels[index].strip()+"\t"+line.strip()+"\n")
#             index+=1
    
import os
outFile = "/home/hjp/Downloads/train.txt"
wrtFile = codecs.open(outFile, 'a+', 'utf-8') 
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        print(child)
        readFile(child)
        #print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题

# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r') # r 代表read
    for eachLine in fopen:
        #print(eachLine)
        tokens = eachLine.strip().split(" ")
        if len(tokens) == 2 or len(eachLine.strip()) == 0:
            wrtFile.write(eachLine.strip()+'\n')
        else:
            print(eachLine)
    fopen.close()        
        
def main():
    fDir = "/home/hjp/Downloads/task8/train/data/tokenized/"
    eachFile(fDir)
    
#     
#     txtFile = "/home/hjp/Downloads/semeval/task2/data/txt.txt"
#     #labFile = "/home/hjp/Downloads/semeval/task2/data/lab.txt"
#     outFile = "/home/hjp/Downloads/semeval/task2/data/out.txt"
#     data_zip(txtFile, outFile)
#     
    
    
#     train_srcFile = "/home/hjp/Downloads/semeval/task1d/data/Ar-train.txt"
#     train_tarFile = "/home/hjp/Downloads/semeval/task1d/data/Ar_train.txt"
#     dev_srcFile = "/home/hjp/Downloads/semeval/task1d/data/Ar-dev.txt"
#     dev_tarFile = "/home/hjp/Downloads/semeval/task1d/data/Ar_dev.txt"
#     test_srcFile = "/home/hjp/Downloads/semeval/task1d/data/Ar-test.txt"
#     test_tarFile = "/home/hjp/Downloads/semeval/task1d/data/Ar_test.txt"
#     test_preFile = "/home/hjp/Downloads/semeval/task1d/data/31.txt"
#     test_subFile = "/home/hjp/Downloads/semeval/task1d/data/V-oc_ar_pred.txt"
#     
#     flag = True
#      
#     if flag:
#         #semeval_data(train_srcFile, train_tarFile)
#         #semeval_data(dev_srcFile, dev_tarFile)
#         #semeval_test(test_srcFile, test_tarFile)
#         os.makedirs("/home/hjp/Downloads/semeval/task2/data_es/train_txt") 
#         os.makedirs("/home/hjp/Downloads/semeval/task2/data_es/dev_txt")
#         os.makedirs("/home/hjp/Downloads/semeval/task2/data_es/test_txt")
#         data_split()
#     else:    
#         semeval_pred(test_srcFile, test_preFile, test_subFile)


if __name__ == "__main__":
    main()










# import os
# import codecs
# from decimal import Decimal
# from nltk.tokenize import word_tokenize
# 
# DATA_DIR = '/home/hjp/Downloads/semeval/task1d/data/'
# TRAIN_FILE = 'Ar_train.txt'
# DEV_FILE = 'Ar_dev.txt'
# TEST_FILE = 'Ar_test.txt'
# TRAID_DIR = 'train_txt'
# DEV_DIR = 'dev_txt'
# TEST_DIR = 'test_txt'
# 
# 
# 
# def data_split():
#     train_file = []
#     #labels = {}
#     count = 0
#     train_file = []
#     with open(os.path.join(DATA_DIR, TRAIN_FILE), encoding='utf-8') as fp:
#         for lines in fp:
#             print(lines)
#             score = lines.split()[0].strip()
#             txt = lines.replace(score, '')
#             #train_score.append(score)
#             count += 1
#             # writing '#count.txt' file
#             filename = str(count)+'.txt'
#             #print(os.path.join(DATA_DIR+TRAID_DIR, filename))
#             fp_train = codecs.open(os.path.join(DATA_DIR+TRAID_DIR, filename), 'a+', 'utf-8')
#             train_file.append(filename)
#             fp_train.write(txt)
#             fp_train.close()
#             # record #count label
#             fp_score = codecs.open(DATA_DIR+'train_label.txt', 'a+', 'utf-8')
#             fp_score.write(str(score.strip()) + '\n')
#             fp_score.close()
#     fp_file = codecs.open(DATA_DIR+'train_txt.txt', 'a+', 'utf-8')
#     for file in train_file:
#         fp_file.write(file + '\n')
#     fp_file.close()
#     
# 
#     fp.close()
#     #print(labels)
#     #with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
#     #fp = open(os.path.join(DATA_DIR, TEST_FILE), 'r')
#     
#     
#     
#     count = 0
#     dev_file = []
#     with open(os.path.join(DATA_DIR, DEV_FILE), encoding='utf-8') as fp:
#         for lines in fp:
#             score = lines.split()[0].strip()
#             txt = lines.replace(score, '')
#             count += 1
#             # writing '#count.txt' file
#             filename = str(count)+'.txt'
#             fp_dev = codecs.open(os.path.join(DATA_DIR+DEV_DIR, filename), 'a+', 'utf-8')
#             #fp_test = open(os.path.join(TEST_DIR, filename), 'wb')
#             dev_file.append(filename)
#             fp_dev.write(txt)
#             fp_dev.close()
#             # record #count label
#             fp_score = codecs.open(DATA_DIR+'dev_label.txt', 'a+', 'utf-8')
#             fp_score.write(str(score) + '\n')
#             fp_score.close() 
#         fp_file = codecs.open(DATA_DIR+'dev_txt.txt', 'a+', 'utf-8')
#         for file in dev_file:
#             fp_file.write(file + '\n')
#         fp_file.close()
#    
#         fp.close()
#     
#     
#     
#     
#     count = 0
#     test_file = []
#     with open(os.path.join(DATA_DIR, TEST_FILE), encoding='utf-8') as fp:
#         for lines in fp:
#             print(lines)
#             score = lines.split()[0].strip()
#             #print(label)
#             txt = lines.replace(score, '')
#             count += 1
#             # writing '#count.txt' file
#             filename = str(count)+'.txt'
#             fp_test = codecs.open(os.path.join(DATA_DIR+TEST_DIR, filename), 'a+', 'utf-8')
#             #fp_test = open(os.path.join(TEST_DIR, filename), 'wb')
#             test_file.append(filename)
#             fp_test.write(txt)
#             fp_test.close()
#             # record #count label
#             fp_score = codecs.open(DATA_DIR+'test_label.txt', 'a+', 'utf-8')
#             fp_score.write(str(score) + '\n')
#             fp_score.close()  
#         fp_file = codecs.open(DATA_DIR+'test_txt.txt', 'a+', 'utf-8')
#         for file in test_file:
#             fp_file.write(file + '\n')
#         fp_file.close()  
#         fp.close()
#         
# def semeval_data(srcFile, tarFile):
#     #with open(tarFile, encoding='utf-8') as wf:
#     wrtFile = codecs.open(tarFile, 'a+', 'utf-8') 
#     tweet_length = 0
#     with open(srcFile, encoding='utf-8') as f:
#         for line in f:
#             if "ID\tTweet\tAffect Dimension" not in line:
#                 print(line)
#                 sents = line.split('\t')
#                 #print(sents[1] + "\t" + sents[3])
#                 print(sents[3])
#                 tokens = word_tokenize(sents[1])
#                 strline = ""
#                 for i in range(len(tokens)):
#                     if len(strline) == 0:
#                         strline = tokens[i]
#                     else:
#                         strline = strline + " " + tokens[i]
#                 print(sents[3] + "\t" + strline )
#                 #strline = strline.replace("\\n", "")
#                 wrtFile.write(sents[3].strip() + "\t" + strline + "\n")
#                 if len(tokens) > tweet_length:
#                     tweet_length = len(tokens)
#                 print(word_tokenize(sents[1]))
#     print(tweet_length)
#     
# def semeval_test(srcFile, tarFile):
#     #with open(tarFile, encoding='utf-8') as wf:
#     wrtFile = codecs.open(tarFile, 'a+', 'utf-8') 
#     tweet_length = 0
#     with open(srcFile, encoding='utf-8') as f:
#         for line in f:
#             if "ID\tTweet\tAffect Dimension" not in line:
#                 print(line)
#                 sents = line.split('\t')
#                 print(sents[1] + "\t" + sents[3])
#                 print(sents[3])
#                 tokens = word_tokenize(sents[1])
#                 strline = ""
#                 for i in range(len(tokens)):
#                     if len(strline) == 0:
#                         strline = tokens[i]
#                     else:
#                         strline = strline + " " + tokens[i]
#                 print("0\t" + strline )
#                 #strline = strline.replace("\\n", "")
#                 wrtFile.write("0\t" + strline + "\n")
#                 if len(tokens) > tweet_length:
#                     tweet_length = len(tokens)
#                 print(word_tokenize(sents[1]))
#     print(tweet_length)
#     
#     
# def semeval_pred(srcFile, preFile, subFile):
#     #with open(tarFile, encoding='utf-8') as wf:
#     wrtFile = codecs.open(subFile, 'a+', 'utf-8') 
#     score = []
#     with open(preFile, encoding='utf-8') as f:
#         for line in f:
#             
#             score.append(line.strip())
#             
#     #tweet_length = 0
#     index = 0
#     with open(srcFile, encoding='utf-8') as f:
#         for line in f:
#             if "ID\tTweet\tAffect Dimension" in line:
#                 wrtFile.write(line)
#             else:
#                 sents = line.split('\t')
#                 wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t'+ str(float('%.3f' % float(score[index])))+'\n')
# #                 if score[index] == '0':
# #                     sents = line.split('\t')
# #                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t0: no Ar can be inferred\n')
# #                 elif score[index] == '1':
# #                     sents = line.split('\t')
# #                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t1: low amount of Ar can be inferred\n')
# #                 elif score[index] == '2':
# #                     sents = line.split('\t')
# #                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t2: moderate amount of Ar can be inferred\n')
# #                 else:
# #                     sents = line.split('\t')
# #                     wrtFile.write(sents[0] + '\t' + sents[1] + '\t' + sents[2] + '\t3: high amount of Ar can be inferred\n')
#                 index += 1
#         
#         
# def main():
#     train_srcFile = "/home/hjp/Downloads/semeval/task1d/data/Ar-train.txt"
#     train_tarFile = "/home/hjp/Downloads/semeval/task1d/data/Ar_train.txt"
#     dev_srcFile = "/home/hjp/Downloads/semeval/task1d/data/Ar-dev.txt"
#     dev_tarFile = "/home/hjp/Downloads/semeval/task1d/data/Ar_dev.txt"
#     test_srcFile = "/home/hjp/Downloads/semeval/task1d/data/Ar-test.txt"
#     test_tarFile = "/home/hjp/Downloads/semeval/task1d/data/Ar_test.txt"
#     test_preFile = "/home/hjp/Downloads/semeval/task1d/data/31.txt"
#     test_subFile = "/home/hjp/Downloads/semeval/task1d/data/V-oc_ar_pred.txt"
#     
#     flag = False
#     
#     if flag:
#         semeval_data(train_srcFile, train_tarFile)
#         semeval_data(dev_srcFile, dev_tarFile)
#         semeval_test(test_srcFile, test_tarFile)
#         os.makedirs("/home/hjp/Downloads/semeval/task1d/data/train_txt") 
#         os.makedirs("/home/hjp/Downloads/semeval/task1d/data/dev_txt")
#         os.makedirs("/home/hjp/Downloads/semeval/task1d/data/test_txt")
#         data_split()
#     else:    
#         semeval_pred(test_srcFile, test_preFile, test_subFile)
# 
# 
# if __name__ == "__main__":
#     main()
