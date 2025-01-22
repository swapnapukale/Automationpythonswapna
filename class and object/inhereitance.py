# class father:
#     def __init__(self, fname, fhouse, fcar):
#         self.fname = fname
#         self.fhouse = fhouse
#         self.fcar = fcar
#
#     def show_father_name(self):
#         print("Father name is :", self.fname)
#
#     def show_father_house(self):
#         print("Father is owning house:", self.fhouse)
#
#     def show_father_car(self):
#         print("Father is owening car ", self.fcar)
#
#
# class son(father):
#     def __init__(self, son_name, fname, fhouse, fcar):
#         super().__init__(fname,fhouse,fcar)
#         self.son_name = son_name
#
#     def show_son_name(self):
#         print(f"The son name is: {self.son_name}")
#
#     def show_all_details(self):
#         self.show_father_name()
#         self.show_father_car()
#         self.show_father_house()
#         self.show_son_name()
#
#
# obj = son('Rohit', 'Mohan Gupta',  '4 BHK', 'BMW')
# obj.show_all_details()

""" Multilvel inhereritence from grand father>>father>>son"""

class grandfather:
    def __init__(self,gname,gsal,gcity):
        self.gname = gname
        self.gsal = gsal
        self.gcity = gcity

    def show_gname(self):
        print("grand father name is ", self.gname)

    def show_gsal(self):
        print("grand father sal is ", self.gsal)

    def show_gcity(self):
        print("grand father city is", self.gcity)



""" father inherit from grandfather"""

class father(grandfather):
    def __init__(self, fname,gname,gcity,gsal ):
        super().__init__(gname,gsal,gcity)
        self.fname = fname

    def  show_fathername(self):
        print("father name is",self.fname)



class son(father):
    def __init__(self,sname,scity,fname,gname,gcity,gsal):
        super().__init__(fname,gname,gcity,gsal)
        self.sname = sname
        self.scity = scity

    def show_sonname(self):
        print("son name is ", self.sname)

    def show_scity(self):
        print("son city is ",self.scity)


    def show_alldetails(self):
        self.show_gname()
        self.show_gcity()
        self.show_gsal()
        self.show_fathername()
        self.show_sonname()
        self.show_scity()


obj = son("bhimu","pune","maru","bhima","dubalgundi",10000)
obj.show_alldetails()