import pandas as pd

unique = pd.read_csv('unique_word.csv').values.tolist() 
prob_tabel = pd.read_csv('prob_bigram.csv')
prob_tabel.set_index("unik", inplace = True)

# func ini digunakan untuk mencari kata dengan probabilitas kemunculan tertinggi
def next_word(kata, prob_tab):
    column = list(prob_tab.columns.values)
    n_max = 0
    indeks = -1
    for i, word in enumerate(prob_tab.loc[kata, : ]):
        if word > n_max :
            n_max = word
            indeks = i
    print("Kata selanjutnya : ", column[indeks], '\n')

# func ini digunakan untuk mengecek kata inputan apakah ada pada table atau tidak
def cek_inputan(unique):
    arr_unique = []
    for kata in unique:
        arr_unique.append(kata[0])
    return arr_unique

# === M A I N ===
cek_kata = cek_inputan(unique)
print("| Ketik 'ex' untuk keluar |")
word = input("Masukkan Kata : ")
while word != 'ex':
    if word not in cek_kata:
        print('Kata tidak ditemukan', '\n')
        word = input("Masukkan Kata : ")
    else:
        next_word(word, prob_tabel)
        word = input("Masukkan Kata : ")
print("-Keluar-")