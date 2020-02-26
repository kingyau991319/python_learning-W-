import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from langconv import *

class QQ_message_text:

    #punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~。，''' if need 

    def __init__(self,filename):
        self.filename = filename

    def process(self):

        # internal function for subtract text
        def subtract_text(f):
            line = f.readline()
            text = ""
            i = 0
            for line in iter(f):
                # subtract the head
                if i == 8:
                    date = line[:4]
                    pict = line[:4]
                    if (date != "2020") & (not line.isspace()) & (pict != "[图片]"):
                        text = text + line
                else:
                    i = i + 1
            text = Converter('zh-hans').convert(text) # i need to change 繁體簡體
            return text

        try:
            f = open(self.filename,"r")
            text = subtract_text(f)
            f.close()

        except IOError as e:
            print(e)
            exit()

        wordlist = jieba.cut(text,cut_all=True)
        wl = " ".join(wordlist)

        wc = WordCloud(background_color = "black",
            width= 2000,height=1000,
            #mask = "",
            max_words = 500, 
            stopwords = "",
            font_path = "華康娃娃體.TTF",
            max_font_size = 150,  
            random_state = 80, 
        )
        myword = wc.generate(wl)
        plt.imshow(myword)
        plt.axis("off")
        plt.show()

        # I need to subtract it first

if __name__ == "__main__":
    test = QQ_message_text("test_file.txt")
    test.process()
