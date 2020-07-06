class InputOutput:
    def __init__(self):
        self.mystr = ""

    def get_input(self):
        self.mystr = input()

    def print_output(self):
        print(self.mystr.upper())


io = InputOutput()
io.get_input()
io.print_output()
