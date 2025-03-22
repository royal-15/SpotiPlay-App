import os
import sys
import appdirs

class DataWriter:
    def __init__(self, filename="data.txt"):
        # If running as exe, use user's app data directory
        if getattr(sys, 'frozen', False):
            # Running as bundled exe
            app_name = "SpotiPlay"
            app_author = "SpotiPlay"
            data_dir = appdirs.user_data_dir(app_name, app_author)
            os.makedirs(data_dir, exist_ok=True)
            self.filename = os.path.join(data_dir, filename)
            # Create the file if it doesn't exist
            if not os.path.exists(self.filename):
                with open(self.filename, "w", encoding='utf-8') as f:
                    f.write("")  # Create empty file
            print(f"Data file location: {self.filename}")
        else:
            # Running as script
            self.filename = filename
            # Create the file if it doesn't exist
            if not os.path.exists(self.filename):
                with open(self.filename, "w", encoding='utf-8') as f:
                    f.write("")  # Create empty file
            print(f"Data file location: {self.filename}")

    def write_url(self, url):
        """Writes the URL to the first line, keeping the path unchanged."""
        try:
            path = self.read_path()  # Read the existing path
            with open(self.filename, "w", encoding='utf-8') as file:
                file.write(url + "\n")  # Write the new URL
                if path:
                    file.write(path + "\n")  # Preserve the path
        except Exception as e:
            print(f"Error writing URL: {e}")
            return False
        return True

    def write_path(self, path):
        """Writes the path to the second line, keeping the URL unchanged."""
        try:
            url = self.read_url()  # Read the existing URL
            with open(self.filename, "w", encoding='utf-8') as file:
                if url:
                    file.write(url + "\n")  # Preserve the URL
                file.write(path + "\n")  # Write the new path
        except Exception as e:
            print(f"Error writing path: {e}")
            return False
        return True

    def read_url(self):
        """Reads the first line (URL) from the file."""
        try:
            with open(self.filename, "r", encoding='utf-8') as file:
                return file.readline().strip()  # Read first line
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Error reading URL: {e}")
            return ""

    def read_path(self):
        """Reads the second line (Path) from the file."""
        try:
            with open(self.filename, "r", encoding='utf-8') as file:
                lines = file.readlines()
                return lines[1].strip() if len(lines) > 1 else ""
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Error reading path: {e}")
            return ""
