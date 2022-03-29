class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    if p1 == p2 == p3 == p4:
        return False
        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        area = sorted([dist(p1, p2), dist(p2,p3), dist(p3,p4), dist(p4, p1), dist(p4, p2), dist(p1, p3)])
        if area[0] == area[1] == area[2] == area[3] and if area[4] == area[5]:
    return True
return False
        

