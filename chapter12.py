pop =  []
jpop = []

def collect_songs():
    song = "Please type song name."
    ask = "Please type p or j. You can exit by typing q."

    while True:
        genre = input(ask)
        if genre == "q":
            break
        elif genre == "p":
            p = input(song)
            pop.append(p)
        if genre == "j":
            j = input(song)
            jpop.append(j)
        else:
            print("Incorrect value.")
    
    print("pop songs: ",pop)
    print("jpop spngs: ",jpop)

collect_songs()


class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color =  c
        print("Created!")

orl = Orange(10, "dark orange")
print(orl)       
class Hexagon:
    def __init__(self,l):
        self.length = l
    def calculate_perimeter(self):
        perimeter = 6 * self.length
        return perimeter

hex = Hexagon(13)
print(hex.calculate_perimeter())
