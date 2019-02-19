def timeprint(*args):
    import datetime
    print('['+datetime.datetime.now().strftime('%F %X')+']', end=' ')
    for i in args[:-1]:
        print(i, end=' ')
    print(args[-1])