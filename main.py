from kivy.app import App
from kivy.uix.button import Button

import relations
import kivy
from kivy.app import App
from kivy.modules import inspector
from kivy.core.window import Window

class MatrixElement(Button):
    def __init__(self, value=0, **kwargs):
        super().__init__(**kwargs)
        self.text = value

class RelationsApp(App):
    def build(self):
        inspector.create_inspector(Window, self)

    def create_matrix(self, text):
        size = int(text)
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(0)
        self.change_view(matrix)

    def change_view(self, matrix):
        for row in matrix:
            for item in row:
                pass


def main():
    result = relations.check_reflexive([[1,0,0],[0,1,0],[0,0,1]])
    print(result)
    result = relations.check_irreflexive([[0,1,0],[0,0,0],[0,1,0]])
    print(result)
    result = relations.make_reflexive([[1,0,0],[0,1,0],[0,0,0]])
    for row in result:
        print(row)
    result = relations.make_reflexive([[1, 0, 0,0], [0, 1, 0,1], [0, 0, 0, 0], [0, 0, 0, 0]])
    for row in result:
        print(row)
    result = relations.check_symmetric([[0,1,0],[0,0,0],[0,0,0]])
    print(result)
    result = relations.check_symmetric([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    print(result)
    for row in [[0, 1, 0], [1, 0, 0], [0, 0, 0]]:
        print(row)
    result = relations.make_symmetric([[0,1,0],[0,0,0],[0,0,0]])
    for row in result:
        print(row)
    result = relations.make_antisymmetric([[0, 1, 0], [1, 0, 1], [0, 0, 0]])
    for row in result:
        print(row)
    result = relations.check_transitive([[0,1,0],[1,1,0],[0,0,0]])
    print(result)
    result = relations.make_transitive([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    for row in result:
        print(row)
    result = relations.make_transitive([[1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]])
    for row in result:
        print(row)
    result = relations.check_transitive([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
    print(result)


if __name__ == '__main__':
    main()
    app = RelationsApp()
    app.run()