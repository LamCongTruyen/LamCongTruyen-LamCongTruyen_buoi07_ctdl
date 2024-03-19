class node:#định nghĩa một thư viện mối nút trong ds liên kết
    def __init__(self, value = None):
        self.value = value
        self.next = next

class linked_list:#định nghĩa một thư viện ds liên kết
    def __init__(self):
        self.head = None
    
class stack:#định nghĩa một lớp thư viện ngăn xếp
    def __init__(self):
        self.linked_list = linked_list()
    def is_empty(self):#ktra em ngăn xếp trống hay không
        if self.linked_list.head == None:
            return True
        else:
            return False
    
custom_stack = stack()
print(custom_stack.is_empty()) #TRUE
