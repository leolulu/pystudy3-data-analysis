from sklearn.feature_extraction.text import CountVectorizer
import jieba
import pandas as pd
import re

with open(r'E:\Python\PycharmProjects\pystudy3-data-analysis\机器学习\public\resource.txt', 'r', encoding='utf-8') as f:
    str1 = f.read()

# str_list = ['本人的硕士论文对算法鲁棒性有所涉及', '并偏向聚类算法的鲁棒性', '但也只是学到了一点皮毛', '我考虑到网上的相关博文极少']
str_list = re.split(r'[，。]', str1)
str_list = [' '.join(list(jieba.cut(i))) for i in str_list]


def textV():
    cv = CountVectorizer()
    data = cv.fit_transform(str_list)

    # print(cv.get_feature_names())
    # print(data)

    d1 = pd.DataFrame(data.toarray(), columns=cv.get_feature_names())
    # print(d1)
    print(d1.sum(axis=0).sort_values(ascending=True))


if __name__ == '__main__':
    textV()
