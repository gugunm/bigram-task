import pandas
# import library for remove stopword
from nltk.corpus import stopwords
# import library untuk stemming
from nltk.stem import PorterStemmer
# untuk dictionary
from collections import OrderedDict
# import library untuk hapus punctuation
from nltk.tokenize import PunktSentenceTokenizer
# library untuk tokenisasi kalimat
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
# import csv untuk membaca file artikel
import csv
from collections import defaultdict
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# factori = StemmerFactory()
# stemmer = factori.create_stemmer()

# stopword yang digunakan dari Sastrawi Indonesia
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

def open_file(data_inputan):
    column = defaultdict(list)
    # untuk membaca file artikel agar dapat di baca per kolom
    with open(data_inputan) as f: 
        reader = csv.DictReader(f) # baca setiap baris sebagai dictionary
        for baris in reader: 
            for (k,v) in baris.items():
                column[k].append(v)
    return column

def praproses_kalimat(columns, nama_column):
    punctuations = '''‘!()-–[]{};:'’+"”“\,<>./`?@#$%^&*|_~''' # daftar punctuation
    arr_kolom = []
    for row in range(len(columns[nama_column])):
        lowcase_kalimat = columns[nama_column][row].lower() # lowcase semua huruf
        tokenizer = word_tokenize(lowcase_kalimat) # tokenisasi kalimat
        kalimat = ''
        for token in tokenizer:
            clean_token1 = token.replace("-"," ") #untuk mereplace "-" dengan spasi
            clean_token2 = clean_token1.replace("–"," ") #untuk mereplace "–" dengan spasi
            # clean_token3 = clean_token2.replace('   ', ' ')
            # clean_token4 = clean_token3.replace('  ', ' ')
            clean_token4 = clean_token2.replace('.', ' ')
            stopw = stopword.remove(clean_token4)
            # tidak memakai stemmer karena masih tidak sempurna librarynya
            # stemming = stemmer.stem(stopw)
            rm_punk = ''
            for char in stopw:
                if char not in punctuations:
                    rm_punk = rm_punk + char
            kalimat = kalimat + rm_punk + ' ' 
        arr_kolom.append(kalimat)
    return arr_kolom

def gabung_2array(array1, array2):
    df = pandas.DataFrame(data={"Judul": array1, "Konten": array2})
    df.to_csv("keluaran2.csv", sep=',',index=False)

kolom_judul = []
kolom = open_file('data-all.csv')
nama_kolom = ['judul', 'konten']
kolom_judul = praproses_kalimat(kolom, nama_kolom[0])
kolom_konten = praproses_kalimat(kolom, nama_kolom[1])
gabung_2array(kolom_judul, kolom_konten)
print("FINISH")
# print(kolom_judul[1])
# print(kolom_konten[1])
