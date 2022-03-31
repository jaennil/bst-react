import Node from "./node";

class BinarySearchTree {
  constructor() {
    this.root = null;
    this.nodes = [];
    //his.printArray = [];
  }

  insert(value) {
    if (this.root) return this._insert(value, this.root);
    this.root = new Node(value);
    this.collision();
    this.nodes.push(this.root);
    return this.root;
  }

  _insert(value, node) {
    if (Number(value) < Number(node.value)) {
      if (node.left) return this._insert(value, node.left);
      node.left = new Node(value, undefined, undefined, node);
      node.left.x -= 100;
      this.collision(node.left);
      this.nodes.push(node.left);
      return node.left;
    } else {
      if (node.right) return this._insert(value, node.right);
      node.right = new Node(value, undefined, undefined, node);
      node.right.x += 100;
      this.collision(node.right);
      this.nodes.push(node.right);
      return node.right;
    }
  }
  printTreeInOrder() {
    this.printArray = [];
    if (this.root) {
      this._printTreeInOrder(this.root);
      return this.printArray;
    } else console.log("cant print tree is empty");
  }
  _printTreeInOrder(node) {
    if (node) {
      this._printTreeInOrder(node.left);
      this.printArray.push(node.value);
      this._printTreeInOrder(node.right);
    }
  }
  find(node) {
    let arr = this.printTreeInOrder();
    if (node.value in arr) {
      console.log("true");
    } else {
      console.log("false");
    }
  }
  collision(node) {
    for (let index = 0; index < this.nodes.length; index++) {
      if (node.x === this.nodes[index].x && node.y === this.nodes[index].y) {
        console.log("collision");
        if (Number(node.value) < Number(this.nodes[index].value)) {
          node.x -= 40;
          //node2.x+=10
        } else {
          //node2.x-=10
          node.x += 40;
        }
      }
    }
  }
}
export default BinarySearchTree;
