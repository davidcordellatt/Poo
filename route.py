class Route:
    user = 1
    start   = list
    end     = list
    escorts = int

    def __init__(self, start, end, escorts,user = 1):
        self.start = start
        self.end = end
        self.escorts = escorts

        if user + escorts <= 3:
            print("Necesitan el carro X")

        else:
            print("Necesitan el carro Y")