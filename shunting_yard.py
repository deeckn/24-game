class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if not self.is_empty():
            return self.array.pop()

    def peek(self):
        if not self.is_empty():
            return self.array[len(self.array)-1]

    def is_empty(self):
        return len(self.array) == 0


class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        if not self.is_empty():
            value = self.array[0]
            self.array.remove(self.array[0])
            return value

    def is_empty(self):
        return len(self.array) == 0


class ShuntingYard:
    def __init__(self):
        self.__stream = Queue()
        self.__queue = Queue()
        self.__stack = Stack()

    def __clear(self):
        self.__queue = Queue()
        self.__stack = Stack()

    def __make_string(self, user_input: str):
        for token in user_input:
            self.__stream.enqueue(token)

    def __get_precedence(self, op):
        if op == "+" or op == "-":
            return 1
        elif op == "*" or op == "/":
            return 2
        else:
            return -1

    def __compute_infix(self):
        while not self.__stream.is_empty():
            t = self.__stream.dequeue()
            if t.isnumeric():
                self.__queue.enqueue(t)
            elif t == "(":
                self.__stack.push(t)
            elif t == ")":
                while not self.__stack.peek() == "(":
                    self.__queue.enqueue(self.__stack.pop())
                self.__stack.pop()
            else:
                while (not self.__stack.is_empty()) and self.__get_precedence(t) <= self.__get_precedence(self.__stack.peek()):
                    self.__queue.enqueue(self.__stack.pop())
                self.__stack.push(t)

        while not self.__stack.is_empty():
            self.__queue.enqueue(self.__stack.pop())

    def __compute_rpn(self) -> float:
        stack = Stack()
        while not self.__queue.is_empty():
            t = self.__queue.dequeue()
            if t.isnumeric():
                stack.push(t)
                continue

            b = float(stack.pop())
            a = float(stack.pop())
            match (t):
                case "-":
                    stack.push(a-b)
                case "+":
                    stack.push(a+b)
                case "*":
                    stack.push(a*b)
                case "/":
                    stack.push(a/b)
        return float(stack.pop())

    def compute(self, user_input) -> float:
        self.__make_string(user_input)
        self.__compute_infix()
        result = self.__compute_rpn()
        self.__clear()
        return result
