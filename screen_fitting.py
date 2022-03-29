class Solution:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence)+' '
        print(s)
        print(len(s))
        start, l = 0,len(s)
        for i in range(rows):
            start+=cols
            print('start % l', start, l, start % l, s[start % l])
            '''
            consider  a b c d e f g h i j k l len =>11
            window is only 3 
            3 % 11 => 3
            consider  a b c d e  len =>5
            window is only 3 
            3 % 5 =>  3
            next iteration 
            3+1 => 4 
            4+ 3(window size)=>7
            7%5=> 2 which is the elements that will be left in the next row
            '''
            while s[start % l]!=' ': # 
                print('decrement')
                start-=1

            start+=1
        print('start', start)
        return start//l
s = Solution()
sentence = ["i","had","apple","pie"]
rows = 4
cols = 5
s.wordsTyping(sentence, rows, cols)