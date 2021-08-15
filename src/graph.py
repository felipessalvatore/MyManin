# #!/usr/bin/env python
# # python3 -m manim gamma.py CreateGraph -p


from manim import *
import numpy as np


WAIT_TIME = 1

def get_exp(i):
    return lambda x: x*i

# def get_exp(i):
#     return lambda x: (x**(i-1))*np.exp(-x)


def get_exp_label(i):
    return 'x^{}'.format(i)


def get_exp_label(i):
    return 'x^{' + str(i) + "-1} e^{-x}"



class CreateGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-5, 5],
            axis_config={"color": BLUE},
        )

        # Create Graph
        graph = axes.get_graph(lambda x: x**2, color=WHITE)
        graph_label = axes.get_graph_label(graph, label='x^{2}')

        graph2 = axes.get_graph(lambda x: x**3, color=WHITE)
        graph_label2 = axes.get_graph_label(graph2, label='x^{3}')

        # Display graph
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(1)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(1)

        # self.play(FadeOut(graphs[0]),
        #           Transform(graphs[0+1], graphs[0+2]))
        # self.wait(WAIT_TIME)
        # self.play(FadeOut(graphs[0+1]),
        #           Transform(graphs[0+2], graphs[0+3]))
        # self.wait(WAIT_TIME)




        # Display graph
        # self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        # self.play(Create(axes), Create(graph), Write(graph_label))
        # graph_label3 = axes.get_graph_label(graph3, label=get_exp_label(4))
        # graph_label = axes.get_graph_label(graph, label=get_exp_label(2))
        # graph_label2 = axes.get_graph_label(graph2, label=get_exp_label(3))
        # graph_label4 = axes.get_graph_label(graph4, label=get_exp_label(5))
        # self.play(FadeOut(graph),
        #           FadeOut(graph_label),
        #           Transform(graph2, graph3),
        #           Transform(graph_label2, graph_label3))
# class CreateGraph(Scene):
#     def construct(self):
#         axes = Axes(
#             x_range=[0, 5],
#             y_range=[0, 5],
#             axis_config={"color": BLUE},
#         )

#         # Create Graph
#         graphs = []
#         graph_labels = []
#         for i in range(1,5):
#             graph = axes.get_graph(lambda x: x**(i-1)*np.exp(-x), color=WHITE)
#             graph_label = axes.get_graph_label(graph, label=get_exp_label(i)xp(-{})'.format(i,i))
#             graphs.append(graph)
#             graph_labels.append(graph_label)


#         # graph2 = axes.get_graph(lambda x: x**3, color=WHITE)
#         # graph_label2 = axes.get_graph_label(graph2, label='x^{3}')

#         # Display graph
#         base_graph = graphs[0]
#         base_label = graph_labels[0]
#         graph_transforms = []
#         for i in range(len(graphs) -1):
#             tg = Transform(graphs[i], graphs[i+1])
#             tgl = Transform(graph_labels[i], graph_labels[i+1])
#             # fadeg = FadeOut(graphs[i])
#             # fadelg = FadeOut(graph_labels[i])

#             graph_transforms.append(tg)
#             graph_transforms.append(tgl)
#             # graph_transforms.append(fadeg)
#             # graph_transforms.append(fadelg)




#         initial = [Create(axes), Create(base_graph), Write(base_label)]
#         self.play(*initial)
#         self.wait(1)
#         init = 0
#         for i in range(2,len(graph_transforms),2):
#             print(i)
#             self.play(*graph_transforms[init:i])
#             self.wait(1)
#             init += 2

#         # graph_transforms
#         # for i in range(len(graphs) -1):

#         # self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
#         # self.wait(2)