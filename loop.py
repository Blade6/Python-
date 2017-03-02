names = ['a','b','c'];
for item in names:
	print item

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
	print webster[key]

print 'O' * 5
# 'OOOOO'
print ['O'] * 5
# ['O', 'O', 'O', 'O', 'O']

board = []
for i in range (5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
# O O O O O
# O O O O O
# O O O O O
# O O O O O
# O O O O O

choices = ['pizza', 'pasta', 'salad', 'nachos']
for index, item in enumerate(choices):
	print index, item