import os
import re
import fitz

check_XO = r'/Type(?= */XObject)'
check_IMG = r'/Subtype(?= */Image)'


def pdfGetImage(path, load_path):
    imgCount = 0
    doc = fitz.open(path)
    objCount = doc.xref_length()
    print('文件名:{}, 页数: {}, 对象: {}'.format(path, len(doc), objCount - 1))
    for i in range(1, objCount):
        text = doc.xref_object(i)
        isXObject = re.search(check_XO, text)
        isImage = re.search(check_IMG, text)
        if not isXObject or not isImage:
            continue
        imgCount += 1
        pix = fitz.Pixmap(doc, i)
        filename = path.replace('\\', '_') + "_image{}.png".format(imgCount)
        filename = filename.replace(':', '')
        if pix.n < 5:
            pix.save(os.path.join(load_path, filename))
        else:
            p = fitz.Pixmap(fitz.csRGB, pix)
            p.save(os.path.join(load_path, filename))
            p = None
        pix = None
        print("提取了{}张图片".format(imgCount))


if __name__ == '__main__':
    path = r'D:\test.pdf'
    load_path = r'D:\imageLoad'
    if os.path.exists(load_path):
        print("you already have this file")
        raise SystemExit
    else:
        os.mkdir(load_path)
    pdfGetImage(path, load_path)
