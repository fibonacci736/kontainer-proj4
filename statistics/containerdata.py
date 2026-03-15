import csv
from pathlib import Path

class CSVFile:
    def __init__(self,path : Path):
        self.path = path
    def read(self):
        with self.path.open(newline='') as file:
            for line in csv.DictReader(file):
                yield line

data_dir = Path(__file__).parent / 'data'
paths = [path for path in data_dir.iterdir() if path.suffix == '.csv']
files = {  path.name : CSVFile(path)  for path in data_dir.iterdir() if path.suffix == '.csv'}
#files = [CSVFile(path) for path in paths]