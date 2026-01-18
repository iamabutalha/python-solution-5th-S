# PolyMorphism examples

class Rectangle:
    def area(self):
        return 5 * 4
    
    def area(self, isTrue):
        if isTrue:
            print("Hi")

rec = Rectangle()

print(rec.area(True))
print(rec.area(isTrue=False))