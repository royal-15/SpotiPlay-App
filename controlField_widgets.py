from customtkinter import *
from settings import *


class controlField(CTkFrame):
    def __init__(self, parent, downloadMethod, resetMethod):
        super().__init__(parent)

        greenBtn(parent=self, text="Download", method=downloadMethod).pack(side="right")


class greenBtn(CTkButton):
    def __init__(self, parent, text, method):
        super().__init__(
            parent,
            text=text,
            fg_color=GREEN_BTN_FG,
            text_color="white",
            font=BUTTON_FONT,
            width=125,
            height=33,
            hover_color=GREEN_BTN_FG_HOVER,
            command=method,
        )
