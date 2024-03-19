class stack: #tạo một thư viện có tên là ngăn xếp
    def __init__(self): #phương thức khởi tạo của lớp stack
        self.list = [1,2,3] #khởi tạo một hàm list rỗng
    def __str__(self):
        values = self.list.reverse() #đảo ngược danh sách và gán vào biến values
        values = [str(x) for x in self.list] #biến từng phần tử thành chuỗi(str) trong hàm list sau đó lưu vào biến value
        return '\n' .join(values) #trả về chuỗi đc tạo từ việc nói từng phần tử lại với nhau,xuống dòng sau mỗi lần trả về
    
    def is_empty(self): #tạo hàm kiểm tra ngăn xếp
        if self.list == []: #nếu rỗng. trả về true, ngược lại trả về false
            return True
        else:
            return False
    

    def push(self, value): #TẠO HÀM PUSH CHO THƯ VIỆN STACK
        self.list.append(value) #thêm gtri vào cuối danh sách. tương đương với vị trí đỉnh ngăn xếp
        return "DA CHEN THEM MOT PHAN TU THANH CONG"
    
    def pop(self): #TẠO HÀM POP CHO THƯ VIỆN STACK
        if self.is_empty(): #kiểm tra xem ngăn xếp có rỗng không,nếu có thì trả về ko có ptu nào
            return "khong co ptu nao trong ngan xep"
        else: 
            return self.list.pop() #loại bỏ và chỉ trả về ptu ở đỉnh ngăn xếp

    def peek(self): #hàm trả về phần tử ở đỉnh của ngăn xếp
        if self.is_empty():
            return "khongco phan tu nao trong nganxep"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None #xóa toàn bộ ngăn xếp
    
    def is_empty(self): #kiểm tra xem ngăn xếp có rỗng không, nếu có trả về true ngược lại false
        if self.list == []:
            return True 
        else:
            return False
        
    def is_full(self):#ktra xem ngăn xếp đầy chưa, dựa trên kích thước ngắn xếp đã khai báo trc đó
        if len(self.list) == self.max_size:
            return True
        else:
            return False
        
    
custom_stack = stack() 
print(custom_stack.is_empty()) #False   
                                #in ra cái kết quả kiểm tra ngăn xếp có 3 phần tử
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(4)#thêm phần tử vào ngăn xếp
custom_stack.delete()
#print(custom_stack.delete()) #None
#print(custom_stack)
#print(custom_stack.pop()) #lấy ra ptu ở đỉnh ngăn xếp
#print(custom_stack.peek()) #trả về giá trị ở đỉnh ngăn xếp, mà không loại bỏ các ptu khác
    

