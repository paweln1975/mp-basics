class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, el):
        self.__stack.append(el)

    def pop(self):
        return self.__stack.pop(len(self.__stack) - 1)

    def peek(self):
        return self.__stack[len(self.__stack) - 1]

    def is_empty(self):
        return len(self.__stack) == 0

    def get_stack(self):
        return self.__stack
