list1 = ['Administrator', 'Python', 'Test', 'Users', 'Pycharm',
          'DataAnlysist', 'Program', 'Anaconda', 'Project', 'Main', 'Console']
lengths = {string: len(string) for string in list1}
for string, length in lengths.items():
    print(f"{string}: {length}")