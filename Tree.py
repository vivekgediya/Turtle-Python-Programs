import turtle

WIDTH = 10
BRANCH_LENGTH = 120
ROTATION_LENGTH = 29
turtle.bgcolor('black')
turtle.title('Fractional_Tree')

class Tree_Fractal(turtle.Turtle):
    def __init__(self, level):
        super(Tree_Fractal, self).__init__()
        self.pencolor('brown')
        self.level = level
        self.hideturtle()
        self.speed(100)
        self.left(90)
        self.width(WIDTH)
        self.penup()
        #self.pencolor('green')
        self.back(BRANCH_LENGTH * 2.5)
        self.pendown()
        self.forward(BRANCH_LENGTH)
        self.draw_tree(BRANCH_LENGTH, level)

    def draw_tree(self, branch_length, level):
        width = self.width()
        
        self.width(width * 3. / 4.)
        branch_length *= 3. / 4.
        self.left(ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
            #self.pencolor('green')
            self.pencolor('brown')
        self.back(branch_length)
        self.right(2 * ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.pencolor('green')
        self.back(branch_length)
        self.left(ROTATION_LENGTH)

        self.width(width)

if __name__ == '__main__':
    tree_level = 8
    tree = Tree_Fractal(tree_level)
    turtle.done()



