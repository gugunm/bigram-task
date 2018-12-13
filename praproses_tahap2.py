import csv
import re

out = open('keluaran_fix.csv', 'w')  
with open ('keluaran2.csv', 'r') as f :
    reader = f.read().split("\n") #split kalimat dengan new line
    for row in reader:
        row_clean = re.sub(' +',' ',row) #untuk menghapus spasi yang lebih dari 1
        print(row_clean)
        out.write(row_clean + '\n')
out.close()