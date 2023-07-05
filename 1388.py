def SearchRow(r, c) :
    global Visited, Shape, Row, Column
    if c < 0 or c >= Column or Visited[r][c] == True :
        return
    if Shape[r][c] != 0 :
        return
    Visited[r][c] = True
    SearchRow(r, c-1)
    SearchRow(r, c+1)
    
def SearchColumn(r, c) :
    global Visited, Shape, Row, Column
    if r < 0 or r >= Row or Visited[r][c] == True :
        return
    if Shape[r][c] == 0 :
        return
    Visited[r][c] = True
    SearchColumn(r-1, c)
    SearchColumn(r+1, c)

N = list(map(int, input("").split()))
Row = N[0]
Column = N[1]

Visited = []
Shape = []
for i in range(Row) :
    N = input("")
    lst = []
    lst_ = []
    for j in range(Column) :
        if N[j] == "-" :
            lst.append(0)
        else :
            lst.append(1)
        lst_.append(False)
    Shape.append(lst)
    Visited.append(lst_)

result = 0
for i in range(Row) :
    for j in range(Column) :
        if Visited[i][j] == False and Shape[i][j] == 0 :
            SearchRow(i, j)
            result += 1
        elif Visited[i][j] == False and Shape[i][j] == 1 :
            SearchColumn(i, j)
            result += 1
            
print(result)