'''
class 類別
object 物件

台大：學號 系級 班級 座號(屬性) class
alan:001.資工 A.   1   obj
kevin:010電機 B.   15
'''

class NTU:
    def __init__(self, name, student_number, major, class_name, class_number):#初始化函數
        self.name = name
        self.student_number = student_number
        self.major = major
        self.class_name = class_name
        self.class_number = class_number
    def bb(self):
        print(f'台大{self.major}爛死了')

alan = NTU('alan','001','資工','A', 1)
print(alan.major)
alan.bb()