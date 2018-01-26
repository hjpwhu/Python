
def wnut(srcPath, tarPath):
    wf = open(tarPath, 'w')
    
    with open(srcPath, 'r') as file:
        strline = ""
        tagline = ""
        for line in file:
            line = line.strip()            
            print(line)
            if len(line) > 0:
                tokens = line.split('\t')
                print(tokens)
                if len(strline) == 0:
                    strline = tokens[0]
                    tagline = tokens[1]
                else:
                    strline = strline + " " + tokens[0]
                    tagline = tagline + " " + tokens[1]
            else:
                wf.write(strline + '\t' + tagline + '\n')  
                strline = ""  
                tagline = ""
    


if __name__ == '__main__':
    srcPath = "/home/hjp/Downloads/wner/train.txt"
    tarPath = "/home/hjp/Downloads/wner/train.dat"
    wnut(srcPath, tarPath)