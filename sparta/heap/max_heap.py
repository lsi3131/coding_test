class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def insert(self, k):
        self.items.append(k)
        self._percorlate_up()

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percorlate_down(1)
        return extracted

    def _percorlate_up(self):
        i = len(self)
        parent = i // 2

        while parent > 0:
            if self.items[i] > self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]

            i = parent
            parent = i // 2

    def _percorlate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] > self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] > self.items[smallest]:
            smallest = right

        if idx != smallest:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percorlate_down(smallest)


datas = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
bheap = BinaryHeap()
for d in datas:
    bheap.insert(d)

while len(bheap) > 0:
    print(bheap.extract())
    print(bheap.items)
