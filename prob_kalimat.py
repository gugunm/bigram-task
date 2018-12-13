from nltk import word_tokenize
import pandas as pd

unique = pd.read_csv('unique_word.csv').values.tolist() 
# prob_tabel = pd.read_csv('addone_smooting.csv')
prob_tabel = pd.read_csv('add_one.csv')
prob_tabel.set_index("unik", inplace = True)

# func ini digunakan untuk mengecek token dari kalimat yang diimputkan
def cek_inputan(unique=unique):
    arr_unique = []
    for kata in unique:
        arr_unique.append(kata[0])
    return arr_unique

# func ini digunakan untuk menghitung nilai probabilitas untuk inputan kalimat
# selain itu, untuk mengeluarkan nilai perplexity juga
def sentence_prob(kalimat, cek_kata=cek_inputan, kata_unik=unique, prob_tabel=prob_tabel):
    tokenizer = word_tokenize(kalimat)
    cek = cek_kata()
    result = 1
    for indeks in range(len(tokenizer)):
        if len(tokenizer) == 1:
            result = 0.1
        elif indeks < len(tokenizer)-1:
            if (tokenizer[indeks] not in cek or tokenizer[indeks+1] not in cek):
                result *= 0.1
            else:
                result *= prob_tabel[tokenizer[indeks+1]][tokenizer[indeks]]
                print(tokenizer[indeks],' ',tokenizer[indeks+1])
    perplexity = pow((1/result), (1/len(tokenizer)))
    print(1/result)
    print(1/len(tokenizer))
    return result, perplexity

# ==== M A I N ====
print("| Ketik 'ex' untuk keluar |")
sentence = input("Masukkan kalimat : ")
while sentence != 'ex':
    probabilitas, perplexity = sentence_prob(sentence)
    print("Probabilitas : ", probabilitas)
    print("Perplexity : ", perplexity, "\n")
    sentence = input("Masukkan Kata : ")
print("-Keluar-")