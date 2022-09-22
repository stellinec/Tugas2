![link menuju aplikasi Heroku dalam html]
(https://tugas2pbpsc.herokuapp.com/mywatchlist/html/) 

![link menuju aplikasi Heroku dalam json]
(https://tugas2pbpsc.herokuapp.com/mywatchlist/json/ )

![link menuju aplikasi Heroku dalam xml]
(https://tugas2pbpsc.herokuapp.com/mywatchlist/xml/)

![screenshot html](assets\html.jpeg)
![screenshot html](assets\json.jpeg)
![screenshot html](assets\xml.jpeg)

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
Dikarenakan dalam pengembangan suatu platform, ada kalanya diperlukan pengiriman data dari suatu stack ke stack lainnya, sehingga diperlukan adanya data delivery. Data yang dikirimkan bisa bermacam-macam bentuknya, beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON. 



# Mengimplementasikan checklist tugas

1. Membuat django-app bernama mywatchlist dengan perintah *python manage.py startapp mywatchlist*.
2. Membuka settings.py di folder "tugas2pbpsc" dan menambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat ke dalam proyek Django.
3. Menambahkan potongan kode pada models.py yang ada di folder mywatchlist.
4. Melakukan perintah *python manage.py makemigrations* untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan perintah *python manage.py migrate* untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
5. Membuat sebuah folder bernama fixtures di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama initial_watchlist_data.json dan menambahkan potongan kode didalamnya.
6. Menjalankan perintah *python manage.py loaddata initial_watchlist_data.json* untuk memasukkan data tersebut ke dalam database Django lokal.
7. Pada folder mywatchlist, tepatnya di dalam file views.py, membuat fungsi show_watchlist yang menerima parameter request dan mengembalikan render(request, "watchlist.html").
8. Menambahkan import HttpResponse dan Serializer pada bagian paling atas.
9. Menambahkan *return function* berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml", dan juga parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json".
10. Membuat berkas urls.py pada folder mywatchlist dan mengimpor fungsi yang telah dibuat pada poin ke 7 dan 9, serta menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
11. Membuat sebuah folder bernama templates di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama watchlist.html
12. Mendaftarkan juga aplikasi mywatchlist ke dalam urls.py yang ada pada folder "tugas2pbpsc".
13. Mengimport models ke dalam file views.py untuk melakukan pengambilan data dari database.
14. Menambah potongan kode yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.
15. Menambahkan variabel "context" sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat buat pada poin 7, agar data yang ada pada variabel "context" dapat ikut di-render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
16. Menambah kode berikut pada urls.py di folder "tugas2pbpsc" :

    ...
    path('mywatchlist/', include('mywatchlist.urls')),
    ...

17. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub.
18. Melakukan Deploy Aplikasi Django yang sudah dibuat ke Heroku
