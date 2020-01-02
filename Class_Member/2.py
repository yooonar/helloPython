class Cs:
    @static_method
    def static_method() :
        print("Static method")
    @classmethod
    def class_method(cls) :
        print("Class method")
    def instance_method(self) :
        print("Instance method")

i = Cs()
Cs.static_method()
Cs.class_mthod()

i.instance_method()
