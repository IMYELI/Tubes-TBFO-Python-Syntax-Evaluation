# Tubes-TBFO-Python-Syntax-Evaluation

# TUGAS BESAR IF2124 - TEORI BAHASA FORMAL DAN OTOMATA
> Evaluasi syntax bahasa Python menggunakan CFG dan CYK Algorithm

## Anggota Kelompok
- Jeremy Rionaldo Pasaribu  - 13520082
- Andreas Indra Kurniawan   - 13520091
- Yakobus Iryanto Prasethio - 13520104

## Cara Run Kode
- Jika anda ingin menggunakan CFG anda sendiri gunakan format sebagai berikut pada CFG untuk convert ke CNF:
[](./Docs/img/format_cfg.png)
- Gunakan cfgConv.py untuk convert ke CNF dengan format :
- ```python cfgConv.py <Nama_file>``` contoh : ```python cfgConv.py cfg.txt```
- Pengecekan syntax dilakukan pada file cyk.py
- cyk.py memiliki 2 argumen yang dapat diambil.
- Argumen pertama merupakan file yang ingin dicek, sedangkan argumen kedua merupakan file CNF yang ingin digunakan.
- Argumen di atas tidak harus ada, jika tidak memasukan apa-apa maka akan digunakan default test.py dan cnf_out.txt.
- Jika argumen yang dipass hanya satu maka CNF default yaitu cnf_out.txt akan digunakan.
- Contoh penggunaan : ```python cyk.py <arg1> <arg2>``` ```python cyk.py test2.py CNF.txt```

## Contoh Penggunaan dan Output
[](./Docs/img/penggunaan.png) 