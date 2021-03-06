import os
import cv2


def cutFrame(file_path, fps_rate=1):
    file_name_list = filter(lambda x: x[-3:] in ['mkv', 'mp4'], os.listdir(file_path))

    for media_file_path in [{'file_name': file_name, 'path': os.path.join(file_path, file_name)} for file_name in file_name_list]:
        dir_name = './save_imgs/{}'.format(media_file_path['file_name'].split('.')[0])
        print(dir_name)
        try:
            os.makedirs(dir_name)
        except Exception as e:
            print(e)

        cap = cv2.VideoCapture(media_file_path['path'])
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        print(cap.isOpened(), fps)
        frame_count = 1
        success = True
        while success:
            if frame_count % 5000 == 0:
                print(frame_count)
            success, frame = cap.read()
            if frame_count % (fps * fps_rate) == 0:
                cv2.imencode(".jpg", frame)[1].tofile(dir_name+'/{}.jpg'.format(frame_count))
            frame_count += 1
        cap.release()


if __name__ == '__main__':
    cutFrame(r'F:\迅雷下载\bilibili_download\OneDrive\量化交易实战项目班-10课(6.7G,Python3,2017年更新)', 5)
