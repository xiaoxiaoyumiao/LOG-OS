import markdown
from lxml import etree
import os
import sys

f = open("../docs/SUMMARY.md")
data = f.read()
html = markdown.markdown(data)
root = etree.fromstring(html)

SOURCE_DIR = "../docs/"

class FileNode:
    def __init__(self, filename, summary_name=None, is_dir=True):
        self.filename = filename
        if summary_name:
            self.summary_name = summary_name
        else:
            self.summary_name = filename
        self.parent = None
        self.is_dir = is_dir
        self.children = []

    def key(self):
        return self.filename

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def add_child_by_path(self, key_list, key_ptr, **kwargs):
        if key_list[key_ptr] == "":
            return
        if key_ptr < len(key_list)-1:
            for child in self.children:
                if child.key() == key_list[key_ptr]:
                    child.add_child_by_path(key_list, key_ptr+1, **kwargs)
                    break
            else:
                print(key_list[key_ptr])
                node = FileNode(key_list[key_ptr], is_dir=True)
                self.add_child(node)
                node.add_child_by_path(key_list, key_ptr+1, **kwargs)
        else:
            print(key_list[key_ptr])
            node = FileNode(key_list[key_ptr], **kwargs)
            self.add_child(node)

    def _print(self, indent):
        print(" " * indent, self.filename, self.summary_name)
        for child in self.children:
            child._print(indent + 4)

    def summarize(self):
        summary_list = []
        for child in self.children:
            if child.is_dir:
                summary_list.append((child.summary_name, child.filename + "/"))
            else:
                summary_list.append((child.summary_name, child.filename))
        return summary_list        

    def pretty_print(self):
        self._print(0)

    def absolute_path(self):
        if self.parent == None:
            return self.filename
        return os.path.join(self.parent.absolute_path(), self.filename)

    def iterator(self):
        yield self
        for child in self.children:
            for ele in child.iterator():
                yield ele

file_root = FileNode("", is_dir=True)

def has_child(node):
    return len(node) > 1

def get_children(node):
    return node[1]

def parse_node(node):
    title = node[0].text
    path = node[0].attrib['href']
    is_file = path.endswith(".md") or path.endswith(".markdown") or path.endswith(".MD")
    file_root.add_child_by_path(path.split("/"), 0, is_dir=not is_file, summary_name=title)
    if has_child(node):
        children = get_children(node)
        for child in children:
            parse_node(child)

def main_parse():
    for section in root:
        for child in section[0]:
            parse_node(child)

def format_summary(summary):
    formatted = [ "* [{0}]({1})\n".format(ele[0], ele[1]) for ele in summary ]
    return "".join(formatted)

def generate_summary():
    for node in file_root.iterator():
        # print(node.absolute_path(), node.is_dir)
        if node.is_dir:
            summary = node.summarize()
            if len(summary) != 0:
                # print("node: ", node.absolute_path())
                # print(format_summary(summary))
                folder_path = os.path.join(SOURCE_DIR, node.absolute_path())
                summary_path = os.path.join(folder_path, "SUMMARY.md")
                print(f"writing to {summary_path}.")
                with open(summary_path, "w") as f:
                    f.write(format_summary(summary))
            else:
                print("exception: node ", node.absolute_path())

if __name__ == "__main__":
    main_parse()
    # file_root.pretty_print()
    generate_summary()
    