from manim import *

# CreateCircle
## First example showing creating a simple animation

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

# TwoObjects
## Draw two things next to each other
## NOTES: Actually generates a static image, not a video.

class TwoObjects(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=1.0)
        circle = Circle()
        circle.set_fill(PINK, opacity=1.0)
        square.next_to(circle, RIGHT)
        self.add(square)
        self.add(circle)

# TwoObjectsWait
## Show two objects, one then the next
## NOTES: They pop into existence.

class TwoObjectsWait(Scene):
    def construct(self):
        square = Square()
        square.set_fill(RED, opacity=1.0)
        circle = Circle()
        circle.set_fill(YELLOW, opacity=1.0)
        square.next_to(circle, RIGHT)
        self.add(square)
        self.wait()
        self.add(circle)
        self.wait()

# TwoObjectsDraw
## Draw two objects, one then the next
## NOTES: `Create` animates drawing based on vectorization of shape.

class TwoObjectsDraw(Scene):
    def construct(self):
        square = Square()
        square.set_fill(GREEN, opacity=1.0)
        circle = Circle()
        circle.set_fill(PURPLE, opacity=1.0)
        square.next_to(circle, RIGHT)
        self.play(Create(square))
        self.wait()
        self.play(Create(circle))
        self.wait()

# ThreeObjects
## Draw three objects with manual positioning

class ThreeObjects(Scene):
    def construct(self):
        for i in range(3):
            square = Square()
            square.shift(RIGHT * 3 * i + LEFT * 3)
            self.play(Create(square))
            self.wait()

# ObjectPlacement
## Draw shapes with different positions and alignments

class ObjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        circle.move_to(LEFT * 2)
        square.next_to(circle, LEFT)
        triangle.align_to(circle, LEFT)
        self.add(circle, square, triangle)
        self.wait(1)

# MoveObject
## Draws a square then slides it to the right

class MoveObject(Scene):
    def construct(self):
        square = Square()
        square.set_fill(PINK, opacity=0.5)
        self.play(Create(square))
        self.play(square.animate.shift(RIGHT))

# ShiftObject
## Draws a square not at default position then slides it to the left
## NOTES: `shift()` does adjustment immediately, `animate.shift()` makes an animation that does adjustment.

class ShiftObject(Scene):
    def construct(self):
        square = Square()
        square.shift(RIGHT * 2)
        square.set_fill(RED, opacity=0.5)
        self.play(Create(square))
        self.play(square.animate.shift(LEFT * 2))

# ShiftObjects
## Draws a square and a circle then slides them to the right
## NOTES: We construct a `VGroup` to contain multiple `Mobject`s.

class ShiftObjects(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        circle.next_to(square, RIGHT)
        group = VGroup()
        group.add(square)
        group.add(circle)
        self.play(Create(group))
        self.play(group.animate.shift(RIGHT))

# Try some more types of objects
## Draws a rectangle, rectangle with internal grid, and arrow
## NOTES: Uses `get_center()` and `get_top()` to get points of existing `Mobject`s.

class DemoObjects(Scene):
    def construct(self):
        rect = Rectangle(width=2.0, height=4.0)
        grid = Rectangle(width=4.0, height=2.0,
                grid_xstep=1.0, grid_ystep=1.0)
        grid.next_to(rect, RIGHT)
        arrow = Arrow(start=grid.get_center(),
                end=rect.get_top(), buff=0, color=YELLOW)
        group = VGroup()
        group.add(rect, grid, arrow)
        self.play(Create(group), run_time=4.0)
        self.wait()

# Show a representation of a linked list with arrows
## NOTES: Uses `next_to()` with `buff` to space out
## Shows how to move a group.

class LinkedList1(Scene):
    def construct(self):
        node1 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0)
        node2 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0)
        node2.next_to(node1, RIGHT, buff=1.0)
        arrow12 = Arrow(start=node1.get_center() + RIGHT * 0.5, end=node2.get_left(), buff=0)
        node3 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0)
        node3.next_to(node2, RIGHT, buff=1.0)
        arrow23 = Arrow(start=node2.get_center() + RIGHT * 0.5, end=node3.get_left(), buff=0)
        group = VGroup(node1, node2, node3, arrow12, arrow23)
        group.shift(LEFT * 2.0)
        self.play(Create(group))
        self.wait()

# Show a linked list animation for removing middle element

class LinkedListRemove(Scene):
    def construct(self):
        node1 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0)
        node2 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0)
        node2.next_to(node1, RIGHT, buff=1.0)
        arrow12 = Arrow(start=node1.get_center() + RIGHT * 0.5, end=node2.get_left(), buff=0)
        node3 = Rectangle(width=2.0, height=1.0, grid_xstep=1.0)
        node3.next_to(node2, RIGHT, buff=1.0)
        arrow23 = Arrow(start=node2.get_center() + RIGHT * 0.5, end=node3.get_left(), buff=0)
        group = VGroup(node1, node2, node3, arrow12, arrow23)
        group.shift(LEFT * 2.0)
        self.play(Create(group))
        self.wait()
        self.play(FadeOut(node2, arrow23))
        self.wait()
        newarrow12 = Arrow(start=node1.get_center() + RIGHT * 0.5, end=node3.get_left(), buff=0)
        self.play(Transform(arrow12, newarrow12))
        self.wait()

# Show a linked list animation for removing middle element
## This time with more details.

class LinkedListRemove2(Scene):
    def construct(self):

        node1 = Rectangle(width=2.0, height=1.0,
                          grid_xstep=1.0)
        node2 = Rectangle(width=2.0, height=1.0,
                          grid_xstep=1.0)
        node2.next_to(node1, RIGHT, buff=1.0)
        node3 = Rectangle(width=2.0, height=1.0,
                          grid_xstep=1.0)
        node3.next_to(node2, RIGHT, buff=1.0)

        arrow12 = Arrow(start=node1.get_center() + RIGHT / 2,
                        end=node2.get_left(), buff=0, color=YELLOW)
        arrow23 = Arrow(start=node2.get_center() + RIGHT / 2,
                        end=node3.get_left(), buff=0, color=YELLOW)
        node1_text = Text('a', color=BLUE).next_to(node1, UP)
        node2_text = Text('b', color=BLUE).next_to(node2, UP)
        node3_text = Text('c', color=BLUE).next_to(node3, UP)
        node3_x = Dot(radius=0.3, color=YELLOW).shift(
            node3.get_center() + RIGHT / 2)

        group = VGroup(node1, node1_text, node2, node2_text,
                       node3, node3_text, node3_x, arrow12, arrow23)
        group.shift(LEFT * 2.0)
        self.play(Create(group))
        self.wait()
        self.play(FadeOut(node2, node2_text, arrow23))
        self.wait()
        arrow13 = Arrow(start=node1.get_center() + RIGHT / 2,
                        end=node3.get_left(), buff=0, color=YELLOW)
        self.play(Transform(arrow12, arrow13))
        self.wait()

# Let's make a binary tree with functions

## Returns group of binary tree
def bt(value, left=None, right=None):
    root = VGroup(Circle(0.75), Text(f'{value}'))
    l = left if left is not None else Circle(0.25, stroke_opacity=0)
    r = right if right is not None else Circle(0.25, stroke_opacity=0)
    # Group left and right next to each other, top aligned
    r.next_to(l, RIGHT)
    r.align_to(l, UP)
    children = VGroup(l, r)
    children.next_to(root, DOWN, buff=0.5)
    tree = VGroup(root, children)
    if left is not None:
        tree.add(Arrow(start=root.get_bottom(), end=l.get_top(), buff=0, stroke_width=3.0))
    if right is not None:
        tree.add(Arrow(start=root.get_bottom(), end=r.get_top(), buff=0, stroke_width=3.0))
    return tree

class BinaryTree1(Scene):
    def construct(self):
        tree = bt(7, bt(5), bt(10, bt(8), bt(11)))
        tree.center()
        self.play(Create(tree))
        self.wait()

# This one didn't work
#
# # Let's make trees that can be animated
# ## Need to keep same `Mobject` as nodes in different trees

# def node(value):
#     node = Circle(0.75)
#     label = Text(f'{value}')
#     return VGroup(node, label)

# def bt(root, left=None, right=None):
#     l = left if left is not None else Circle(0.75, stroke_opacity=0)
#     r = right if right is not None else Circle(0.75, stroke_opacity=0)
#     # Group left and right next to each other, top aligned
#     r.next_to(l, RIGHT)
#     r.align_to(l, UP)
#     children = VGroup(l, r)
#     children.next_to(root, DOWN, buff=0.5)
#     tree = VGroup(root, children)
#     if left is not None:
#         tree.add(Arrow(start=root.get_bottom(), end=l.get_top(), buff=0, stroke_width=3.0))
#     if right is not None:
#         tree.add(Arrow(start=root.get_bottom(), end=r.get_top(), buff=0, stroke_width=3.0))
#     return tree

# class BinaryTree2(Scene):
#     def construct(self):
#         nodes = [node(5), node(7), node(8), node(10), node(11)]
#         tree1 = bt(nodes[1], nodes[0], bt(nodes[3], nodes[2], nodes[4]))
#         tree1.center()
#         tree2 = bt(nodes[3], bt(nodes[1], nodes[0], nodes[2]), nodes[4])
#         tree2.center()
#         self.play(Create(tree1))
#         self.play(Transform(tree1, tree2), run_time=4)
#         self.wait()

class BinaryTree2(Scene):
    def construct(self):
        tree1 = bt(7, bt(5), bt(10, bt(8), bt(11)))
        tree1.center()
        tree2 = bt(10, bt(7, bt(5), bt(8)), bt(11))
        tree2.center()
        self.play(Create(tree1))
        self.wait()
        self.play(FadeTransform(tree1, tree2))
        self.wait()

# Let's show an insert path
class BinaryTree3(Scene):
    def construct(self):
        tree1 = bt(10, bt(7, bt(5), bt(8)), bt(11))
        tree1.center().scale(0.7)
        self.play(Create(tree1))
        node = VGroup(Circle(0.75, color=BLACK,
                             stroke_color=BLUE,
                             fill_opacity=1),
                      Text('6')).scale(0.7)
        node.next_to(tree1[0], UP) # above 10 circle
        self.play(Create(node))
        self.play(node.animate.next_to(tree1[1][0], UP))
        self.wait()
        self.play(node.animate.next_to(tree1[1][0][1][0], UP))
        self.wait()
        # Slide it near where it needs to be in new tree
        self.play(node.animate.shift(2.5 * DOWN + 0.5 * RIGHT))
        self.wait()
        tree2 = bt(10, bt(7, bt(5, None, bt(6)), bt(8)), bt(11))
        tree2.center().scale(0.7)
        self.remove(node)
        self.play(Transform(tree1, tree2))
        self.wait()

### GRU

class Activation(VGroup):
    def __init__(self, height=1.0, tanh=False):
        s = Rectangle(fill_opacity=1.0, width=2.0,
                      height=2.0 * height, fill_color=BLACK)
        p1 = np.array([-1, -0.8 * height, 0])
        p2 = np.array([0, -0.8 * height, 0])
        p3 = np.array([0, 0.8 * height, 0])
        p4 = np.array([1, 0.8 * height, 0])
        b = CubicBezier(p1, p2, p3, p4, color=BLUE)
        a = Line(LEFT + DOWN * 0.8 * height,
                 RIGHT + DOWN * 0.8 * height,
                 stroke_width=2.0) if not tanh else Line(
                     LEFT, RIGHT, stroke_width=2.0)
        self.inputs = [s.get_top()]
        self.outputs = [s.get_bottom()]
        super().__init__(s, a, b)

class Activation1(Scene):
    def construct(self):
        act1 = Activation()
        act2 = Activation(tanh=True).next_to(act1, DOWN)
        network = VGroup(act1, act2).center()
        self.play(Create(network))
        self.wait()

class LinearActivation(VGroup):
    def __init__(self, inputs=1, txt=r"$d_{in}, d_{out}$",
                 activation_height=1.0, tanh=False):
        ab = Activation(height=activation_height, tanh=tanh) \
                .set_z_index(1)
        linear = VGroup(
            Rectangle(width=2.0, height=0.5, fill_opacity=1, 
                      fill_color=BLACK).set_z_index(1),
            Tex(txt).scale(0.8),
        ).set_z_index(1).next_to(ab, UP)
        c = Line(linear[0].get_bottom(), ab.get_top())
        cxs = VGroup([Line(ORIGIN, UP * 0.2) for i in
            range(inputs)]) \
            .arrange(buff=2.8 / inputs) \
            .shift(linear[0].get_top() + UP * 0.1)
        cy = Line(ab.get_bottom(), ab.get_bottom() + DOWN * 0.2)
        self.cy = cy 
        self.cxs = cxs
        super().__init__(linear, ab, cxs, c, cy)
    def get_inputs(self):
        return [c.get_center() for c in self.cxs]
    def get_outputs(self):
        return [self.cy.get_center()]

class LinearScene(Scene):
    def construct(self):
        b = LinearActivation()
        lbl_x = Tex("$x$").next_to(b, UP)
        lbl_y = Tex("$y$").next_to(b, DOWN)
        v = VGroup(lbl_x, b, lbl_y)
        self.play(Create(v))
        self.wait(1)

class MLP(Scene):
    def construct(self):
        b = LinearActivation(txt=r'784, 200',
                             activation_height=0.5)
        lbl_x = Tex("$x$").next_to(b, UP)
        c = LinearActivation(txt=r'200, 200', 
                             activation_height=0.5) \
            .next_to(b, DOWN, buff=-0.05)
        d = LinearActivation(txt=r'200, 10',
                             activation_height=0.5) \
            .next_to(c, DOWN, buff=-0.05)
        lbl_y = Tex("$y$").next_to(d, DOWN)
        v = VGroup(lbl_x, b, c, d, lbl_y) \
            .center().scale(0.8)
        self.play(Create(v), run_time=4)
        self.wait(1)
