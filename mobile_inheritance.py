#inheritance example

class MobilePhone:
    def __init__(self,ScreenType,Networktype,Dualsim,FrontCamera,rearCamera,RAM,Storage):
        self.ScreenType=ScreenType
        self.Networktype=Networktype
        self.Dualsim=Dualsim
        self.FrontCamera=FrontCamera
        self.rearCamera=rearCamera
        self.RAM=RAM
        self.Storage=Storage
#functionalities
    def make_call(self,number):
        print(f"calling {number}...")
    def receive_call(self):
        print("Incoming Call Received")
    def take_a_picture(self):
        print(f"picture taken using {self.rearCamera} camera.")        
        

    def show_specs(self):
        print("Screen Type: ",self.ScreenType)
        print("Network Type: ",self.Networktype)   
        print("Dualsim: ",self.Dualsim)   
        print("FrontCamera: ",self.FrontCamera)   
        print("rearCamera: ",self.rearCamera)   
        print("RAM: ",self.RAM)
        print("Storage: ",self.Storage)

   

#apple child class
class Apple(MobilePhone):
     def __init__(self,ScreenType,Networktype,Dualsim,FrontCamera,rearCamera,RAM,Storage):
        super().__init__(
            "Touch Screen",
            "4G",
            True,
            "12MP",
            "48MP",
            "4GB",
            "64GB"
        )
    def brand(self):
        print("Brand: Apple iphone") 
#samsung class(child class)
class Samsung(MobilePhone):
    def __init__(self,ScreenType,Networktype,Dualsim,FrontCamera,rearCamera,RAM,Storage):
        super().__init__(
            "Touch Screen",
            "5G",
            False,
            "16MP",
            "32MP",
            "4GB",
            "64GB"
        )
    def brand(self):
        print("Brand: Samsung Galaxy")

#Creating Apple objects
iphone13 = Apple("5G", True, "12MP", "48MP", "4GB", "64GB")
iphone14 = Apple("5G", False, "16MP", "48MP", "4GB", "128GB")


#Using apple method
iphone13=Apple()
iphone13.brand()
iphone13.make_call("9865783392")
iphone13.receive_call()
iphone13.take_a_picture()
iphone13.show_specs()
iphone14.brand()
iphone14.show_specs()
print("---------")
#creating samsung objects
samsungA = Samsung("4G", True, "8MP", "32MP", "3GB", "64GB")
samsungS = Samsung("5G", True, "16MP", "48MP", "4GB", "128GB")

SamsungA=Samsung()
SamsungA.brand()
SamsungA.make_call("9675783342")
SamsungA.receive_call()
SamsungA.take_a_picture()
SamsungA.show_specs()

SamsungS.brand()
SamsungS.show_specs()
