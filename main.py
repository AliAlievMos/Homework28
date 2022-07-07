from graphviz import Digraph

# задание 1
list_of_branches = []


class Branch:

    def __init__(self, name, text):
        self.name = name
        self.text = text
        list_of_branches.append(self)

    @staticmethod
    def print_text():
        for i in range(len(list_of_branches)):
            print(list_of_branches[i].text)


branch1_Tsoy = Branch('first', 'Я знаю, мое дерево не проживет и недели.')
branch2_Tsoy = Branch('second', 'Я знаю, мое дерево в этом городе обречено. ')
branch3_Tsoy = Branch('third', 'Но я все свое время провожу рядом с ним: ')
branch4_Tsoy = Branch('fourth', 'Мне все другие дела надоели... ')
branch1_Cure = Branch('first', 'I hear her voice')
branch2_Cure = Branch('second', 'And start to run')
branch3_Cure = Branch('third', 'Into the trees')
branch4_Cure = Branch('fourth', 'Into the trees')



# Branch.print_text()

# Задание2

dot = Digraph(comment='The TreeSong Table')




dot.node('A', 'Dot A')
dot.node('B', 'Dot B')
dot.node('C', 'Dot C')
dot.node('D', 'Dot D')
dot.node('E', 'Dot E')
dot.node('F', 'Dot F')

dot.edges(['AB', 'DC', 'AD', 'BE', 'EF'])
dot.view()

print(dot.source)

# dot.render('test-output/TreeSong.gv', view=True)