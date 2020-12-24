class Human:
    def __init__(self):
        self.human = "human"
class Man(Human):
    def __init__(self):
        self.sex = "man"
class Woman(Human):
    def __init__(self):
        self.sex = "woman"
def God():
    man = Man()
    woman = Woman()
    return [man, woman]