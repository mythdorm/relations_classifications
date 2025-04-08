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
        self.add_widget(FixerButton())
        self.add_widget(FixerSpinner())

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
            result = Label(text=f"Reflexive: {reflexive}")
        elif option == "Irreflexive":
            irreflexive = relations.check_irreflexive(matrix)
            result = Label(text=f"Irreflexive: {irreflexive}")
        elif option == "Symmetric":
            symmetric = relations.check_symmetric(matrix)
            result = Label(text=f"Symmetric: {symmetric}")
        elif option == "Asymmetric":
            asymmetric = relations.check_asymmetric(matrix)
            result = Label(text=f"Asymmetric: {asymmetric}")
        elif option == 'Antisymmetric':
            antisymmetric = relations.check_antisymmetric(matrix)
            result = Label(text=f"Antisymmetric: {antisymmetric}")
        elif option == 'Transitive':
            transitive = relations.check_transitive(matrix)
            result = Label(text=f"Transitive: {transitive}")
        elif option == 'Equivalence':
            equivalence = relations.check_equivalence(matrix)
            result = Label(text=f"Equivalence: {equivalence}")
        instance.root.ids.something.add_widget(result)

    def on_press(self):
        instance = App.get_running_app()
        matrix = instance.matrix
        option = self.check_spinner()
        self.choose_option(option, matrix)

class FixerSpinner(Spinner):
    def __init__(self, **kwargs):
        super(FixerSpinner, self).__init__(**kwargs)
        self.text = "Fix Matrix"
        self.values = ('Reflexive', 'Irreflexive', 'Symmetric', 'Antisymmetric', 'Asymmetric', 'Transitive', 'Equivalence')

    def on_text(self, instance, value):
        instance = App.get_running_app()
        instance.fix_option = self.text

class FixerButton(AllButton):
    def __init__(self, **kwargs):
        super(FixerButton, self).__init__(**kwargs)
        self.text = 'Fix'

    def check_differences(self, matrix, new_matrix):
        changes = []
        if not matrix == new_matrix:
            for row in range(len(matrix)):
                if not matrix[row] == new_matrix[row]:
                    for col in range(len(matrix[row])):
                        if not matrix[row][col] == new_matrix[row][col]:
                            changed = f"{matrix[row][col]} --> {new_matrix[row][col]}"
                            changes.append([(row, col), changed])
        return changes

    def choose_option(self, option, matrix):
        instance = App.get_running_app()
        new_matrix = [row[:] for row in matrix]
        changed = []
        result = Label()
        most_recent = instance.root.ids.something.children[0]
        if isinstance(most_recent, kivy.uix.label.Label):
            instance.root.ids.something.remove_widget(most_recent)
        result.text = "Something went wrong and the result wasn't calculated."
        if option == "Fix Matrix":
            result.text = "An option must first be picked to fix a matrix."
            result.color = (173/225, 2/225, 2/225, 1)
        if option == "Reflexive":
            new_matrix = relations.make_reflexive(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text
        elif option == "Irreflexive":
            new_matrix = relations.make_irreflexive(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text
        elif option == "Symmetric":
            new_matrix = relations.make_symmetric(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text
        elif option == "Asymmetric":
            new_matrix = relations.make_asymmetric(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text
        elif option == 'Antisymmetric':
            new_matrix = relations.make_antisymmetric(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text
        elif option == 'Transitive':
            new_matrix = relations.make_transitive(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text
        elif option == 'Equivalence':
            new_matrix = relations.make_equivalence(new_matrix)
            changed = self.check_differences(matrix, new_matrix)
            result_text = "Updated matrix with:\n"
            if len(changed) > 0:
                for difference in changed:
                    result_text += f"{difference[0]}: {difference[1]}\n"
            else:
                result_text = "No changes"
            result.text = result_text

        result.size_hint_y = None
        result.text_size = (300, None)
        result.font_size = 20
        result.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.fix_matrix(changed)
        instance.root.ids.something.add_widget(result)
        instance.matrix = new_matrix

    def fix_matrix(self, changes):
       if changes:
            coordinate_list =[]
            for change in changes:
                pos = change[0]
                coordinates = ''
                for coord in pos:
                    coordinates += f"{coord} "
                coordinate_list.append(coordinates)
            root = App.get_running_app().root
            for child in root.ids.something.children:
                if isinstance(child, MatrixLayout):
                    for element in child.children:
                        if element.id in coordinate_list:
                            if int(element.text) == 0:
                                element.text = str(1)
                            else:
                                element.text = str(0)
                            element.background_color = (135/255, 165/255, 207/255, 1)

    def reset_matrix_looks(self):
        root = App.get_running_app().root
        for child in root.ids.something.children:
            if isinstance(child, MatrixLayout):
                for element in child.children:
                    if  element.background_color == [135/255, 165/255, 207/255, 1]:
                        element.background_color = (1, 1, 1, 1)

    def check_spinner(self):
        instance = App.get_running_app()
        self.reset_matrix_looks()
        return instance.fix_option

class OptionSpinner(Spinner):
    def __init__(self, all_button, **kwargs):
        super(OptionSpinner, self).__init__(**kwargs)
        self.all_button = all_button
        self.id = 'option_spinner'
        self.text = 'Check Matrix'
        self.values = ('Reflexive', 'Irreflexive', 'Symmetric', 'Antisymmetric', 'Asymmetric', 'Transitive', 'Equivalence', 'All')

    def on_text(self, instance, value):
        instance = App.get_running_app()
        if not self.text == 'Check Matrix' and not self.text == 'All':
            self.all_button.text = 'Confirm'
        else:
            self.all_button.text = 'Check All'
        instance.option = self.text

class MatrixElement(Button):

    def __init__(self, row, col, value, **kwargs):
        super().__init__(**kwargs)
        self.text = str(value)
        self.id = f"{row} {col} "

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
    def __init__(self, width, row_pos, matrix, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        for i in range(width):
            self.add_widget(MatrixElement(row_pos, i, matrix[row_pos][i]))

class RelationsCalcApp(App):
    matrix_size = 0
    matrix = []

    def build(self):
        inspector.create_inspector(Window, self)
        self.matrix = []
        self.matrix_size = 0

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

    def form_matrix(self, text):
        self.matrix_size = size = int(text)
        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(0)
        self.matrix = matrix
        self.change_view()

    def change_view(self):
        matrix_copy = self.matrix
        for row in range(len(matrix_copy)):
            self.root.ids.something.add_widget(MatrixLayout(self.matrix_size, row, self.matrix))
        self.root.ids.something.add_widget(MatrixOperators())

if __name__ == '__main__':
    app = RelationsCalcApp()
    app.run()