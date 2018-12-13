import pandas as pd
import numpy as np

unique = pd.read_csv('unique_word.csv').values.tolist() # list kata-kata unik
all_word = pd.read_csv('semua_kata.csv').values.tolist() # list semua token pada dokumen
len_allword = len(all_word) # panjang token dari dokumen untuk dimasukkan ke rumus smooting
freq_dict = np.load('./output/freq_tab.npy').item() # dictionary dari frekuensi kata
freq_tabel = pd.read_csv('freq_bigram.csv') # table frekuensi dari bigram
freq_tabel.set_index("unik", inplace = True) # indeks dari table dirubah ke kolom "unik"

# func ini digunakan untuk smooting (add_one) untuk menghindari nilai 0 saat perkaliat token pada kalimat inputan
def fill_addone(data=freq_tabel, freq_table=freq_dict, kata_unik=unique, all_vocab=len_allword):
    for i, kata1 in enumerate(kata_unik):
        for j, kata2 in enumerate(kata_unik):
            hasil = (data[kata2[0]][kata1[0]]+1.0)/(freq_table[kata1[0]]+all_vocab)
            data[kata2[0]][kata1[0]] = hasil
            print(data[kata2[0]][kata1[0]])
    print(data)
    data.to_csv('addone_smooting2.csv')

# def addone_bigram(data, kata_unik):
#     for i, kata1 in enumerate(kata_unik):
#         for j, kata2 in enumerate(kata_unik):
#             data[kata2[0]][kata1[0]] += 1
#     print(data)
#     data.to_csv('add_one.csv')

# print(freq_dict['resmi'])
fill_addone()
print("=== S U K S E S ===")