class node:
    def __init__(self,data,lat_lng,label,adj,is_marker) -> None:
        self.lat_lng = lat_lng
        self.adj = adj
        self.key = data
        self.label = label
        self.right = self.left = None
        self.height =1
        self.is_marker = is_marker

class all_point_tree:
    def __init__(self) -> None:
        self.root = None

    def check_bf(self,root):
        if not root:
            return 0
        return self.tree_height(root.left) - self.tree_height(root.right)

    def tree_height(self,root):
        if not root:
            return 0
        return root.height
    
    def rotateL(self,root):
        y = root.right
        t2 = y.left
        y.left = root
        root.right = t2
        root.height = max(self.tree_height(root.left),self.tree_height(root.right))+1
        y.height = max(self.tree_height(y.left),self.tree_height(y.right))+1

        return y


    def rotateR(self,root):
        y = root.left
        t2 = y.right
        y.right = root
        root.left = t2
        root.height = max(self.tree_height(root.left),self.tree_height(root.right))+1
        y.height = max(self.tree_height(y.left),self.tree_height(y.right))+1

        return y
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)    
    def insert_node(self,root,key,lat_lng,label,adj,is_marker):
        if not root :
            return node(key,lat_lng,label,adj,is_marker)
        if key<root.key:
            root.left = self.insert_node(root.left,key,lat_lng,label,adj,is_marker)
        if key>root.key:
            root.right = self.insert_node(root.right,key,lat_lng,label,adj,is_marker)

        if not root:
            return root
        root.height = max(self.tree_height(root.left),self.tree_height(root.right))+1

        bf = self.check_bf(root)
        # print(bf)
        if bf>1 and key<root.left.key:
            return self.rotateR(root)
        if bf<-1 and key>root.right.key:
            return self.rotateL(root)
        if bf>1 and key>root.left.key:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if bf<-1 and key<root.right.key:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        
        return root
    def delete(self, root, key):
 
        if not root:
            return root
 
        elif key < root.key:
            root.left = self.delete(root.left, key)
 
        elif key > root.key:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,
                                      temp.key)
 
 
        if root is None:
            return root
 
 
        root.height = 1 + max(self.tree_height(root.left),
                            self.tree_height(root.right))
 
        balance = self.check_bf(root)
 
 
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
    def search(self,root,key):
        
        if root is None or root.key == key:
            return root
    
        if root.key < key:
            return self.search(root.right,key)
    
        return self.search(root.left,key)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end=' ',sep='->')
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.key,end=' ',sep='->')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key,end=' ',sep='->')
