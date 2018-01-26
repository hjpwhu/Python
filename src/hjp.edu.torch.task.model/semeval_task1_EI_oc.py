import codecs
from nltk.tokenize import word_tokenize

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
                print(sents[3][0:1])
                tokens = word_tokenize(sents[1])
                strline = ""
                for i in range(len(tokens)):
                    if len(strline) == 0:
                        strline = tokens[i]
                    else:
                        strline = strline + " " + tokens[i]
                print(sents[3][0:1] + "\t" + strline )
                #strline = strline.replace("\\n", "")
                wrtFile.write(sents[3][0:1] + "\t" + strline + "\n")
                if len(tokens) > tweet_length:
                    tweet_length = len(tokens)
                print(word_tokenize(sents[1]))
    print(tweet_length)




def main():
    print("hello!")
    srcFile = "/Users/hjp/Downloads/task1_EI_oc/anger-train.txt"
    tarFile = "/Users/hjp/Downloads/task1_EI_oc/anger_train1.txt"
    semeval_data(srcFile, tarFile)


if __name__=='__main__':
    main()