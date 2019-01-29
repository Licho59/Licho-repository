"""Program that inputs a document and then outputs a barchart
plot of the frequencies of each alphabet character that appears in
that document."""

def alphabet_freq():
    freqDic = {}
    with open('words.txt') as f:
        #Read source file and calculate the frequences
        for line in f:
            for char in line:
                if char.isalpha():
                    freqDic[char] = freqDic.get(char, 0) + 1
    #plot the frequences
    for alpha in range(ord('a'), ord('z') + 1):
        alpha = chr(alpha)
        print("%s " % (alpha) + "-" * freqDic.get(alpha, 0))
    for alpha in range(ord('A'), ord('Z') + 1):
        alpha = chr(alpha)
        print("%s " % (alpha) + "-" * freqDic.get(alpha, 0))
        
if __name__ == '__main__':
    print(alphabet_freq())
