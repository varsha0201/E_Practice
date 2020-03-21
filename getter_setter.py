class Edureka:
    def __init__(self,courseName):
        self.courseName=courseName
       

    def setCource_Name(self,courseName):
        self.courseName=courseName.upper()


    def getCource_Name(self):
        return(self.courseName)
        
e = Edureka('Python')

print(e.getCource_Name())


e.setCource_Name("machine learning")
print(e.getCource_Name())


