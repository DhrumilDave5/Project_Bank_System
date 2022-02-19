import pygame as pg


class TextBox:

    def __init__(self, display_surface: pg.Surface,
                 x: int, y: int, width: int, height: int = 35,
                 colour: tuple[int, int, int] = (255, 255, 255),
                 border_colour: tuple[int, int, int] = (0, 0, 0),
                 text_colour: tuple[int, int, int] = (0, 0, 0),
                 text_font: str = "cambria", text_size: int = 27,
                 text_allowed: str = "str", border_thickness: int = 2):

        """Keep values of width & height parameters as even numbers"""
        self.DISPLAY_SURFACE = display_surface
        self.RECT = pg.Rect(x, y, width, height)
        self.COLOUR = colour
        self.BORDER_COLOUR = border_colour
        self.TEXT_COLOUR = text_colour
        self.FONT = pg.font.SysFont(text_font, text_size)
        # The font 'consolas' is preferred as it's font sizes matches with
        # the number of pixels
        self.TEXT_ALLOWED = text_allowed
        self.thickness = self.ORIGINAL_THICKNESS = border_thickness
        self.hover = self.typing = self.action = False
        self.text = ""
        self.display_cursor = self.FONT.render("|", True, self.TEXT_COLOUR)

    def mouse_input(self):

        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] in range(self.RECT.left, self.RECT.right) \
                and mouse_pos[1] in range(self.RECT.top, self.RECT.bottom):
            self.hover = True
        else:
            self.hover = False

        if self.hover and pg.mouse.get_pressed()[0]:
            self.typing = True

        if not self.hover and self.typing and pg.mouse.get_pressed()[0]:
            self.typing = False
            if self.text:
                self.action = True
            else:
                self.action = False

    def keyboard_input(self, event: pg.event.Event):

        if self.action:
            self.action = False

        if self.typing:
            key_string = pg.key.name(event.key).upper()
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pg.K_DELETE:
                self.text = ""
            elif event.key == pg.K_PERIOD and "." not in self.text \
                    and self.TEXT_ALLOWED == "float":
                self.text += key_string
            elif key_string.isalnum() and len(key_string) == 1:
                if self.TEXT_ALLOWED == "float" and key_string.isnumeric():
                    if len(self.text) >= 3:
                        if self.text[-3] != ".":
                            self.text += key_string
                    else:
                        self.text += key_string
                if self.TEXT_ALLOWED == "int" and key_string.isnumeric():
                    self.text += key_string
                elif self.TEXT_ALLOWED == "str" and key_string.isalpha():
                    self.text += key_string
            elif event.key == pg.K_RETURN and self.text:
                self.typing = False
                self.action = True

    def give_value(self):

        if self.TEXT_ALLOWED == "float":
            to_be_returned = float(self.text)
        elif self.TEXT_ALLOWED == "int":
            to_be_returned = int(self.text)
        else:
            to_be_returned = self.text
        return to_be_returned

    def display(self):

        if self.typing:
            self.thickness = self.ORIGINAL_THICKNESS * 3
        elif self.hover:
            if self.thickness < self.ORIGINAL_THICKNESS * 3:
                self.thickness += 0.4
        else:
            self.thickness = self.ORIGINAL_THICKNESS

        border_rect = pg.Rect(self.RECT.x, self.RECT.y,
                              self.RECT.width + int(2 * self.thickness),
                              self.RECT.height + int(2 * self.thickness))
        border_rect.center = self.RECT.center
        pg.draw.rect(self.DISPLAY_SURFACE, self.BORDER_COLOUR, border_rect)
        pg.draw.rect(self.DISPLAY_SURFACE, self.COLOUR, self.RECT)

        text_to_display \
            = self.FONT.render(self.text, True, self.TEXT_COLOUR)
        text_x = self.RECT.x + 10
        text_y = self.RECT.y + \
            ((self.RECT.height - text_to_display.get_height()) // 2)
        # The correction of + 4 is done by trial & error as the font
        # doesn't center itself properly
        self.DISPLAY_SURFACE.blit(text_to_display, (text_x, text_y))

        if self.typing:
            cursor_x = text_x + text_to_display.get_width() - 5
            self.DISPLAY_SURFACE.blit(self.display_cursor,
                                      (cursor_x, text_y))
