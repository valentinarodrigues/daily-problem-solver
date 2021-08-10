class Solution(object):
    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        # print(symbols)
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        # print(symbols)


        ans = list(dominoes)
        print(list(zip(symbols, symbols[1:])))
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in range(i+1, j):
                    # cmp = lambda a,b: (a>b)-(a<b)
                    print('.LR'[cmp(k-i, j-k)])

                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)
'''
    -1 if a<b

    0 if a=b

    1 if a>b
'''
def cmp(a, b):
    return (a > b) - (a < b) 

solution = Solution()
print(solution.pushDominoes(".L.R...LR..L.."))

[((-1, 'L'), (1, 'L')), 
((1, 'L'), (3, 'R')),
((3, 'R'), (7, 'L')), 
((7, 'L'), (8, 'R')),
((8, 'R'), (11, 'L')),
((11, 'L'), (14, 'R'))]