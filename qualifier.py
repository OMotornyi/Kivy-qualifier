"""This is a basic "Hello world" using Kivy.

It uses the Builder to load a KVlang string, that describe a widget
tree, here containing only one element, the root, a Label displaying
"Hello world!"
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.popup import Popup
from pathlib import Path


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
class PydisLogo(Scatter):
    # pass
    def on_transform_with_touch(self, touch):
        if self.top > self.parent.top:
            self.top = self.parent.top
            print("COLLIDE!!!!!")
        if self.y < self.parent.y:
            self.y = self.parent.y
        if self.right > self.parent.right:
            self.right = self.parent.right
            print("COLLIDE!!!!!")
        if self.x < self.parent.x:
            self.x = self.parent.x
    # source = StringProperty(None)
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


class Root(FloatLayout):
    img = ObjectProperty(None)
    scat = ObjectProperty(None)
    pic = ObjectProperty(None)
    loadfile = ObjectProperty(None)

    # source = "data/python_discord_logo.png"

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(self.pic)
        if keycode[1] == 'left':
            print("Moving left")
            self.scat.x -= 10
        elif keycode[1] == 'right':
            self.scat.x += 10
        elif keycode[1] == 'up':
            self.scat.y += 10
        elif keycode[1] == 'down':
            self.scat.y -= 10
        elif keycode[1] == 'w':
            center = (self.scat.center_x, self.scat.center_y)
            self.img.width *= 1.1
            self.img.height *= 1.1
            self.scat.center_x = center[0]
            self.scat.center_y = center[1]
        elif keycode[1] == 's':
            center = (self.scat.center_x, self.scat.center_y)
            self.img.height *= 0.9
            self.img.width *= 0.9
            self.scat.center_x = center[0]
            self.scat.center_y = center[1]
        if self.scat.top > self.top:
            self.scat.top = self.top
        if self.scat.y < self.y:
            self.scat.y = self.y
        if self.scat.right > self.right:
            self.scat.right = self.right
#            print("COLLIDE!!!!!")
        if self.scat.x < self.x:
            self.scat.x = self.x

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def dismiss_popup(self):
        self._popup.dismiss()

    def load(self, path, filename):
        print(f"Path: '{path}', Filename: '{filename}'")
        # self.source = filename
        self.img.source = filename[0]
        self.img.reload()
        self.dismiss_popup()


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    home = StringProperty(str(Path.home()))


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
        game = Root()
        return game
        # return Builder.load_string(KV_RULES)


if __name__ == "__main__":
    # calling run method of the application will build the widget tree,
    # and start the event loop.
    ImageMover().run()
