import yaml

class TaskLogger:
    def __init__(self, path):
        self.path = path

    def read(self) -> []:
        with open(self.path, 'r') as file:
            self.log_item_list = yaml.load(file, Loader=yaml.FullLoader)
        if self.log_item_list == None:
            self.log_item_list = []

        return self.log_item_list

    def append(self, log_item):
        self.log_item_list += [log_item]
        with open(self.path, 'w') as file:
            log_item_list_dump = yaml.dump(self.log_item_list, file)
