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
    node = Circle(0.75)
    label = Text(f'{value}')
    # Group left and right next to each other, top aligned
    if right is not None and left is not None:
        right.next_to(left, RIGHT)
        right.align_to(left, UP)
    children = VGroup()
    if left is not None: children.add(left)
    if right is not None: children.add(right)
    children.next_to(node, DOWN, buff=0.5)
    tree = VGroup(node, label, children)
    if left is not None:
        tree.add(Arrow(start=node.get_bottom(), end=left.get_top(), buff=0, stroke_width=3.0))
    if right is not None:
        tree.add(Arrow(start=node.get_bottom(), end=right.get_top(), buff=0, stroke_width=3.0))
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
        tree1.center()
        self.play(Create(tree1))
        self.wait()
        node = VGroup(Circle(0.75, color=BLUE), Text('6'))
        node.next_to(tree1[0], UP) # above 10 circle
        self.play(Create(node))
        self.wait()
        self.play(node.animate.next_to(tree1[2][0][0], UP)) # above 7
        self.wait()
        self.play(node.animate.next_to(tree1[2][0][2][0], UP)) # above 5
        self.wait()
        # Slide it near where it needs to be in new tree
        self.play(node.animate.shift(3.5 * DOWN + RIGHT))
        self.wait()
        tree2 = bt(10, bt(7, bt(5, None, bt(6)), bt(8)), bt(11))
        tree2.center()
        self.remove(node)
        self.play(Transform(tree1, tree2))
        self.wait()
