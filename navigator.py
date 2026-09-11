import json
from classes import *
from filecontent import FILE_CONTENTS
import random
from infection import *

class FileSystem:

    def __init__(self):

        with open("basefs.json", 'r') as f:
            self.fs_json = json.load(f)

        self.tree = Folder("root")
        self.curr_fol = self.tree #self.fs["root"]
        self.infec = Infections()

        self.ques_sets = []

    def generate_fs(self):

        def crawl(fol_obj, tree):
            for key, item in tree.items():
                #print(item)
                if ('.' in key and key[0] != '.'):
                    name, ext = key.rsplit('.', 1)

                    if isinstance(item, dict):
                        fol = Folder(key)
                        fol.parent = fol_obj
                        fol.path = fol_obj.path + key if fol_obj.path == "/" else fol_obj.path + "/" + key
                        fol_obj.add(fol)

                        self.curr_fol = fol
                        crawl(fol, item)

                    else:
                        f = File(name, ext)
                        f.set_path(fol_obj.path)
                        cont = FILE_CONTENTS.get(key, "")
                        #print(cont, key)
                        f.contents = cont[random.randrange(0, 3)]
                        fol_obj.add(f)
    
                elif ('.' in key and key[0] == '.'):
                    key_name = key[1:]
            
                    if ('.' in key_name):
                        name, ext = key_name.rsplit('.', 1)

                        if isinstance(item, dict):
                            fol = Folder(key)
                            fol.parent = fol_obj
                            fol.path = fol_obj.path + key if fol_obj.path == "/" else fol_obj.path + "/" + key
                            fol_obj.add(fol)

                            self.curr_fol = fol
                            self.crawl(fol, item)

                        else:
                            f = File(name, ext)
                            f.set_path(fol_obj.path)
                            f.contents = FILE_CONTENTS.get(key, "")[random.randrange(0,3)]
                            fol_obj.add(f, True)
                    else:
                        if isinstance(item, list):
                            f = File(key)
                            f.set_path(fol_obj.path)
                            f.contents = FILE_CONTENTS.get(key, "")[random.randrange(0,3)]
                            fol_obj.add(f, True)
                            return
                        
                        fol = Folder(key)
                        fol.parent = fol_obj
                        fol.path = fol_obj.path + key if fol_obj.path == "/" else fol_obj.path + "/" + key
                        fol_obj.add(fol, True)
                        #self.curr_path += f"/{key}"
                        

                        self.curr_fol = fol
                        #print(key, item)
                        crawl(fol, item)
    
                elif ('.' not in key):

                
                    if isinstance(item, list):
                        
                        f = File(name=key)
                        f.set_path(fol_obj.path)
                        cont = FILE_CONTENTS.get(key, "")
                        #print(cont, key)
                        f.contents = cont[random.randint(0,2)]
                        fol_obj.add(f, True)

                    else:
                        fol = Folder(key)
                        #self.curr_path += f"/{key}"
                        fol.path = fol_obj.path + key if fol_obj.path == "/" else fol_obj.path + "/" + key
                        fol.parent = fol_obj
                        fol_obj.add(fol)

                        self.curr_fol = fol
                        crawl(fol, item)

            
                


        root_part = self.fs_json["root"]
        crawl(self.tree, root_part)

        self.curr_fol = self.tree
                    
    def pwd(self):
        return self.curr_fol.path

    def get_item(self, name):

        for item in self.curr_fol.all:
            if isinstance(item, File):
                prefix = "." if item.hidden and not item.name.startswith(".") else ""
                iname = prefix + item.name + (f".{item.ext}" if item.ext else "")
                #print(name, iname, item.ext)
                if iname == name: return item
            else:
                if item.name == name:
                    return item

        return None

    def jmp_into(self, folder):

        fol = self.get_item(folder)
        #print(isinstance(fol, Folder), fol is not None)
        if (fol is not None) and isinstance(fol, Folder):
            self.curr_fol = fol
        else:
            print(f"{folder} is a file or doesn't exist")

    def jmp_out(self):

        if self.curr_fol.parent:
            self.curr_fol = self.curr_fol.parent

    def path_to_tree(self, path):

        parts = [part for part in path.split("/") if part]
        current = self.tree

        for part in parts:
            found = None
            for item in current.all:

                if isinstance(item, File):
                    prefix = "." if item.hidden and not item.name.startswith(".") else ""
                    iname = prefix + item.name + (f".{item.ext}" if item.ext else "")

                    if iname == part:
                        found = item
                        break
                else:
                    if item.name == part:
                        found = item
                        break
            if found is None:
                return None
            if isinstance(found, File):
                # File is only valid if it is the final component
                if part != parts[-1]:
                    return None
                return found
            current = found
        return current

            

    def infect(self):
        for traceID in self.infec.applied_traces:
            trace = self.infec.get_infection(traceID)
            self.ques_sets.append(trace.get("questions"))

            affected_paths = trace.get("affected", [])

            for filep, contents in affected_paths.items():
                file = self.path_to_tree(filep)

                #print(filep, contents)
                file.contents = contents[random.randrange(len(contents))]

        persistence = self.infec.get_infection(self.infec.persistance)

        self.ques_sets.append(persistence.get("questions"))
        affected_paths = persistence.get("affected", [])

        for filep, contents in affected_paths.items():
            file = self.path_to_tree(filep)
            
            file.contents = contents[random.randrange(len(contents))]
            
                #print(file.name, file.contents)
