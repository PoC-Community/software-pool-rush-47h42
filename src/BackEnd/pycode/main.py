def check_line():
    file = open('.line', 'r').read()
    line = int(file.read())
    print(line)


class TestLog():
    __init__(self):
        self.file = open('.line', 'rw')
        self.value = int(self.file.read())
    
    
        