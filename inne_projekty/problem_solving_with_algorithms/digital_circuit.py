class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getName() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getName() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getName() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
        
        
class NandGate(AndGate):
    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1
            
            
class NorGate(OrGate):
    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


def main():
   '''g1 = AndGate("G1")
   g2 = AndGate("G2")
   #g2 = NandGate("G2")
   #print(g2.getOutput())
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1, g3)
   c2 = Connector(g2, g3)
   c3 = Connector(g3, g4)
   print(g4.getOutput())'''
   
   # Checking if true:
   # NOT((A and B) or (C and D)) == NOT(A and B) and NOT(C and D) 
   g1 = AndGate("A")
   g2 = OrGate("B")
   g3 = AndGate("C")
   g4 = AndGate("D")
   g5 = AndGate("E")
   g6 = AndGate("F")
   g7 = NorGate("G")
   g8 = NandGate("H")
   g9 = NandGate("I")
   g10 = AndGate("J")
   c1 = Connector(g1, g5)
   c2 = Connector(g2, g5)
   c3 = Connector(g3, g6)
   c4 = Connector(g4, g6)
   c5 = Connector(g5, g7)
   c6 = Connector(g6, g7)
   
   c7 = Connector(g1, g8)
   c8 = Connector(g2, g8)
   c9 = Connector(g3, g9)
   c10 = Connector(g4, g9)
   c11 = Connector(g8, g10)
   c12 = Connector(g9, g10)

   print(g7.getOutput() == g10.getOutput())
   


main()
