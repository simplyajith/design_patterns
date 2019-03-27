class Dictattr:

    dicto = {}

    def __getattr__(self, item):
        try:
            return self.dicto[item]
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, key, value):

        self.dicto[key]=value
        return self.dicto

if __name__ == '__main__':
    d1 = Dictattr()
    print d1
    print d1.__setattr__('name','ajith')
    print d1.__getattr__('name')
    print d1.__setattr__('name1', 'ajith')
    print d1.__setattr__('dicto', 'ajith')






