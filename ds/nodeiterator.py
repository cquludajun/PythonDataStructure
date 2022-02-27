class NodeIterator:
    def __init__(self, first):
        self.cur = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is not None:
            cur = self.cur
            self.cur = self.cur.next
            return cur.data
        else:
            raise StopIteration
