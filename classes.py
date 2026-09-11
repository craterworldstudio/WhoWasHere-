
import random

class File:

    def __init__(self, name: str = "file", ext: str = ""):

        self.name = name
        self.ext = ext
        self.hidden = self.name.startswith(".")
        self.path = "/"

        number = str(random.randrange(0, 10))
        self.owner = "manger"+number
        self.group = "admin"
        self.perms = "rw-rwxr--"

        self.contents = []

    def set_path(self, path):
        self.path = path

    def set_owner(self, name):
        self.owner = name

class Folder:

    def __init__(self, name: str = "folder", parent:Folder = None):

        self.name = name
        self.visible = set()
        self.hidden = set()
        self.path = "/"
        self.parent = parent

        number = str(random.randrange(0, 10))
        self.owner = "manger"+number
        self.group = "admin"
        self.perms = "rw-rwxr--"

        self.all = set()

        self._upd_content()

    def _upd_content(self):
        self.all.update(self.hidden)
        self.all.update(self.visible)

    def add(self, item, h=False):
        if h:
            self.hidden.add(item)
        else:
            self.visible.add(item)

        self._upd_content()

    def disp(self, h=False):
        if h:
            for item in self.all:
                hid = '.' if item.hidden else ""
                ext = f'.{item.ext}' if isinstance(item, File) else ""
                fol_slash = "/" if isinstance(item, Folder) else ""
                print(f"{item.perms}\t{item.owner}\t{item.group}\t {hid+item.name+ext+fol_slash}")
        else:
            for item in self.visible:
                ext = f'.{item.ext}' if isinstance(item, File) else ""
                fol_slash = "/" if isinstance(item, Folder) else ""
                print(f"{item.perms}\t{item.owner}\t{item.group}\t {item.name+ext+fol_slash}")

    def set_owner(self, name):
        self.owner = name

    def __repr__(self):
        lines = [f"{self.name}/"]
    
        def build_tree(folder, prefix=""):
            items = sorted(folder.all, key=lambda x: x.name)
    
            for i, item in enumerate(items):
                last = i == len(items) - 1
                branch = "└── " if last else "├── "
    
                if isinstance(item, Folder):
                    lines.append(f"{prefix}{branch}{item.name}/")
                    build_tree(
                        item,
                        prefix + ("    " if last else "│   ")
                    )
                else:
                    
                    lines.append(f"{prefix}{branch}{item.name}{f'.{item.ext}' if isinstance(item, File) else ""} at {item.path}")
    
        build_tree(self)
    
        return "\n" + "\n".join(lines)