from os import wait3

from kivy.app import App
from kivy.properties import StringProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

import relations
import kivy
from kivy.app import App
from kivy.modules import inspector
from kivy.core.window import Window



class MatrixOperators(BoxLayout):
    def __init__(self, **kwargs):
        super(MatrixOperators, self).__init__(**kwargs)
        self.id = 'operators'
        self.all_button = AllButton()
        self.add_widget(self.all_button)
        self.add_widget(OptionSpinner(self.all_button))

class AllButton(Button):
    instance = App.get_running_app()

    def __init__(self, **kwargs):
        super(AllButton, self).__init__(**kwargs)
        self.id = 'all_button'
        self.text = "Check All"

    def check_spinner(self):
        instance = App.get_running_app()
        return instance.option

    def choose_option(self, option, matrix):
        instance = App.get_running_app()
        most_recent = instance.root.ids.something.children[0]
        if isinstance(most_recent, kivy.uix.label.Label):
            instance.root.ids.something.remove_widget(most_recent)
        result = Label(text="Something went wrong and the result wasn't calculated.", color=(173/225, 2/225, 2/225, 1))
        if option == "Check Matrix" or option == "All":
            reflexive = relations.check_reflexive(matrix)
            irreflexive = relations.check_irreflexive(matrix)
            symmetric = relations.check_symmetric(matrix)
            antisymmetric = relations.check_antisymmetric(matrix)
            asymmetric = relations.check_asymmetric(matrix)
            transitive = relations.check_transitive(matrix)
            equivalence = relations.check_equivalence(matrix)
            result = Label(text=f"Reflexive: {reflexive}\nIrreflexive: {irreflexive}\nSymmetric: {symmetric}\n"
                                f"Antisymmetric: {antisymmetric}\nAsymmetric: {asymmetric}\nTransitive: {transitive}\n"
                                f"Equivalence: {equivalence}", size_hint_y=None, text_size=(300,None), font_size=25)
            result.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        elif option == "Reflexive":
            reflexive = relations.check_reflexive(matrix)
            result = Label(text=f"{reflexive}")
        elif option == "Irreflexive":
            irreflexive = relations.check_irreflexive(matrix)
            result = Label(text=f"{irreflexive}")
        elif option == "Symmetric":
            symmetric = relations.check_symmetric(matrix)
            result = Label(text=f"{symmetric}")
        elif option == "Asymmetric":
            asymmetric = relations.check_asymmetric(matrix)
            result = Label(text=f"{asymmetric}")
        elif option == 'Antisymmetric':
            antisymmetric = relations.check_antisymmetric(matrix)
            result = Label(text=f"{antisymmetric}")
        elif option == 'Transitive':
            transitive = relations.check_transitive(matrix)
            result = Label(text=f"{transitive}")
        instance.root.ids.something.add_widget(result)

    def on_press(self):
        instance = App.get_running_app()
        matrix = instance.matrix
        option = self.check_spinner()
        self.choose_option(option, matrix)

class OptionSpinner(Spinner):
    def __init__(self, all_button, **kwargs):
        super(OptionSpinner, self).__init__(**kwargs)
        self.all_button = all_button
        self.id = 'option_spinner'
        self.text = 'Check Matrix'
        self.values = ('Reflexive', 'Irreflexive', 'Symmetric', 'Antisymmetric', 'Asymmetric', 'Transitive', 'Equivalence', 'All')

    def on_text(self, instance, value):
        instance = App.get_running_app()
        # if not hasattr(root, 'ids') or 'all_button' not in root.ids:
        #     return  # Too early, or the button doesn't exist
        if not self.text == 'Check Matrix' and not self.text == 'All':
            self.all_button.text = 'Confirm'
        else:
            self.all_button.text = 'Check All'
        instance.option = self.text

class MatrixElement(Button):

    def __init__(self, row, col, **kwargs):
        super().__init__(**kwargs)
        self.text = str(0)
        self.id = f"{row} {col}"

    def on_press(self, *args):
        instance = App.get_running_app()
        pos_x = int(self.id.split(' ')[0])
        pos_y = int(self.id.split(' ')[1])
        if self.text == '0':
            instance.matrix[pos_x][pos_y] = 1
            self.text = '1'
        elif self.text == '1':
            instance.matrix[pos_x][pos_y] = 0
            self.text = '0'

class MatrixLayout(BoxLayout):
    def __init__(self, width, row_pos, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        for i in range(width):
            self.add_widget(MatrixElement(row_pos, i))

class RelationsCalcApp(App):
    matrix_size = 0
    matrix = []

    def build(self):
        inspector.create_inspector(Window, self)

    def form_matrix(self, text):
        self.matrix_size = size = int(text)
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(0)
        self.matrix = matrix
        self.change_view()

    def create_matrix(self, text):
        if int(text) <= 0:
            pass
        elif not len(self.root.ids.something.children) > 1:
            self.form_matrix(text)
        elif not len(self.root.ids.something.children) == int(text) - 1:
            layout = self.root.ids.something
            children_to_remove = [child for child in layout.children if not isinstance(child, TextInput)]
            for child in children_to_remove:
                layout.remove_widget(child)
            self.form_matrix(text)

    def change_view(self):
        matrix_copy = self.matrix
        for row in range(len(matrix_copy)):
            self.root.ids.something.add_widget(MatrixLayout(self.matrix_size, row))
        self.root.ids.something.add_widget(MatrixOperators())



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
    app = RelationsCalcApp()
    app.run()