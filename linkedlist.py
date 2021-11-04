# Singly linked list
# Author: Peter Karacsonyi

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def display(self):
        print(self.data)


class LinkedList:

    def __init__(self):
        self.head = None  # head is the last item added to the list
        self.tail = None  # tail is the first item, starting from there
        self.count = 0

    def append(self, data: Node):  # Place the Node specified as an argument to the end of the list

        # if type(data) is not Node:
        #     print("Unable to add item as it is not encapsulated in a Node object")
        #     return

        if not isinstance(data, Node):
            print(f"Skipping the addition of item {data} of "
                  f"type {type(data)} as it is not encapsulated in a Node object")
            return

        # If this is the very first item, set it as the head and tail
        if self.count == 0:
            self.tail = data
            self.count = 1
        else:
            self.head.next = data
            self.count += 1
        self.head = data

    def iterate(self):  # currently printing but will convert it to yield based
        if self.count > 0:
            current_item = self.tail
            while current_item is not None:
                yield current_item
                current_item = current_item.next
        else:
            print("no items in this LL yet")

    def __getitem__(self, index: int):  # Return the item at n-th position, where tail = 0 from the linked list

        item_to_return = self.tail

        if index >= self.count:
            print(f"There is no item at index {index} since the list is {self.count} long only")
            return

        for i in range(index):
            item_to_return = item_to_return.next

        return item_to_return

    def __setitem__(self, index: int, data: Node):  # overloading the index based assignment operator

        if index >= self.count:
            print(f"There is no item at index {index} since the list is {self.count} long only")
            return

        # setting the new item`s next pointer to the original next
        data.next = self.__getitem__(index).next

        # setting the previous item`s next pointer to this element
        self.__getitem__(index-1).next = data









if __name__ == '__main__':

    # Create new LL
    dogelink = LinkedList()

    # Add elements
    dogelink.append(Node("D"))
    dogelink.append(Node("O"))
    dogelink.append(Node("G"))

    # Testing an addition of not Node type
    dogelink.append("E")

    dogelink.append(Node("E"))

    # Iterating through
    print("iterating thru the list")
    for dogeitem in dogelink.iterate():
        dogeitem.display()

    # Getting an item by the overloaded address (?) operator
    print("getting the 2nd item, should be C as it is zero based")
    dogelink[2].display()

    # Replacing / Setting the 3rd item (everything is zero-based)

    dogelink[3] = Node("I")


    # Iterating through
    print("iterating thru the list")
    for dogeitem in dogelink.iterate():
        dogeitem.display()
