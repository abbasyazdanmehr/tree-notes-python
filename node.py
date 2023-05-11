class Node:
    def __init__(self, key, title='', description='') -> None:
        self.key = key
        self.title = title
        self.description = description
        self.children = []
        
    def __repr__(self) -> str:
        return " #" + str(self.key) + \
    " - " + self.title
    