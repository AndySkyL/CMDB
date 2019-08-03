
class Person():
    def talk(self):
        raise NotImplementedError('talk() must be implemented')

class Chinese(Person):
    pass
Chinese().talk()