[link menuju aplikasi Heroku dalam html](https://tugas2pbpsc.herokuapp.com/mywatchlist/html/) 

[link menuju aplikasi Heroku dalam json](https://tugas2pbpsc.herokuapp.com/mywatchlist/json/ )

[link menuju aplikasi Heroku dalam xml](https://tugas2pbpsc.herokuapp.com/mywatchlist/xml/)

## Screenshot HTML
![screenshot html](https://github.com/stellinec/Tugas2/blob/main/assets/html.jpeg)

## Screenshot JSON
![screenshot json](https://github.com/stellinec/Tugas2/blob/main/assets/json.jpeg)

## Screenshot XML
![screenshot xml](https://github.com/stellinec/Tugas2/blob/main/assets/xml.jpeg)

# Perbedaan antara JSON, XML, dan HTML

HTML adalah Hypertext Markup Language yang membantu mengembangkan struktur halaman web, HTML bersifat static dan digunakan untuk menampilkan data bukan untuk mengangkut data. Sementara, XML adalah Extensible Markup Language yang membantu untuk bertukar data antar platform yang berbeda, bersifat dinamis karena digunakan untuk mengangkut data bukan untuk menampilkan data. JSON adalah format pertukaran data yang ringan dan sepenuhnya tidak bergantung pada bahasa. JSON didasari oleh pada bahasa pemrograman JavaScript, sehingga lebih mudah dimengerti dan di-*generate*.
Berikut adalah perbedaan-perbedaannya :
- HTML
    - Merupakan *markup language*
    - Tidak men-*support namespaces*
    - Sintaksnya sangat singkat dan menghasilkan teks berformat
    - Aplikasi tambahan tidak diperlukan untuk mem-*parsing* JavaScript
    - <html> merupakan root elemen dari halaman HTML
    - Didefinisikan dengan *start tag*, beberapa konten dan *end tag*
- XML
    - Merupakan *extensible markup language*
    - Men-*support namespaces*
    - Ukuran dokumen besar dan struktur tag membuatnya besar dan rumit untuk dibaca
    - DOM (Document Object Model) diperlukan untuk mem-*parsing* JavaScript
    - Harus mengandung root element, contohnya seperti <note>
    - Perlu adanya *start* dan *end tag*
    - case sensitive
- JSON
    - Merupakan *JavaScript Object Notation*
    - Tidak men-*support namespaces*
    - Ringkas dan mudah dibaca, tidak ada tag atau data yang berlebihan maupun kosong, membuat file terlihat sederhana
    - Data bisa langsung diakses sebagai objek JSON
    - Disimpan dalam bentuk *key* dan *value*
    - Tidak menggunakan *end tag*

# Mengapa data delivery diperlukan dalam pengimplementasian sebuah platform
Dikarenakan dalam pengembangan suatu platform, ada kalanya diperlukan pengiriman data dari suatu stack ke stack lainnya dan data-data tersebut bisa bermacam-macam bentuknya sehingga diperlukan adanya data delivery. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON. Data delivery disini berguna untuk menyesuaikan format data yang akan dikirimkan dengan yang di-*request*, contohnya jika browser me-*request* halaman dengan format data HTML, maka data yang dikirimkan akan berformat HTML.



# Mengimplementasikan checklist tugas

1. Membuat django-app bernama mywatchlist dengan perintah *python manage.py startapp mywatchlist*.
2. Membuka settings.py di folder "tugas2pbpsc" dan menambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat ke dalam proyek Django.
3. Menambahkan potongan kode pada models.py yang ada di folder mywatchlist.
4. Melakukan perintah *python manage.py makemigrations* untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan perintah *python manage.py migrate* untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
5. Membuat sebuah folder bernama fixtures di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama initial_watchlist_data.json dan menambahkan data watchlist di dalamnya.
6. Menjalankan perintah *python manage.py loaddata initial_watchlist_data.json* untuk memasukkan data tersebut ke dalam database Django lokal.
7. Membuat sebuah folder bernama templates di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama watchlist.html dan menambahkan potongan kode di dalamnya.
8. Pada folder mywatchlist, tepatnya di dalam file views.py, menambahkan impor HttpResponse dan Serializer pada bagian paling atas dan mengimpor models ke dalam file views.py untuk melakukan pengambilan data dari database. 
9. Membuat fungsi show_watchlist yang menerima parameter request dan mengembalikan render(request, "watchlist.html").
10. Menambahkan *return function* berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml", dan juga parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json".
11. Membuat dan menambahkan variabel "context" sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat buat pada poin 7, agar data yang ada pada variabel "context" dapat ikut di-render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
12. Membuat berkas urls.py pada folder mywatchlist dan mengimpor fungsi yang telah dibuat pada poin ke 8 dan 9, serta menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
13. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub.
14. Melakukan Deploy Aplikasi Django yang sudah dibuat ke Heroku.
