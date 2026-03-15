import containerdata
import itertools

def print_fields():
    for name,file in containerdata.files.items():
        print(name)
        for entry,_ in zip(file.read(),range(1)):
            print([key for key in entry])
def handling():
    file = containerdata.files['handling.csv']
    handle_data = tuple(file.read())
    print(len(handle_data))
    fields = 'startrelativemarkerposition', 'endrelativemarkerposition'
    for entry in handle_data[:100]:
        start,end = map(entry.__getitem__,fields)
        print(f'start={start},end={end}')

print_fields()
handling()