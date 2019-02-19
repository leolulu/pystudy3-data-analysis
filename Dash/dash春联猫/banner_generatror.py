def generator(words):
    template = '''┌○┐
｜A1｜
｜B1｜ﾊ,,ﾊ
｜B2｜ﾟωﾟ )
｜B3｜ ／/
└○┘ (⌒)
　　 し⌒“'''

    if len(words) < 4:
        words = '字数需要大于四个'

    result = template.replace('｜A1｜\n',''.join(['｜{}｜\n'.format(i) for i in words[:-3]])) \
            .replace('B1',words[-3]) \
            .replace('B2',words[-2]) \
            .replace('B3',words[-1])
        
    return result


if __name__ == '__main__':
    print(
        generator('风评被害')
    )