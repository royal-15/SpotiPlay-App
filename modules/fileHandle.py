import os
import sys
import appdirs


class DataWriter:
    def __init__(self, filename="data.txt", showMessage=None):
        self.showMessage = showMessage
        # If running as exe, use user's app data directory
        try:
            if getattr(sys, "frozen", False):
                # Running as bundled exe
                app_name = "SpotiPlay"
                app_author = "SpotiPlay"
                data_dir = appdirs.user_data_dir(app_name, app_author)
                os.makedirs(data_dir, exist_ok=True)
                self.filename = os.path.join(data_dir, filename)
                # Create the file if it doesn't exist
                if not os.path.exists(self.filename):
                    with open(self.filename, "w", encoding="utf-8") as f:
                        f.write("")  # Create empty file
                print(f"Data file location: {self.filename}")
            else:
                # Running as script
                self.filename = filename
                # Create the file if it doesn't exist
                if not os.path.exists(self.filename):
                    with open(self.filename, "w", encoding="utf-8") as f:
                        f.write("")  # Create empty file
                print(f"Data file location: {self.filename}")
        except Exception as e:
            error_message = f"Error initializing data file: {str(e)}"
            if self.showMessage:
                self.showMessage("Data File Error", error_message, "e")

    def write_url(self, url):
        """Writes the URL to the first line, keeping the path unchanged."""
        try:
            path = self.read_path()  # Read the existing path
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(url + "\n")  # Write the new URL
                if path:
                    file.write(path + "\n")  # Preserve the path
        except Exception as e:
            warning_message = f"Error writing URL: {str(e)}"
            if self.showMessage:
                self.showMessage("URL Save Error", warning_message, "w")
            return False
        return True

    def write_path(self, path):
        """Writes the path to the second line, keeping the URL unchanged."""
        try:
            url = self.read_url()  # Read the existing URL
            with open(self.filename, "w", encoding="utf-8") as file:
                if url:
                    file.write(url + "\n")  # Preserve the URL
                file.write(path + "\n")  # Write the new path
        except Exception as e:
            warning_message = f"Error writing path: {str(e)}"
            if self.showMessage:
                self.showMessage("Path Save Error", warning_message, "w")
            return False
        return True

    def read_url(self):
        """Reads the first line (URL) from the file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return file.readline().strip()  # Read first line
        except FileNotFoundError:
            return ""
        except Exception as e:
            warning_message = f"Error reading URL: {str(e)}"
            if self.showMessage:
                self.showMessage("URL Read Error", warning_message, "w")
            return ""

    def read_path(self):
        """Reads the second line (Path) from the file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                return lines[1].strip() if len(lines) > 1 else ""
        except FileNotFoundError:
            return ""
        except Exception as e:
            warning_message = f"Error reading path: {str(e)}"
            if self.showMessage:
                self.showMessage("Path Read Error", warning_message, "w")
            return ""
