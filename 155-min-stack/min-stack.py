class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        self.stack.append(value)

        if len(self.minstack) == 0:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value, self.minstack[-1]))

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]