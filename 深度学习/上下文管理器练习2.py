class ContextManager:
    def __enter__(self):
        print('进入上下文管理器')
        return self

    def __exit__(self, type1, val1, tb1):
        print(type1, val1, tb1, sep='+++++++++++++')
        print('退出上下文管理器')
        return True

    def __init__(self):
        self.mark = 'this is base instance!'

    def bark(self):
        print(
            'my mark is :',
            self.mark
        )

    def err_func(self):
        1/0


with ContextManager() as f:
    f.err_func()
