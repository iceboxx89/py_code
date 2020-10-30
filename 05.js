/*
Breadth first and Depth first directory traversal
*/

var fs = require('fs');
var path = require('path');
var root_dir = path.resolve('./folders');

function Node(name, parent=null, children=[]) {
  /*
  Node which encapsulate parent - child relationsip
  if a parent is specified current node will automatically be
  added as a child

  args:
  name    -- name of the node
  parent  -- parent of this Node
  returns
    Node
  */
  this.name = name;
  this.parent = parent;
  this.children = children;
  if(parent !== null) {
    parent.children.push(this);
  }

  this.searchNode = function (value, currentNode=this) {
    /*
    Searches the tree for a node matching value
    returns:
      Node
    */
    var i, currentChild, result;
    if (value == currentNode.name) {
      return currentNode;
    } else {
      for (i = 0; i < currentNode.children.length; i++) {
        currentChild = currentNode.children[i];
        result = this.searchNode(value, currentChild);
        if (result != false) {
          return result;
        }
      }
      return false;
    }
  }

  this.renderTree = function () {
    /*
    Render the tree in a human readable format
    */
    function recurse(node) {
      rel_path = node.name.replace(root_dir, '');
      depth = rel_path.split(path.sep).length - 1
      console.log(
        "| ".repeat(depth) + "|--" + path.basename(node.name)
      )
      node.children.forEach(function(child_node){
        recurse(child_node);
      })
    }
    recurse(this)
  }
}

function Traverse(rootDir) {
  /*
  Depth First / Breadth First encapsulation
  Usage:
    t = new Traverse(rootDir)
    t.dfs()
  */
  this.rootDir = rootDir
  this.rootNode = new Node(rootDir)
  if(this.rootDir.endsWith('/')){throw("Root directory cannot endwith /")}

  this.dfs = function(dir) {
    /* Depth first directory traversal */
    (function recurse (that, currentDir) {
      _this = that;
      files = fs.readdirSync(currentDir);
      files.forEach(function(item){
        full_path = path.join(currentDir, item)
        n = _this.rootNode.searchNode(path.dirname(full_path))
        if(n) {
          new Node(full_path, n)
        }
        stat = fs.statSync(full_path);
        if(stat.isDirectory()){
          recurse(_this, full_path)
        }
      })
    })(this, this.rootDir);
    return true
  }

  this.bfs = function(){
    /* Breadth first directory traversal */
    var queue = []
    queue.push(root_dir)
    while(queue.length) {
      current = queue.shift()
      n = this.rootNode.searchNode(path.dirname(current));
      if(n){
        new Node(current, n)
      }
      files = fs.readdirSync(current)
      for (var i=0; i < files.length; i++){
        full_path = path.join(current, files[i])
        stat = fs.statSync(full_path)
        if(stat.isDirectory()){
          queue.push(full_path)
        } else {
          if(!files[i].startsWith(".")) {
            new Node(full_path, n)
          }
        }
      }
    }
  }
}


/* Depth First Traversal */
var t = new Traverse(root_dir)
t.dfs()
t.rootNode.renderTree()

/* Breadth First Traversal */
// var t = new Traverse(root_dir)
// t.bfs()
// t.rootNode.renderTree()