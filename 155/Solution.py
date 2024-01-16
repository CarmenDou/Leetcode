class MinStack:

    def __init__(self):
        self.st=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.min and self.min[-1]<val:
            return
        self.min.append(val)

    def pop(self) -> None:
        if self.min[-1]==self.st[-1]:
            self.min.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]