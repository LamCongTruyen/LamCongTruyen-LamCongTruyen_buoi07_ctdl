class stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        values = self.list.reserve()
        values = [str(x) for x in self.list]
        return '\n' .join(values)
    
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
custom_stack = stack()
print(custom_stack.is_empty())