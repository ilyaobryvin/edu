try:
    with open('demo_data.csv', 'r') as f1, open('demo_data.json', 'r') as f2:
        ...
except FileNotFoundError as e:
    self.generateDemoFiles()