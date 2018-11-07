from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

s1 = "Wake her up slip fingers in pants play with pussy through undies then go in with fingers while playin with clit once she's wet enough get her on top and play with her clit with ur fingers while you slowly go in and out or she goes up n down Made my gf shriek was so fuckin hot"
s2 = "You know, this place sucks. Anyway don't pretend to know what you're doing, if she/he is a newbie like you cheer up. If not, simple follow his/her lead."
s3 = "follow up... the best ones were when i'd wake up at 3am middle of the night type time range, and be rock hard as fuck and just start railing her while we were both semi conscious. and i'd just blow as hard as humanly possible and she'd absolutely shatter windows with the screaming orgasms. neighbors had to have heard it all. "


def tfidf():
    tf = TfidfVectorizer()
    data = tf.fit_transform([s1, s2, s3])

    # print(tf.get_feature_names())

    # print(data.toarray())

    a = pd.DataFrame(data.toarray(),columns=tf.get_feature_names())
    a.to_excel('ifidf.xlsx')


if __name__ == '__main__':
    tfidf()
