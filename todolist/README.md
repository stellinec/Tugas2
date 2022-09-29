[link menuju aplikasi Heroku](https://tugas2pbpsc.herokuapp.com/todolist) 


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

# Apakah kita dapat membuat elemen "<form>" secara manual?
Kita dapat membuat elemen "<form>" secara manual, yaitu dengan menggunakan {{form.name_of_field}}, dengan
begitu form akan dirender secara manual.
# Proses alur data 
Pertama-tama, alur akan dimulai dengan *user* yang mengetik alamat di *browser*, kemudian
*browser* akan men-*generate* HTTP *request* ke alamat yang telah dikirim oleh *user*. Server
akan menerima *request* HTTP tersebut dan mencari fungsi views.py mana yang menghandle
*path* tersebut. Kemudian ketika ketemu, akan di-*generate* halaman HTML dan dikirim ke tampilan
*browser* sebagai bentuk respon kepada *user*. *User* akan mengisi form tersebut dan *browser* akan
men-*generate* HTTP *request* dan dikirimkan ke URL destination. Data yang telah diisi oleh *user* tersebut
dapat dikirim dengan menggunakan beberapa metode, contohnya metode POST. Metode POST digunakan untuk
menyimpan data ke dalam database server. Server akan menerima HTTP *request* yang sudah di-*generate* tadi lalu akan 
mencari fungsi views.py mana yang menghandle *path* tersebut dan akan diolah datanya sesuai dengan fungsinya.
Terakhir, data yang sudah diolah akan ditaruh pada templates HTML dan server men-*generate* halaman HTML
tersebut ke tampilan *browser* sebagai bentuk respon ke *user*.

# Mengimplementasikan checklist tugas

1. Membuat django-app bernama todolist dengan perintah *python manage.py startapp todolist*.
2. Membuka settings.py di folder "tugas2pbpsc" dan menambahkan aplikasi todolist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat ke dalam proyek Django.
3. Menambahkan atribut user, date, title dan description pada models.py yang ada di folder todolist.
4. Menggunakan models.ForeignKey pada atribut user.
5. Membuat file "form.py" pada folder todolist dan membuat "class Form(forms.ModelForm):" sehingga
fields yang didalamnya nanti dapat diambil oleh models.py.
6. Melakukan perintah *python manage.py makemigrations* untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan perintah *python manage.py migrate* untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
7. Membuat sebuah folder bernama templates di dalam folder aplikasi todolist, kemudian membuat berkas todolist.html, rgister.html, login.html dan create-task.html, kemudian menambahkan potongan kode di dalamnya.
8. Pada file views.py, membuat fungsi show_todolist yang menerima parameter request dan mengembalikan render(request, "todolist.html", context).
9. Pada file views.py, membuat fungsi register yang menerima parameter request dan menambahkan potongan kode yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
10. Pada file views.py, membuat fungsi login_user yang menerima parameter request dan menambah potongan kode yang berfungsi untuk mengautentikasi pengguna yang ingin login.
11. Pada file views.py, membuat fungsi logout_user yang menerima parameter request dan menambah potongan kode yang berfungsi untuk melakukan mekanisme logout.
12. Pada file views.py, membuat fungsi create-task yang menerima parameter request dan menambah potongan kode yang berfungsi untuk menyimpan data yang diinput user ke dalam database.
13. Membuat berkas urls.py pada folder todolist dan mengimpor fungsi yang telah dibuat pada views.py, serta menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
14. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub.
15. Melakukan deploy aplikasi Django yang sudah dibuat ke Heroku.
