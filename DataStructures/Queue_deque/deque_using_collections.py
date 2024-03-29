from collections import deque

if __name__ == "__main__":
    # Initializing a queue
    q = deque()

    # Adding elements to a queue
    q.append('a')
    q.append('b')
    q.append('c')

    print("Initial queue")
    print(q)

    # Removing elements from a queue
    print("\nElements dequeued from the queue")
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())

    print("\nQueue_deque after removing elements")
    print(q)

