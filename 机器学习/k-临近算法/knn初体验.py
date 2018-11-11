import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def knncls():
    status = pd.read_csv(r'E:\python\pystudy3-data-analysis\机器学习\k-临近算法\status_predict.csv', engine='python')
    status.columns = ["PRICE", "CUSTOMBANLANCE", "CUSTOMERBANLANCE", "STATUS"]
    status.drop_duplicates(inplace=True)

    y = status['STATUS']
    x = status.loc[:, 'PRICE': 'CUSTOMERBANLANCE']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    std = StandardScaler()
    std.fit_transform(x_train)
    std.transform(x_test)

    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(x_train, y_train)

    y_predict = knn.predict(x_test)
    score = knn.score(x_test, y_test)

    print(score)


if __name__ == '__main__':
    knncls()
