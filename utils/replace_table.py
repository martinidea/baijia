def replace(path):
    with open(path, 'r', encoding='utf-8') as f:
        x = [t.replace('<tbody>', '').replace('</tbody>', '').replace('<td>', '').replace('</td>', '').replace('<tr>',
                                                                                                               '').replace(
            '<tr>', '').replace('</tr>', '') for t in
             f.readlines()]
        print(x)
        with open('../html/三国/《三国演义》中的诸葛亮，曾多次用火攻，为何只在火烧藤甲兵时感叹会折寿？2.html', 'w') as ff:
            ff.writelines(x)
            ff.close()
        f.close()
        # with open(path,'w')


if __name__ == '__main__':
    replace('../html/三国/《三国演义》中的诸葛亮，曾多次用火攻，为何只在火烧藤甲兵时感叹会折寿？.html')
