
def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open(filename, 'r') as input_file:
        return [[int(column) for column in row.split()] for row in input_file]

dataset = read_matrix("testmatrix0.txt")



def read_matrix1(matrix):
        for i in range(len(matrix)):
                matrix[i]
                
                j = 0
                while j < len(matrix[i]):
                        print(matrix[i][j], end=' ')
                        
                        j +=1
                
                print()

read_matrix1(dataset)

def sum_rows(m):
        sum_rows = [sum(i) for i in m]
        sums = list(map(lambda x: str(x), sum_rows))
        x_sum = " ".join(sums)
        print("Row Sums: ", x_sum)
        
def colum_sum(m):
        sums_col = [sum(i) for i in zip(*m)]
        str_col = list(map(lambda x: str(x), sums_col))
        join_col = " ".join(str_col)
        print("Column Sums: ", join_col)
                
colum_sum(dataset)