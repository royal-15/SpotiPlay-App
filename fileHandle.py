class DataWriter:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def write_url(self, url):
        """Writes the URL to the first line, keeping the path unchanged."""
        path = self.read_path()  # Read the existing path
        with open(self.filename, "w") as file:
            file.write(url + "\n")  # Write the new URL
            if path:
                file.write(path + "\n")  # Preserve the path

    def write_path(self, path):
        """Writes the path to the second line, keeping the URL unchanged."""
        url = self.read_url()  # Read the existing URL
        with open(self.filename, "w") as file:
            if url:
                file.write(url + "\n")  # Preserve the URL
            file.write(path + "\n")  # Write the new path

    def read_url(self):
        """Reads the first line (URL) from the file."""
        try:
            with open(self.filename, "r") as file:
                return file.readline().strip()  # Read first line
        except FileNotFoundError:
            return ""

    def read_path(self):
        """Reads the second line (Path) from the file."""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                return lines[1].strip() if len(lines) > 1 else ""
        except FileNotFoundError:
            return ""
