class Solution:
    def simplifyPath(self, path: str) -> str:
        directions = path.split("/")
        stack = []
        for direction in directions:
            if direction:
                if direction == ".":
                    pass
                elif direction == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(direction)
        return "/" + "/".join(stack)