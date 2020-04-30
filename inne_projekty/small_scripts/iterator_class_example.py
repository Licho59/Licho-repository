# from serie 'Dead Simple Python':
# https://dev.to/codemouse92/dead-simple-python-loops-and-iterators-15bp
# to show own interator class implemented


class AgentRoster:
    def __init__(self):
        self._agents = {}
        self._classified = []

    def add_agent(self, name, number, classified=False):
        self._agents[number] = name
        if classified:
            self._classified.append(name)

    def validate_number(self, number):
        try:
            name = self._agents[number]
        except KeyError:
            return False
        else:
            return True

    def lookup_agent(self, number):
        try:
            name = self._agents[number]
        except KeyError:
            name = "<NO KNOWN AGENT>"
        else:
            if name in self._classified:
                name = "<CLASSIFIED>"
        return name

    def __iter__(self): #says how to iterate AgentRoster() object
        return AgentRoster_Iterator(self)


class AgentRoster_Iterator:
    """Iterator which loops over defined range"""
    def __init__(self, container):
        self._classified = container._classified
        self._roster = [(k, container._agents[k]) for k,v in container._agents.items() if v not in self._classified]
        self._index = 0

    def __next__(self):
        if self._index == len(self._roster):
            raise StopIteration
        else:
            r = self._roster[self._index]
            self._index += 1
            return r
        

roster = AgentRoster()

roster.add_agent("Ann Tickwitee", 2539634)
roster.add_agent("Chase Devineaux", 1495263, True)
roster.add_agent("Ivan Idea", 1324595)
roster.add_agent("Rock Solid", 1385723)

for number, name in roster:
    print(f'{name}, id #{number}')
