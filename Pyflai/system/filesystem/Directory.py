class Directory:
    def __init__(self, path: str):
        self.path = path.replace("\\", "/")
        if not self.path.endswith("/"):
            self.path += "/"
