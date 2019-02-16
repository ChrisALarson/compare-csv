import csv

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
                node = file_dict[row_ind]
                while node is not None:
                    if (node == row_node):
                        node.add_one()
                        node = None
                    else:
                        if node.next_row is not None:
                            node = node.next_row
                        else:
                            node.next_row = row_node
                            node = None
            else:
                file_dict[row_ind] = row_node 
    return file_dict

def print_file_dict(file_dict):
    print('printing file')
    for index, row_list in file_dict.items():
        node = row_list
        while node is not None:
            print(node)
            node = node.next_row


# tests
file1dict = create_file_dict('test/resources/file1.csv', 'employee_id')
file2dict = create_file_dict('test/resources/file2.csv', 'employee_id', ['last_name', 'first_name', 'employee_id', 'years_employed'])
print_file_dict(file1dict)
print_file_dict(file2dict)