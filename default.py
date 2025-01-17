import xbmc
import xbmcgui
import os

class TextEditor:
    def __init__(self):
        self.file_path = ""
        self.text = ""

    def open_file(self):
        dialog = xbmcgui.Dialog()
        self.file_path = dialog.browse(0, "Select a text file", "files", ".txt", False, False)
        if self.file_path:
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    self.text = file.read()
            except Exception as e:
                xbmcgui.Dialog().ok("Error", f"Failed to open file: {str(e)}")

    def save_file(self):
        if not self.file_path:
            dialog = xbmcgui.Dialog()
            self.file_path = dialog.browse(0, "Select a location to save the text file", "files", ".txt", False, False)
        if self.file_path:
            try:
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text)
            except Exception as e:
                xbmcgui.Dialog().ok("Error", f"Failed to save file: {str(e)}")

    def edit_text(self):
        dialog = xbmcgui.Dialog()
        self.text = dialog.textviewer("Text Editor", self.text)

    def show(self):
        dialog = xbmcgui.Dialog()
        while True:
            options = ["Open File", "Edit Text", "Save File", "Exit"]
            choice = dialog.select("TextEdio", options)
            if choice == -1 or choice == 3:  # Exit
                break
            elif choice == 0:  # Open File
                self.open_file()
            elif choice == 1:  # Edit Text
                self.edit_text()
            elif choice == 2:  # Save File
                self.save_file()

if __name__ == "__main__":
    editor = TextEditor()
    editor.show()
