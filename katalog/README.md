link menuju aplikasi Heroku : [https://tugas2pbpsc.herokuapp.com/]

# Bagan beserta penjelasannya

Berikut adalah link yang berisi image bagan:
[https://drive.google.com/file/d/1J7Pimkmsd0oXqKYZIf1xFP896GdhWmrs/view?usp=sharing]

Penjelasan:
Awalnya, request client akan masuk ke web aplikasi berbasis Django dan diproses melalui urls.py dan diteruskan ke views.py, kemudian views.py akan memanggil query ke models.py dan models.py akan mengembalikan database kepada views.py. Database tersebut akan diproses dan hasilnya dipetakan ke dalam berkas HTML, kemudian Django akan mengembalikan respon kepada user dengan template sebagai responnya. Dalam proses ini, urls.py berfungsi untuk mengatur segala macam routing,  models.py berperan sebagai pengelola data dan direpresentasikan oleh database, views.py berperan penerima permintaan dan mengirimkan tanggapan, dan berkas html berperan sebagai tampilan yang akan dikembalikan kepada pengguna.



# Menapa menggunakan virtual environment?

Kita menggunakan virtual environment dikarenakan setiap program ataupun aplikasi yang kita kerjakan memiliki modul atau library dengan versi yang spesifik nya sendiri agar dapat dijalankan dengan baik. Contohnya kita mengerjakan suatu proyek dengan menggunakan django versi 1.1, aplikasi berjalan dengan baik pada modul versi 1.1. Selang beberapa waktu kemudian, django merilis versi baru dan kita mengupgradenya ke versi baru tersebut. Tetapi, ternyata proyek yang sudah kita kerjakan tadi tidak dapat berjalan dengan baik pada modul versi terbaru ini, dikarenakan adanya perubahan-perubahan fungsi. Oleh karena itu, kita memnggunakan virtual environment agar masing-masing aplikasi atau program memiliki modulnya masing-masing. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, akan tetapi lebih baik menggunakan virtual environment untuk menghindari kekacauan *interdependency*.



# Mengimplementasikan poin 1 sampai dengan 4

1. Pada folder katalog, membuat fungsi show_katalog yang menerima parameter request dan mengembalikan render(request, "katalog.html") di dalam file views.py
2. Membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada views.py dengan menambahkan code pada file urls.py
4. Mengimport models ke dalam file views.py untuk melakukan pengambilan data dari database
5. Menambah potongan kode yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.
6. Menambahkan variabel "context" sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah kamu buat pada poin 1, agar data yang ada pada variabel "context" dapat ikut di-render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
7. Melakukan mapping terhadap data yang telah ikut di-render pada fungsi views untuk dapat memunculkannya di halaman HTML denagn engubah bagian "Fill me!" yang ada pada katalog.html menjadi nama dan id serta melakukan iterasi terhadap variabel list_barang untuk menampilkan isinya di dalam tabel
8. Membuat app heroku yang baru bernama "tugas2pbpsc" dan juga mengubah nama folder yang awalnya project_django menjadi tugas2pbpsc, begitu pula dengan variabel-variabel yang ada di foldernya.
9. Mengubah code yang ada di urls.py di folder tugas2pbpsc menjadi:

urlpatterns = [
    path('', include('katalog.urls')),
]

10. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub.
11. Melakukan Deploy Aplikasi Django yang sudah dibuatke Heroku
