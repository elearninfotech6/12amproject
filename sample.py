class student:
        '''doc strng example starting heading'''
        name='ravi'
        rno=123
        marks=90
        def read(self):  
                print('reading')
                rno=100
                print(self.rno)
        def write(self):
                print('writing')
obj=student()
print(obj.name)
print(obj.rno)
print(obj.marks)
obj.read()
obj.write()
print(obj.__doc__)

