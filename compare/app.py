import csv

# add file list
class IndexList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def _add_row(self, row):
        if self.head is None:
            self.head = row
            self.tail = row
        else:
            self.tail.next_row = row
            self.tail = row
    
    def add_row(self, row):
        node = self.head
        while node is not None:
            if node == row:
                node.add_one()
                return True
            else:
                node = node.next_row
        self._add_row(row)
        return True
    
    def __str__(self):
        rep = ''
        node = self.head
        while node is not None:
            rep += str(node) 
            node = node.next_row
            if node is not None:
                rep += '\n'
        return rep

class RowNode:
    def __init__(self, index, data):
        self.index = index
        self.data = data
        self.count = 1
        self.next_row = None

    def add_one(self):
        self.count = self.count + 1

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        row_display = { 'index': self.index, 'data': self.data, 'count': self.count }
        return str(row_display)


def create_file_dict(file_path, index, fieldnames=None):
    file_dict = dict()
    with open(file_path) as file:
        reader = csv.DictReader(file, fieldnames)
        for row in reader:
            row_ind = row[index]
            data = dict(row)
            row_node = RowNode(row_ind, data)
            if (row_ind in file_dict):
                index_list = file_dict[row_ind]
                index_list.add_row(row_node)
            else:
                index_list = IndexList()
                index_list.add_row(row_node)
                file_dict[row_ind] = index_list
    return file_dict


def print_file_dict(file_dict):
    print('printing file')
    for index, index_list in file_dict.items():
        print(str(index_list))

# tests
file1dict = create_file_dict('test/resources/file1.csv', 'employee_id')
file2dict = create_file_dict('test/resources/file2.csv', 'employee_id', ['last_name', 'first_name', 'employee_id', 'years_employed'])
print_file_dict(file1dict)
print_file_dict(file2dict)
