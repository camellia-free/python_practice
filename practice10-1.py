with open('learning_pyhon.txt') as f:
    contents = f.read()
    print(contents)
with open('learning_pyhon.txt') as file_object:
    lines = file_object.readlines()
    
print(lines)
for line in lines:
    if 'python' in line:
        line = line.replace('python', 'java')
        
        print(line.rstrip())
    
