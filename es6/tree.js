
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
  
  *inOrder() {
    if(this.left) {
      yield *this.left.inOrder()
    }
    yield this.value
    if(this.right) {
      yield *this.right.inOrder()
    }
  }

  *preOrder() {
    yield this.value
    if(this.left) {
      yield *this.left.preOrder()
    }
    if(this.right) {
      yield *this.right.preOrder()
    }
  }
}

class Tree {
  constructor(items) {
    this.root = null;

    if(!items) return ;
    
    for(let i of items) {
      this.insert(i);
    }
  }
  
  insert(value) {
    if(!this.root) {
		  this.root = new TreeNode(value);
		  return ;
	  }

  	var step = this.root;
  	var lastStep = this.root;
  	while(step) {
  		if(step.value < value) {
  			step = step.right;
  		} else if(step.value > value) {
  			step = step.left;
  		} else {
  			return ;
  		}
  
  		lastStep = step ? step : lastStep;
  	}
  	if(lastStep.value < value) {
  		lastStep.right = new TreeNode(value);
  	} else {
  		lastStep.left = new TreeNode(value);
  	}
  }
  
  *inOrder() {
    yield *this.root.inOrder()
  }

  *preOrder() {
    yield *this.root.preOrder()
  }

  [Symbol.iterator]() {
    return this.root.inOrder()
  }
}

var tree = new Tree([5, 2, 4, 3, 10, 7, 6, 8])

for(let i of tree.preOrder()) {
  console.log('value: ' + i);
}
console.log('-- in order: ')
for(let i of tree) {
  console.log('value: ' + i);
}
