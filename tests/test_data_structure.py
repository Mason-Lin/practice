from data_structure.linked_lists import LinkedList


def test_linked_list_create():
    linked_list = LinkedList()
    assert linked_list.head is None


def test_linked_list_append():
    linked_list = LinkedList()
    linked_list.append("1")
    assert linked_list.head.data == "1"


def test_linked_list_delete_first():
    linked_list = LinkedList()
    linked_list.append("1")
    linked_list.append("2")
    linked_list.append("3")
    linked_list.delete_node_by_index(1)
    assert linked_list.head.data == "2"
    assert linked_list.head.next.data == "3"


def test_linked_list_delete_second():
    linked_list = LinkedList()
    linked_list.append("1")
    linked_list.append("2")
    linked_list.append("3")
    linked_list.delete_node_by_index(2)
    assert linked_list.head.data == "1"
    assert linked_list.head.next.data == "3"


def test_linked_list_delete_last():
    linked_list = LinkedList()
    linked_list.append("1")
    linked_list.append("2")
    linked_list.append("3")
    linked_list.delete_node_by_index(3)
    assert linked_list.head.data == "1"
    assert linked_list.head.next.data == "2"
