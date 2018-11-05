import os


def get_html_in_page(page):
    return [path for path in os.listdir(page) if path.endswith(".html") and not path == 'index.html']


def make_index(page):
    with open(page + "\\index.html", "w", encoding="utf-8") as index_html:
        index_html.writelines(
            """<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>{0}</title></head>\n<body>\n""".format(
                os.path.split(page)[-1]))
        content = ['<a href=\"' + a + '\"  target=\"_blank\">' + a + '</a></br>\n' for a in get_html_in_page(page)]
        index_html.writelines(content)
        index_html.writelines("</body></html>")
        index_html.close()


def get_pages():
    return [path for path in os.listdir('../html') if os.path.isdir('../html/' + path)]


def make_all():
    for page in get_pages():
        make_index('../html/' + page)


def make_page_html():
    with open('../index.html', 'w', encoding="utf-8") as page_html:
        page_html.writelines(
            '<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>百家号文章</title></head><body><h1>百家号</h1>')
        content = ['<a href=\"html/' + a + '/index.html\"  target=\"_blank\">' + a + '</a></br>\n' for a in get_pages()]
        page_html.writelines(content)
        get_pages()


if __name__ == '__main__':
    make_page_html()
    make_all()
    exit()
    # print(get_html_in_page('../html/李华华说花草/html'))
