class pen ():
    def __init__ (self , colour , ballpoint , click ):
        self.a= colour
        self.b= ballpoint
        self.c= click
        print(self.a,self.b,self.c)
    def write (self):
        print("writing...")
    def scrible (self):
        print("scribling...")
    def draw (self):
        print("drawing...")
k=pen("blue","yes","no")
k.write()
k.scrible()
k.draw()
