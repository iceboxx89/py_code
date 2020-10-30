#!/usr/bin/env python

# Implementation of DFS & BFS

__author__ = "Jagadish Kumar P"
__email__ = "jagadish123@gmail.com"

import os
from Queue import Queue


class Node(object):
    """
    A very simple node oject to capture information gathered while traversals, 
    used for encapsulating parent - child relationsip
    """
    def __init__(self, name, parent=None):
        """
        Object init function
        Args:
        name    -- name of the node
        parent  -- parent of this Node
        """
        self.name = name
        self.parent = parent
        self.children = []
        if self.parent is not None:
            self.parent.children.append(self)

    def searchNode(self, value, child=None):
        """
        Searches all children for a node matching the value
        returns:
        Node
        """
        if not value: assert(Exception("Cannot search with a empty `value`"))
        child = child if child is not None else self
        if child.name == value:
            return child
        else:
            children = child.children
            if len(children):
                for child in children:
                    y = child.searchNode(value, child)
                    if y: return y
        return None

    def renderTree(self, depth=0, child=None, ascii=False):
        child = child if child is not None else self
        if ascii:
            print "|{}--{}".format(u"\t|" * depth, os.path.basename(child.name))
        else:
            print u"\u2502{}\u2500\u2500{}".format(u"\t\u2502" * depth, os.path.basename(child.name))
        children = child.children
        if len(children):
            for child in children:
                child.renderTree(depth+1, child)



    def __repr__(self):
        """
        Internal representation
        """
        classname = self.__class__.__name__
        return "%s (%s)" % (classname, self.name)


class Traverse(object):
    """
    Object encapsulating Depth first, Breadth first traversal algorithm
    """
    def __init__(self, rootDir, use="dfs", ascii_only=False):
        """
        Object init function
        Args:
        rootDir -- the root directory from which to start
        """
        self.rootDir = rootDir
        if rootDir.endswith("/"): raise(Exception("rootDir cannot end with /"))
        self.rootNode = Node(rootDir)
        if use == "bfs":
            self.queue = Queue()    # a simple queue from python std_lib
            self.queue.put(self.rootDir)
            self.bfs()
        else:
            self.dfs(rootDir)
        print "\nTraversal Using: %s" % use
        self.rootNode.renderTree(ascii=ascii_only)

    def dfs(self, dir_name=None):
        """
        Depth first traversal
        Args:
        dir_name -- the directory name
        """
        currentDir = dir_name if dir_name is not None else self.rootDir
        for item in os.listdir(currentDir):
            full_path = os.path.join(currentDir, item)
            if not item.startswith('.'):
                n = self.rootNode.searchNode(os.path.dirname(full_path))
                if n:
                    Node(full_path, n)
            if os.path.isdir(full_path):
                self.dfs(full_path)

    def bfs(self):
        """
        Breadth first traversal
        """
        while not self.queue.empty():
            # get a item from queue to process
            currentItem = self.queue.get()
            parent = os.path.dirname(currentItem)
            node = self.rootNode.searchNode(parent)
            if node:
                Node(currentItem, node)
            for _dir in os.listdir(currentItem):
                full_path = os.path.join(currentItem, _dir)
                if os.path.isdir(full_path):
                    self.queue.put(full_path)
                else:
                    if not _dir.startswith('.'):
                        Node(_dir, node)


if __name__ == '__main__':
    rootDir = os.path.abspath("./folders")
    Traverse(rootDir, use="dfs")
    # Traverse(rootDir, use="bfs")