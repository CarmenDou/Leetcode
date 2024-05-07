class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = None
        
        def backtrack(state, choices, visited):
            if len(state) == 2**n:
                if is_solution(state):
                    print(state)
                    record_solution(state)
                return

            for i in range(len(choices)):
                # print(visited)
                if visited[i] != 1:
                    visited[i] = 1
                    if is_valid(state, choices[i]):
                        state.append(choices[i])
                        # print(state)
                        backtrack(state, choices, visited)
                        state.pop()
                    visited[i] = 0
                    # undo_choice(state, choice)

        def is_solution(state):
            xor_result = state[-1] ^ state[0]
            # Check if xor_result is a power of two
            return (xor_result & (xor_result - 1)) == 0 and xor_result != 0

        def record_solution(state):
            print("record_solution")
            result = state
            print(result)

        def is_valid(state, choice):
            xor_result = state[-1] ^ choice
            # Check if xor_result is a power of two
            return (xor_result & (xor_result - 1)) == 0 and xor_result != 0

        nums = [i for i in range(1,2**n)]
        visited = [0 for i in range(1,2**n)]
        backtrack([0], nums, visited)

        return result

