import functools

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_size = len(hand)
        hand = ''.join(sorted(hand))

        @functools.cache
        def recursive_search(curr_board, remaining_hand):
            curr_board = self.optimize(curr_board)
            if curr_board == '': 
                return hand_size - len(remaining_hand)
            if remaining_hand == '': 
                return float('inf')

            min_steps = float('inf')
            for i in range(len(remaining_hand)):
                if i > 0 and remaining_hand[i] == remaining_hand[i - 1]:
                    continue

                for j in range(len(curr_board)):
                    if curr_board[j] == remaining_hand[i] or (j > 0 and curr_board[j] == curr_board[j - 1] and curr_board[j] != remaining_hand[i]):
                        next_board = curr_board[:j] + remaining_hand[i] + curr_board[j:]
                        optimized_board = self.optimize(next_board)
                        min_steps = min(min_steps, recursive_search(optimized_board, remaining_hand[:i] + remaining_hand[i + 1:]))

            return min_steps
        
        result = recursive_search(board, hand)
        return result if result != float('inf') else -1

    @functools.cache
    def optimize(self, s):
        stack = []
        for char in s:
            if stack and stack[-1][0] != char and stack[-1][1] >= 3:
                stack.pop()
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
        if stack and stack[-1][1] >= 3:
            stack.pop()
        return ''.join(a * b for a, b in stack)
