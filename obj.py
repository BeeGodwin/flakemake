class Tester:
    '''Testing my understanding of classes'''

    def __init__(self, attr1, attr2, gens):
        self.attr1 = attr1
        self.attr2 = attr2
        self.gens = gens
        self.ch = None
        if self.gens > 0: # trying out recursive object creation
            self.ch = Tester(self.add_them(), self.add_them(), self.gens - 1)
        print('My add_them returns {}'.format(self.add_them()))

    def __str__(self):
        return 'I am a test object.'

    def add_them(self):
        return self.attr1 + self.attr2

def main():
    print('Creating an object')
    test = Tester(2, 2, 2)
    print(test.ch)

if __name__ == '__main__':
    main()
