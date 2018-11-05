import os
from win32com import client as wc


def make_html(input_path, output_path=None):
    if not output_path:
        output_path = input_path + "\\html"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    word = wc.Dispatch('KWPS.Application')
    path = os.listdir(input_path)
    for name in path:
        if os.path.splitext(name)[1] in ['.doc', '.docx']:
            print("正在转换：" + name)
            new_name = name.replace('docx', 'html').replace('doc', 'html')
            doc = word.Documents.Open(os.path.join(input_path, name))
            doc.SaveAs(os.path.join(output_path, new_name), 8)
            doc.Close()
            print("转换文档完成：" + name)
    print('文档全部转换完成')


if __name__ == '__main__':
    make_html('E:\\自媒体\\百家\\1转化\\4', 'E:\\PythonProject\\baijia\\html\\红楼')
    exit()
    # for path in os.listdir('E:\\自媒体\\百家\\2018-10-29'):
    #     make_html('E:\\自媒体\\百家\\2018-10-29\\' + path)
    # make_html('E:\\自媒体\\百家\\2018-10-29\\六六 三国 2')
    for path in ['E:\\自媒体\\百家\\' + str(i) for i in range(1, 10)]:
        make_html(path)
# from win32com import client as wc
# import os
# word = wc.Dispatch('Word.Application')
#
# def wordsToHtml(dir):
#
#     for path, subdirs, files in os.walk(dir):
#         for wordFile in files:
#             wordFullName = os.path.join(path, wordFile)
#             #print "word:" + wordFullName
#             doc = word.Documents.Open(wordFullName)
#             if(fileSuffix == "doc" or fileSuffix == "docx"):
#                 fileName = wordFile2[ : dotIndex]
#                 htmlName = fileName + ".html"
#                 htmlFullName = os.path.join(unicode(path, "gbk"), htmlName)
#                 #htmlFullName = unicode(path, "gbk") + "\\" + htmlName
#                 print "generate html:" + htmlFullName
#                 doc.SaveAs(htmlFullName, 10)
#                 doc.Close()
#
#     word.Quit()
#     print("")
#     print("Finished!")
#
# if __name__ == '__main__':
#     import sys
#     if len(sys.argv) != 2:
#         print("Usage: python funcName.py rootdir")
#         sys.exit(100)
#     wordsToHtml(sys.argv[1])
