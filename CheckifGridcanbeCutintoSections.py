# Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

# Output: true

def checkValidCuts(n, rectangles):
    return can_cut(rectangles, 0) or can_cut(rectangles, 1)

def can_cut(rectangles, axis):
    rectangles.sort(key=lambda x: x[axis])
    cuts, previous_end = 0, -1
    for rect in rectangles:
        start, end = rect[axis], rect[axis + 2]
        if start >= previous_end:
            cuts += 1
        previous_end = max(previous_end, end)
        if cuts >= 3:
            return True
    return False

n = 5
rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
print(checkValidCuts(n, rectangles)) 