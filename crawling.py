#import wikipedia library (jangan lupa pip install wikipedia)
import wikipedia
import csv

#Inisialisasi csv writter
csvFile = open('dataset_crawling.csv', 'w', newline='')
csvWriter = csv.writer(csvFile)

#Input keyword pencarian
search_value = input('Mau Cari Apa : ')

#Melakukan pencarian dengan library wikipedia
search = wikipedia.search(search_value)

#proses data hasil pencarian
if search:
    print(f'Ditemukan {len(search)} data.')
    print('Proses Crawling Dimulai Mohon Tunggu..')
    for res in search:
        page = wikipedia.page(res)
        title = page.title
        url = page.url
        csvWriter.writerow([title, url])
    print('Proses Crawling Selesai..')
else:
    print(f'Tidak ada hasil untuk "{search_value}"')
