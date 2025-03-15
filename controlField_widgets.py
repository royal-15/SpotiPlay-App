from customtkinter import *
from settings import *


class controlField(CTkFrame):
    def __init__(self, parent, downloadMethod):
        super().__init__(parent)

        self.status = statusLabel(self)
        self.status.pack(side="left", padx=(15, 0))

        greenBtn(parent=self, text="Download", method=downloadMethod).pack(side="right")


class statusLabel(CTkLabel):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="@royal-15 Officials",
            font=BUTTON_FONT,
            text_color=STATUS_TEXT_COLOR,
        )


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
