# 1. Create inheritance using MobilePhone as base class and Apple &
# Samsung as child class
# 1. The base class should have properties:
# 1. ScreenType = Touch Screen
# 2. NetworkType = 4G/5G
# 3. DualSim = True or False
# 4. FrontCamera = (5MP/8MP/12MP/16MP)
# 5. rearCamera = (8MP/12MP/16MP/32MP/48MP)
# 6. RAM = (2GB/3GB/4GB)
# 7. Storage = (16GB/32GB/64GB)

class MobilePhone:
    def __init__(self,ScreenType,Networktype,Dualsim,FrontCamera,rearCamera,RAM,Storage):
        self.ScreenType=ScreenType
        self.Networktype=Networktype
        self.Dualsim=Dualsim
        self.FrontCamera=FrontCamera
        self.rearCamera=rearCamera
        self.RAM=RAM
        self.Storage=Storage

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

   


class Apple(MobilePhone):
    def __init__(self):
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

class Samsung(MobilePhone):
    def __init__(self):
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

iphone=Apple()
iphone.brand()
iphone.make_call("9865783392")
iphone.receive_call()
iphone.take_a_picture()
iphone.show_specs()

print("---------")
Samsung_phone=Samsung()
Samsung_phone.brand()
Samsung_phone.make_call("9675783342")
Samsung_phone.receive_call()
Samsung_phone.take_a_picture()
Samsung_phone.show_specs()
