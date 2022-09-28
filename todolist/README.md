[link menuju aplikasi Heroku](https://tugas2pbpsc.herokuapp.com/mywatchlist/html/) 


# Kegunaan {% csrf_token %} pada elemen <form>
CSRF merupakan singkatan dari Cross-site request forgery yang berarti pemalsuan permintaan lintas situs, 
ini merupakan suatu bentuk serangan pada aplikasi web. Peretas menipu para pengguna melalui permintaan 
untuk menjalankan tugas yang tidak ingin mereka jalankan. Server web memerlukan mekanisme untuk menentukan 
apakah pengguna yang sah membuat permintaan melalui browser pengguna untuk menghindari serangan tersebut.
Dan disinilah kegunaan dari token CSRF atau ditulis sebagai {% csrf_token %} pada html, token CSRF akan
menghasilkan nilai yang bersifat rahasia, unik, dan tidak terduga yang dihasilkan aplikasi sisi server 
untuk dimasukkan ke dalam permintaan HTTP pengguna. Saat permintaan berikutnya dibuat, server web 
akan membandingkan dua token yang ditemukan di sesi pengguna dan dalam permintaan. Jika token tidak cocok 
dengan nilai dalam sesi pengguna, permintaan akan ditolak, sesi pengguna dihentikan dan peristiwa 
dicatat sebagai potensi serangan CSRF.

# Apakah kita dapat membuat elemen <form> secara manual?

# Proses alur data 

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
