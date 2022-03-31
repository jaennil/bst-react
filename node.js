class Node {
  constructor(value, left, right, parent) {
    this.value = value;
    this.left = left;
    this.right = right;
    this.parent = parent;
    this.depth = 0;
    this.calculateDepth(this);

    if (this.parent) {
      this.x = this.parent.x;
      this.y = this.parent.y + 100;
    } else {
      this.x = 800;
      this.y = 0;
    }
  }
  calculateDepth(node) {
    if (node.parent) {
      this.depth += 1;
      this.calculateDepth(node.parent);
    }
  }
}
export default Node;
