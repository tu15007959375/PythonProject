import os

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt  # 绘制图像的模块
import imageio

tag = 0
if tag == 0:
    from .wordsegment import get_pkuseg
    from .wordsegment import get_snowlp
    from .wordsegment import get_jieba
    from .wordsegment import get_thulac
elif tag == 1:
    from wordsegment import get_pkuseg
    from wordsegment import get_snowlp
    from wordsegment import get_jieba
    from wordsegment import get_thulac


def get_wordcloud(cut_text, method, starttime, endtime):
    path = 'resources/cloud/' + method + 'cloud' + starttime + '_' + endtime + '.jpg'
    mk = imageio.imread('resources/cloud/background.jpeg')
    if not os.path.exists(path):
        print("生成词云中")
        wordcloud = WordCloud(
            # 设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
            font_path="resources/fonts/msyh.ttc",
            # 设置了背景，宽高
            background_color="white", mask=mk, width=1000, height=1000, scale=5).generate(cut_text)

        # 调用wordcloud库中的ImageColorGenerator()函数，提取模板图片各部分的颜色
        image_colors = ImageColorGenerator(mk)
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        wordcloud.to_file(path)


# 获取词频字典的键
def get_cut_text(countdict):
    namelist = []
    for key in countdict.keys():
        namelist.append(key)
    cut_text = ' '.join(namelist)
    return cut_text


def pku_seg_cloud(starttime, endtime):
    countdict = get_pkuseg(starttime, endtime)
    cut_text = get_cut_text(countdict)
    get_wordcloud(cut_text, 'pkuseg', starttime, endtime)


def jieba_seg_cloud(starttime, endtime):
    countdict = get_jieba(starttime, endtime)
    cut_text = get_cut_text(countdict)
    get_wordcloud(cut_text, 'jieba', starttime, endtime)


def thulac_seg_cloud(starttime, endtime):
    countdict = get_thulac(starttime, endtime)
    cut_text = get_cut_text(countdict)
    get_wordcloud(cut_text, 'thulac', starttime, endtime)


def snowlp_seg_cloud(starttime, endtime):
    countdict = get_snowlp(starttime, endtime)
    cut_text = get_cut_text(countdict)
    get_wordcloud(cut_text, 'snowlp', starttime, endtime)


if __name__ == '__main__':
    thulac_seg_cloud('2022-3-1', '2022-3-7')
