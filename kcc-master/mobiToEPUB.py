import os
import shutil

from kindlecomicconverter.comic2ebook import main

basePATH = 'E:\\Download\\mobiToEPUB\\'

if __name__ == '__main__':
    # 初始化项目目录
    mobiPATH = basePATH + 'mobi\\'
    tmpPATH = basePATH + 'tmp\\'
    epubPATH = basePATH + 'epub\\'
    mobiFolder = os.path.exists(mobiPATH)
    tmpFolder = os.path.exists(tmpPATH)
    epubFolder = os.path.exists(epubPATH)
    if not tmpFolder:
        os.mkdir(tmpPATH)
    if not epubFolder:
        os.mkdir(epubPATH)
    if not mobiFolder:
        os.mkdir(mobiPATH)
        print('--初始化完毕，将mobi文件放入文件夹下，然后再次运行--')
        exit(0)

    # 获取mobi文件夹下的文件目录
    mobiFiles = os.listdir(mobiPATH)
    for mobiFile in mobiFiles:
        # 获取文件名
        pureName = mobiFile[0:mobiFile.rfind(".")]
        print('--当前正在处理' + pureName + '--')

        # 在tmp文件夹下新建一个文件夹用于保存临时文件
        myTmpPATH = tmpPATH + pureName
        folder = os.path.exists(myTmpPATH)
        if not folder:
            os.mkdir(myTmpPATH)
            os.system('python2 ' + basePATH + 'mobiunpack.py ' + mobiPATH + mobiFile + ' ' + myTmpPATH)
            print('--解包完毕--')
            src = os.path.join(tmpPATH, pureName, 'images\\')
            args = ['-p', 'KoAO', '-f', 'EPUB', '--forcecolor', '-o', epubPATH, '-t', pureName, src]
            main(args)
            os.rename(os.path.join(epubPATH, 'images.kepub.epub'), os.path.join(epubPATH, pureName + '.epub'))
            # 清理tmp文件夹
            trashes = os.listdir(tmpPATH)
            for trash in trashes:
                print('--正在清理' + trash + '--')
                shutil.rmtree(os.path.join(tmpPATH, trash))
