from PIL import Image
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed


class Pic_Dumplicator():
    def __init__(self, dirname, ans_rate):
        self.width = 128
        self.high = 128
        self.dirName = dirname
        self.allDiff = []
        self.dumplicate_pic_name_set = set()
        self.dirList = os.listdir(self.dirName)
        self.dirList.sort(key=lambda x: str(x.split('.')[0]).zfill(8))
        self.cnt = 0
        self.ans_rate = ans_rate

    def getDiff(self, width, high, image):  # 将要裁剪成w*h的image照片
        diff = []
        im = image.resize((width, high))
        imgray = im.convert('L')  # 转换为灰度图片 便于处理
        pixels = list(imgray.getdata())  # 得到像素数据 灰度0-255

        for row in range(high):  # 逐一与它左边的像素点进行比较
            rowStart = row * width  # 起始位置行号
            for index in range(width - 1):
                leftIndex = rowStart + index
                rightIndex = leftIndex + 1  # 左右位置号
                diff.append(pixels[leftIndex] > pixels[rightIndex])

        return diff  # *得到差异值序列 这里可以转换为hash码*

    def getHamming(self, diff=[], diff2=[]):  # 暴力计算两点间汉明距离
        hamming_distance = 0
        for i in range(len(diff)):
            if diff[i] != diff2[i]:
                hamming_distance += 1
        return hamming_distance

    def removePic(self, dirname, file_set):
        for i in file_set:
            os.remove(os.path.join(dirname, i))

    def process(self, i, j):
        if i != j:
            ans = self.getHamming(self.allDiff[i][1], self.allDiff[j][1])
            if ans <= self.ans_rate:
                self.dumplicate_pic_name_set.add(self.allDiff[j][0])
                # 以下为调试输出信息
                # print(ans, self.allDiff[i][0] + "-" + self.allDiff[j][0])
            print(ans, self.allDiff[i][0] + "-" + self.allDiff[j][0])
            # if self.allDiff[i][0] == '3206.jpg':
            #     print(ans, self.allDiff[i][0] + "-" + self.allDiff[j][0])

    def run(self):
        for i in self.dirList:
            self.cnt += 1
            im = Image.open(os.path.join(self.dirName, i))
            diff = self.getDiff(self.width, self.high, im)
            self.allDiff.append((str(i), diff))

        # with ThreadPoolExecutor(max_workers=4) as executor:
        #     for i in range(len(self.allDiff)):
        #         if self.allDiff[i][0] in self.dumplicate_pic_name_set:
        #             continue
        #         for j in range(i + 1, len(self.allDiff)):
        #             executor.submit(self.process, i, j)
        for i in range(len(self.allDiff)):
            if self.allDiff[i][0] in self.dumplicate_pic_name_set:
                continue
            for j in range(i + 1, min(i + 10, len(self.allDiff))):
                self.process(i, j)
            # print(self.dumplicate_pic_name_set,i)

        self.removePic(self.dirName, self.dumplicate_pic_name_set)


if __name__ == '__main__':
    base_dir = "./save_imgs"
    folder_list = os.listdir(base_dir)
    for i in folder_list:
        folder_path = os.path.join(base_dir,i)
        pder = Pic_Dumplicator(folder_path,ans_rate=2000)  # ans_rate：默认教学片2000，电影8000
        pder.run()
