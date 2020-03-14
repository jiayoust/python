import heapq
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        heapq.heappush(self.items, (priority, item))
    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    pq = Queue()
    pq.enqueue(3, 3)
    pq.enqueue(2, 2)
    pq.enqueue(1, 1)
    pq.enqueue(4, 4)
    pq.enqueue(5, 5)
    print(pq.size())
    while not pq.is_empty():
        print(pq.dequeue())
    print(pq.size())


if __name__ == '__main__':
    main()