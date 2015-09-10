<?php
	
class TreeNode {
  	public $value;
	public $left;
	public $right;
	
	public function __construct($value) {
		$this->value = $value;
		$this->left = null;
		$this->right = null;
	}
	
	public function inOrder() {
		if($this->left) {
		  yield from $this->left->inOrder();
		}
		yield $this->value;
		if($this->right) {
		  yield from $this->right->inOrder();
		}
  	}

	public function preOrder() {
		yield $this->value;
		if($this->left) {
			yield from $this->left->preOrder();
		}
		if($this->right) {
			yield from $this->right->preOrder();
		}
	}
}


class Tree {
	public $root;
	
	public function __construct($items = null) {
    	$this->root = null;

		if(!$items) return null;

		foreach($items as $i) {
			$this->insert($i);
		}
	}
  
	public function insert($value) {
		if(!$this->root) {
			$this->root = new TreeNode($value);
			return null;
		}

		$step = $this->root;
		$lastStep = $this->root;
		while($step) {
			if($step->value < $value) {
				$step = $step->right;
			} else if($step->value > $value) {
				$step = $step->left;
			} else {
				return null;
			}

			$lastStep = $step ? $step : $lastStep;
		}
		if($lastStep->value < $value) {
			$lastStep->right = new TreeNode($value);
		} else {
			$lastStep->left = new TreeNode($value);
		}
	}
  
	public function inOrder() {
		yield from $this->root->inOrder();
	}

	public function preOrder() {
		yield from $this->root->preOrder();
	}
}

$tree = new Tree([5, 2, 4, 3, 10, 7, 6, 8]);

foreach($tree->preOrder() as $i) {
  echo 'value: ' . $i . "<br/>\n";
}

