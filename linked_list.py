class Node:
    """
    This class defines a node of a linked list.
    It's two instance variables are:
    - a data holder
    - a pointer to the next node in the linked list
    """
    def __init__(self, d):
        self.Data = d
        self.Next = None

class LinkedList:
    """
    This class defines the data structure of a linked list.
    It's two instance variables are:
    - A header node
    - A current node
    Each of these variables are designed to hold a node, 
    however the nodes that they hold can be changed as one manipulates the linked list 
    using this class's methods.
    """
    
    def __init__(self, d=None):
        """
        The class constructor of a linked list that either:
        - creates an empty linked list (Header and Current empty)
        - creates a linked list with one node as both header and current
        """

        if (d==None):
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def nextCurrent(self):
        """
        This method advances the linked list's current node to:
        - the next node if the current node is not the last node in the linked list
        - the header node if the current node is the last node in the linked list
        """

        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header

    def resetCurrent(self):
        """
        This method resets the linked list's current node to the header node.
        """ 

        self.Current = self.Header

    def getCurrent(self):
        """
        This method returns: 
        - The data value of the current node, if the list is not empty.
        - None, if the list is empty.
        """

        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
        
    def insertBeginning(self, d):
        """
        This methods adds a node to the beginning of the linked list.
        If the list is empty it sets the header to a Node instantiated with the argument given in this method
        as its value. It also sets the lists current node to the header it just assigned the new node to.  
        If the list is not empty, it uses a temporary variable to hold the new node instantiated as above. 
        While the temporary variable holds the new node it sets the new node's next value to point to 
        the list's current header node.  It then sets the list's header node to the new node using the 
        temporary variable.  
        """

        if (self.Header is None):
            self.Header = Node(d)
            self.Current = self.Header
        else:
            new_node = Node(d)
            new_node.Next = self.Header
            self.Header = new_node

    def insertCurrentNext(self, d):
        """
        This method adds a new node directly following the current node.
        If the list is empty it sets the header to a Node instantiated with the argument given in this method
        as its value. It also sets the lists current node to the header it just assigned the new node to.
        If the list is not empty, it instantiates a new node using the data point give as an argument in this method
        as its value and assigns it to a temporary new node variable.  It then assigns this new node's next instance
        variable to the linked list's current node's next instance variable.  Then it sets the current node's next
        instance variable to the new node. 
        """

        if (self.Header is None):
            self.Header = Node(d)
            self.Current = self.Header
        else:
            new_node = Node(d)
            new_node.Next = self.Current.Next
            self.Current.Next = new_node

    def removeBeginning(self):
        """
        This method returns:
        - None, if the list is empty
        - the data value of the linked list's header node, removes the header node from the linked list,
        and resets the current node to be the new header node, if the list is not empty.
        """

        if (self.Header is None):
            return None
        else:
            removed_data = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return removed_data
        
    def removeCurrentNext(self):
        """
        This method returns:
        - None, if the list is empty.
        - the data value of the next node following linked list's current node while removing the node itself.
        """

        if (self.Header is None):
            return None
        else:
            removed_data = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return removed_data
        
    def printList(self):
        """
        This method uses a while loop to cycle through the linked list and print its contents to the console.
        If the linked list is empty the user will be notified.  If the linked list is not empty the user
        will see the contents of the linked list as well as the current node.
        """

        node_to_print = self.Header
        print(" ")
        while node_to_print is not None:
            print(node_to_print.Data, end=" ")
            node_to_print = node_to_print.Next
        if (self.Current is not None):
            print("Current: ", self.Current.Data)
        else:
            print("Empty Linked List")

def main():
    """
    This main function runs when the user runs this program to show case all the 
    functionality built into the Linked List class.
    """
    a_list = LinkedList()
    a_list.printList()
    a_list.insertBeginning(25)
    a_list.printList()
    a_list.insertBeginning(37)
    a_list.printList()
    a_list.nextCurrent()
    a_list.printList()
    print("The current is:",a_list.getCurrent())
    a_list.insertCurrentNext(32)
    a_list.printList()
    a_list.nextCurrent()
    a_list.printList()
    print("The current is:",a_list.getCurrent())
    a_list.resetCurrent()
    a_list.printList()
    a_list.insertCurrentNext(28)
    a_list.printList()
    print(a_list.removeBeginning())
    a_list.printList()
    print(a_list.removeCurrentNext())
    a_list.printList()

main()
print(LinkedList.__doc__)
print(Node.__doc__)