class Engine:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def start(self):
        print("Start the engine")
    def stop(self):
        print("Stop the engine")
class Car(Engine):
    def __init__(self, name,engine):
        self.name = name
        self.engine = engine
        self.engine = Engine(name)
    def getname(self):
        return self.name
    def getengine(self):
        return self.engine
e = Engine("abc")
# print(e.getname())
c = Car("xyz","abc")
print(c.getname())
print(c.getengine())
print(c.start())
print(c.stop())