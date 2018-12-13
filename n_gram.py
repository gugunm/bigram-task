from nltk import word_tokenize
import csv
import numpy as np
import pandas as pd

# func ini digunakan untuk membuat model unigram
def save_unigram(file_data):
    unik_kata = open('unique_word.csv', 'w')
    semua_kata = open('semua_kata.csv', 'w')
    with open (file_data, 'r') as f :
        reader = f.read().split("\n")
        freq_tab = {}
        total_kata = 0
        for row in reader:
            reader2 = row.split(',') # split judul dan kontennya menggunakan koma
            for kolom in reader2:
                tokenizer = word_tokenize(kolom) # tokenisasi
                for token in tokenizer:
                    if token not in freq_tab: # jika token tidak ada di dictionary
                        freq_tab[token] = 1 # assign 1
                        unik_kata.write(token + '\n')
                    else:
                        freq_tab[token] += 1 # plus 1
                    semua_kata.write(token + '\n')
                    total_kata += 1
        prob_tab = {}
        for kata in freq_tab:
            prob_tab[kata] = freq_tab[kata]/total_kata # dictionary buat probabilitas unigram
        # Save dictionary into file
        np.save('./output/prob_tab.npy', prob_tab)
        np.save('./output/freq_tab.npy', freq_tab)
        print(total_kata)
    semua_kata.close()
    unik_kata.close()

#function ini digunakan untuk mengisi table frekuensi bigram
def fill_freq_bigram(unique, data):
    zero_tab = np.zeros(shape=(len(unique),len(unique)), dtype=float) # inisialisasi table 2 dimensi dengan size(kata yang unik)
    df = pd.DataFrame( # membuat table dengan index dan kolom dari setiap kata unik
        zero_tab, #isi dari index dan kolomnya adalah table zero
        index=pd.Index(unique, name='unik'), # header index "unik"
        columns=pd.Index(unique, name='attribute') #header kolom "attribute"
    )
    # df2 = df.values.tolist()
    # for i, kata in enumerate(unique):
    #     print(i , ' ' , kata, ' ', unique[i])
    # with open (data, 'r') as f :
    #     reader = f.read().split("\n")
    #     for row in reader:
    #         reader2 = row.split(',')
    #         for kolom in reader2:
    #             tokenizer = word_tokenize(kolom)
    #             for j, kata1 in enumerate(unique):
    #                 for k, kata2 in enumerate(unique):
    #                     for indeks in range(len(tokenizer)):
    #                         if indeks < len(tokenizer)-1:
    #                             df[tokenizer[indeks+1]][tokenizer[indeks]] += 1
    
    # for j, kata1 in enumerate(unique):
    #     for k, kata2 in enumerate(unique):
    #         count = 0
    #         for i, token in enumerate(all_words):
    #             if i < len(all_words)-1:
    #                 print(all_words[i], ' ', all_words[i+1])
    #                 if token == kata1 and all_words[i+1] == kata2:
    #                     count += 1
    #         df[j][k] = count

    # df.to_csv('./tupro1/frekuensi_bigram.csv')
    
    with open (data, 'r') as f :
        reader = f.read().split("\n")
        for row in reader:
            reader2 = row.split(',')
            for kolom in reader2:
                tokenizer = word_tokenize(kolom)
                for indeks in range(len(tokenizer)):
                    if indeks < len(tokenizer)-1:
                        df[tokenizer[indeks+1]][tokenizer[indeks]] += 1
    df.to_csv('freq_bigram.csv')
    return df

# func ini digunakan untuk mengisi probabilitas pada table bigram
def fill_prob_bigram(data, freq_table, kata_unik):
    for i, kata1 in enumerate(kata_unik):
        for j, kata2 in enumerate(kata_unik):
            data[kata2][kata1] = data[kata2][kata1]/freq_table[kata1] # assign frekuensi untuk table bigram.
    print(data)
    data.to_csv('prob_bigram.csv')

# function ini digunakan untuk ekstraksi file kata yang unik dari .csv menjadi list
def bigram_v2(unik):
    arr_unique = []
    with open (unik, 'r') as f :
        reader = f.read().split("\n")
        for i in range(len(reader)):
            arr_unique.append(reader[i])
            # print(reader[i])
        # print(i)
    return arr_unique

# ========= MAIN ========
data = 'keluaran_fix.csv'

''' uncomment baris dibawah ini untuk menjalankan program untuk membuat model unigram '''
# save_unigram(data)

'''uncomment 5 baris dibawah ini untuk menjalankan program untuk membuat model bigram '''
# unique_kata = bigram_v2('unique_word.csv')
# freq_table = np.load('./output/freq_tab.npy').item()
# tabel_frekuensi = fill_freq_bigram(unique_kata, data)
# print(tabel_frekuensi)
# fill_prob_bigram(tabel_frekuensi, freq_table, unique_kata)


# ==== N O T U S E ====
# semua_kata = pd.read_csv('./tupro1/semua_kata.csv').values.tolist()
# Load dictionary from file
# prob_table = np.load('./tupro1/output/prob_tab.npy').item()
# tabel_frekuensi = pd.read_csv('./tupro1/freq_bigram.csv')