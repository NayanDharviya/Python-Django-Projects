##a='nanna'
####n='x'
##a1=a[0]
##b=a[1:]
##r=b.replace('n','x')
##print(a1+r)
##
##
##

class FileHandling():
    def __init__(self,name):
        self.filename=name
##        print('name of the user is',self.user)

        print("#########read the file")
        f=open(self.filename,'rt')
        c=f.read()
        print(c)

    def writefile(self):
        
        print("#########write into file")
        
        f=open(self.filename,'at')
        d=input('enter text')
        f.write(d)
        f.close()

        print("###########read th file after write")
        f=open(self.filename,'rt')
        c=f.read()
        print(c)
        
n=input('Enter file name')
c=FileHandling(n)
c.writefile()
