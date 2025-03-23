from customtkinter import *
from .settings import *
from PIL import Image
from tkinter import filedialog


class inputFields(CTkFrame):
    def __init__(self, parent, onCheckURL, onCheckPATH):
        super().__init__(parent, fg_color=WINDOW_FG, height=120)

        # layout
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1, minsize=60, uniform="b")
        self.rowconfigure(1, weight=1, minsize=60, uniform="b")

        # declare variables for checkboxes
        self.check_var_url = BooleanVar()
        self.check_var_path = BooleanVar()

        self.input1 = input1(self, var=self.check_var_url, onCheck=onCheckURL)
        self.input1.grid(row=0, column=0, sticky="ew")

        self.input2 = input2(self, var=self.check_var_path, onCheck=onCheckPATH)
        self.input2.grid(row=1, column=0)


class input1(CTkFrame):
    def __init__(self, parent, var, onCheck):
        super().__init__(parent, fg_color=WINDOW_FG, height=60)

        self.urlInput = CTkEntry(
            self,
            placeholder_text="Song or playlist URL",
            width=280,
            text_color=INPUTFIELD_TEXT_COLOR,
            font=INPUTFIELD_FONT,
        )
        self.urlInput.pack(side="left", padx=(15, 8))
        
        # Bind right-click event
        self.urlInput.bind("<Button-3>", self.onRightClick)

        self.checkUrlInput = CTkCheckBox(
            self,
            text="remember",
            fg_color=GREEN_BTN_FG_HOVER,
            hover_color=GREEN_BTN_FG,
            font=BUTTON_FONT,
            variable=var,
            command=onCheck,
        )
        self.checkUrlInput.pack(side="left")

    def getUrlInput(self):
        return self.urlInput

    def getCheckUrlInput(self):
        return self.checkUrlInput

    def onRightClick(self, event):
        """Handle right-click event to paste clipboard content"""
        try:
            from tkinter import TclError
            clipboard_content = self.clipboard_get()
            self.urlInput.delete(0, "end")  # Clear current content
            self.urlInput.insert(0, clipboard_content)
        except TclError:
            # If clipboard is empty or contains non-text data
            pass


class input2(CTkFrame):
    def __init__(self, parent, var, onCheck):
        self.parent = parent
        super().__init__(parent, fg_color=WINDOW_FG, height=60)

        self.pathInput = CTkEntry(
            self,
            placeholder_text="Download folder path",
            width=251,
            text_color=INPUTFIELD_TEXT_COLOR,
            font=INPUTFIELD_FONT,
        )
        self.pathInput.pack(side="left", padx=(15, 0))

        image = CTkImage(light_image=Image.open(THREE_DOT_PNG), size=(10, 18))
        self.folderPathInput = CTkButton(
            self,
            text="",
            image=image,
            text_color="white",
            fg_color=FOLDER_BUTTON_FG,
            hover_color=FOLDER_BUTTON_FG_HOVER,
            font=BUTTON_FONT,
            width=25,
            command=self.onFolderSelectClick,
        )
        self.folderPathInput.pack(side="left", padx=(4, 8))

        self.checkPathInput = CTkCheckBox(
            self,
            text="remember",
            fg_color=GREEN_BTN_FG_HOVER,
            hover_color=GREEN_BTN_FG,
            font=BUTTON_FONT,
            variable=var,
            command=onCheck,
        )
        self.checkPathInput.pack(side="left")

    def getPathInput(self):
        return self.pathInput

    def getFolderPathInput(self):
        return self.folderPathInput

    def getCheckPathInput(self):
        return self.checkPathInput

    def onFolderSelectClick(self):
        path = filedialog.askdirectory()
        self.pathInput.delete(0, "end")
        self.pathInput.insert(0, path)
