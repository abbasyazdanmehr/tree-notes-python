class Node:
    def __init__(self, key, title='', content='') -> None:
        self.key = key
        self.title = title
        self.content = content
        self.children = []
        
    def __repr__(self) -> str:
        return " #" + str(self.key) + \
    " - " + self.title
    