class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if stack:
                while stack and stack[-1] > 0 and asteroid < 0:
                    tmp = stack.pop()
                    if abs(tmp) > abs(asteroid):
                        asteroid = tmp
                    elif abs(tmp) == abs(asteroid):
                        asteroid = 0
            if asteroid != 0:
                stack.append(asteroid)

        return stack