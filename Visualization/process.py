import psutil

class Process:
    """
    List of all process running in computer.
    """

    def get_process_list(self):
        listOfProcessNames = list()
        # Iterate over all running processes
        for proc in psutil.process_iter():
           # Get process detail as dictionary
           # pInfoDict = proc.as_dict(attrs=['pid', 'username', 'name', 'cpu_percent', 'memory_percent', 'status'])
           pInfoDict = proc.as_dict(attrs=['name', 'status', 'username'])
           # print(pInfoDict)
           # Append dict of process detail in list
           listOfProcessNames.append(pInfoDict)
        return listOfProcessNames

    def list_by_username(self, username):
            listOfProcessNames = list()
            for proc in psutil.process_iter():
               pInfoDict = proc.as_dict(attrs=['name', 'status', 'username', 'cpu_percent', 'memory_percent'])
               if username in pInfoDict['username'] and pInfoDict['cpu_percent'] > 0.0:
                   listOfProcessNames.append(pInfoDict)
            return listOfProcessNames

    def list_processed(self, list_process):
        dict = {}
        for process in list_process:
            if process['name'] in dict:
                dict[process['name']]['max_process'] += 1
                dict[process['name']]['cpu_percent'] += process['cpu_percent']
            else:
                dict[process['name']] = {}
                dict[process['name']]['max_process'] = 1
                dict[process['name']]['cpu_percent'] = process['cpu_percent']
        return dict
