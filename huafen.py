import os, random, shutil
def moveFile(fileDir):
    pathDir = os.listdir(fileDir)    # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.2   # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber*rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    print(sample)
    for name in sample:
        shutil.move(fileDir+name, tarDir+name)
    return

def moveLabel(tarDir,labDir):
    filesname_list1 = []
    pathDir1 = os.listdir(tarDir)
    for i in range(len(pathDir1)):
        (filepath, tempfilename) = os.path.split(pathDir1[i])
        (filesname, extension) = os.path.splitext(tempfilename)
        filesname_list1.append(filesname)

    filesname_list2 = []
    pathDir1 = os.listdir(labDir)
    for i in range(len(pathDir1)):
        (filepath, tempfilename) = os.path.split(pathDir1[i])
        (filesname, extension) = os.path.splitext(tempfilename)
        filesname_list2.append(filesname)

    for name1 in filesname_list1:
        for name2 in filesname_list2:
            if name1 == name2:
                shutil.move(labDir+name2+'.txt', tarLabDir+name2+'.txt')
    return


if __name__ == '__main__':
    fileDir = "C:\\Users\\hp\\Desktop\\youcha\\train\\images\\"    # 源图片文件夹路径
    tarDir = "C:\\Users\\hp\\Desktop\\youcha\\valid\\images\\"    # 移动到新的文件夹路径
    moveFile(fileDir)
    labDir = 'C:\\Users\\hp\\Desktop\\youcha\\train\\labels\\'  # 源文件的标签
    tarLabDir = 'C:\\Users\\hp\\Desktop\\youcha\\valid\\labels\\'  # 新标签
    moveLabel(tarDir, labDir)
