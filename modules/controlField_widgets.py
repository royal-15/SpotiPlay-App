from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkButton
from .settings import *
from PIL import Image


class controlField(CTkFrame):
    def __init__(self, parent, retryMethod, downloadMethod):
        super().__init__(parent)

        self.status = statusLabel(self)
        self.status.pack(side="left", padx=(15, 0))

        self.downloadBtn = greenBtn(parent=self, text="Download", method=downloadMethod)
        self.downloadBtn.pack(side="right")

        img = Image.open(RETRY_ICON)
        img = img.convert("RGBA")
        ctk_img = CTkImage(light_image=img, dark_image=img, size=(25, 25))

        self.retry_label = CTkLabel(
            self,
            text="",
            image=ctk_img,
            cursor="hand2",
            compound="left",
        )
        self.retry_label.bind("<Button-1>", retryMethod)
        self.retry_label.place(x=444, y=1)


class statusLabel(CTkLabel):
    def __init__(self, parent):
        super().__init__(
            parent,
            text="@royal-15 Officials",
            font=BUTTON_FONT,
            text_color=STATUS_TEXT_COLOR,
        )


class greenBtn(CTkButton):
    def __init__(self, parent, text, method, image=None, witdh=125, height=33, cr=6):
        super().__init__(
            parent,
            text=text,
            fg_color=GREEN_BTN_FG,
            text_color="white",
            font=BUTTON_FONT,
            width=witdh,
            height=height,
            corner_radius=cr,
            image=image,
            hover_color=GREEN_BTN_FG_HOVER,
            command=method,
        )
