"""This is a basic "Hello world" using Kivy.

It uses the Builder to load a KVlang string, that describe a widget
tree, here containing only one element, the root, a Label displaying
"Hello world!"
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scatter import Scatter



# KVLang is a yaml-inspired declarative language to describe user
# interfaces you can find an introduction to its syntax here
# https://kivy.org/doc/stable/guide/lang.html

# for an even shorter introduction…
# Widgets are declared nested by indentation, and properties are
# similarly defined in the scope (indentation level) of the widget they
# apply to. It also allows defining canvas (graphical) instructions much
# in the same way as widgets.

# KVlang also allows declaring "rules" for widget classes, these rules
# will similarly declare a tree of widget children, properties and
# canvas instructions, that will be automatically applied to all
# instances of these classes, these rules are declared using the class
# name around pointy brackets, e.g: "<MyCustomLabel>:" would declare a
# rule applied to all instances of the MyCustomLabel class (which you
# could define as a subclass of kivy.uix.label.Label).

# The string can contain at most one "root" rule, which is a rule
# without <> around its name, this rule is treated differently, it
# directly instantiates a widget of the class, and adds the declared
# properties, graphical instructions and children widgets to it. This
# widget is returned by the Builder.load_string (or Builder.load_file)
# call, so it can be added to the widget tree, either as root, or to an
# existing parent widget of your choice. In the example below, "Label"
# is the "root rule".
class PydisLogo(Image):
    pass
    #source = StringProperty(None)
    # def __init__(self, **kwargs):
     #    super(PydisLogo, self).__init__(**kwargs)
      #   print(self.parent)

    #     self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
    #     self._keyboard.bind(on_key_down=self._on_keyboard_down)
    #
    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None
    #
    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode[1] == 'left':
    #         print("Moving left")
    #         self.x -= 100
    #     elif keycode[1] == 'right':
    #         self.x += 10
    #     elif keycode[1] == 'up':
    #         self.center_y += 10
    #     elif keycode[1] == 'down':
    #         self.center_y -= 10


class ImageFrame(FloatLayout):
    img = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ImageFrame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(self.img.pos_hint)
        if keycode[1] == 'left':
            print("Moving left")
            self.img.x -= 10
        elif keycode[1] == 'right':
            self.img.x += 10
        elif keycode[1] == 'up':
            self.img.y += 10
        elif keycode[1] == 'down':
            self.img.y -= 10
        elif keycode[1] == 'w':
            center = (self.img.center_x,self.img.center_y)
            self.img.width *= 1.1
            self.img.height*=1.1
            self.img.center_x = center[0]
            self.img.center_y = center[1]
        elif keycode[1] == 's':
            center = (self.img.center_x, self.img.center_y)
            self.img.height*=0.9
            self.img.width *= 0.9
            self.img.center_x = center[0]
            self.img.center_y = center[1]
        if self.img.top > self.top:
            self.img.top = self.top
            print("COLLIDE!!!!!")
        if self.img.y < self.y:
            self.img.y = self.y
        if self.img.right > self.right:
            self.img.right = self.right
            print("COLLIDE!!!!!")
        if self.img.x < self.x:
            self.img.x = self.x
class ImageMover(App):
    """The application class manages the lifecycle of your program, it
    has events like on_start, on_stop, etc.

    see https://kivy.org/doc/stable/api-kivy.app.html for more information.
    """

    def build(self):
        """whatever is returned by `build` will be the root of the
        widget tree of the application, and be accessible through the
        `root` attribute of the Application object.

        You can also delete this method and rely on the default behavior
        of loading a kv file in the same directory, named like the
        application class, but lower case. here, it would be
        application.kv.
        """
        game = ImageFrame()
        return game
        #return Builder.load_string(KV_RULES)


if __name__ == "__main__":
    # calling run method of the application will build the widget tree,
    # and start the event loop.
    ImageMover().run()
