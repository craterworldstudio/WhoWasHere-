import json
from classes import *


class FileSystem:

    def __init__(self):

        with open("basefs.json", 'r') as f:
            self.fs_json = json.load(f)

        self.tree = Folder("root")
        self.curr_fol = self.tree #self.fs["root"]

    def generate_fs(self):

        def crawl(fol_obj, tree):
            for key, item in tree.items():
                #print(item)
                if ('.' in key and key[0] != '.'):
                    name, ext = key.rsplit('.', 1)
                    f = File(name, ext)
                    f.set_path(fol_obj.path)
                    fol_obj.add(f)
    
                elif ('.' in key and key[0] == '.'):
                    key_name = key[1:]
            
                    if ('.' in key_name):
                        name, ext = key_name.rsplit('.', 1)
                        f = File(name, ext)
                        f.set_path(fol_obj.path)
                        fol_obj.add(f, True)
                    else:
                        fol = Folder(key)
                        fol.parent = fol_obj
                        fol.path = fol_obj.path + key if fol_obj.path == "/" else fol_obj.path + "/" + key
                        fol_obj.add(fol, True)
                        #self.curr_path += f"/{key}"
                        

                        self.curr_fol = fol
                        
                        crawl(fol, item)
    
                elif ('.' not in key):
                    fol = Folder(key)
                    #self.curr_path += f"/{key}"
                    fol.path = fol_obj.path + key if fol_obj.path == "/" else fol_obj.path + "/" + key
                    fol.parent = fol_obj
                    fol_obj.add(fol)

                    self.curr_fol = fol
                    
                    crawl(fol, item)


            #paths = self.curr_path.split("/")
            #self.curr_path = "".join(paths[:-1])
            
                


        root_part = self.fs_json["root"]
        crawl(self.tree, root_part)

        self.curr_fol = self.tree
                    
    def pwd(self):
        return self.curr_fol.path

    def get_item(self, name):

        for item in self.curr_fol.all:
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
