class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.fullness = 100
        self.maried = None
        self.House = None

    def set_maried(self, maried):
        self.maried = maried
        print('Я {} за {}'.format(self.name, self.maried))

    def __str__(self):
        return self.name


t1 = Human('Саша', 'муж')
t2 = Human('Лана', 'жен')
t1.set_maried(t2)
t2.set_maried(t1)
