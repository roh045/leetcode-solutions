class Answer:
    def numTrees(self, n):
        memo = {}

        def count(start, end):
            if start > end:
                return 1
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            total = 0
            
            for i in range(start, end + 1):
                left = count(start, i - 1)
                right = count(i + 1, end)
                total += left * right
            
            memo[(start, end)] = total
            return total
        
        return count(1, n)