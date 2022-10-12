[link menuju aplikasi Heroku](https://tugas2pbpsc.herokuapp.com/todolist) 
# TUGAS 6
# Perbedaan antara asynchronous programming dengan synchronous programming
*Asynchronous programming* merupakan teknik pemograman dimana beberapa tugas dapat berjalan secara bersamaan tanpa menunggu tugas lain selesai. *Asynchronous programming* menganut protokol input dan output (I/O) non-blocking, yang berarti tidak memblokir eksekusi lebih lanjut saat satu atau lebih operasi sedang berlangsung, hal ini menandakan program asinkron tidak menjalankan operasi dalam urutan hierarkis atau berurutan. 

*Synchronous programming* merupakan teknik pemograman dimana tugas dijalankan satu persatu sesuai dengan urutan serta prioritasnya, penyelesaian tugas pertama memicu tugas berikutnya, dan seterusnya. *Synchronous programming* menganut protokol  I/O blocking, yang berarti saat satu operasi sedang dilakukan, instruksi operasi lainnya diblokir.


# Apa itu paradigma Event-Driven Programming dan contoh penerapannya pada tugas ini
*Event-Driven Programming* adalah paradigma di mana aliran kontrol program ditentukan oleh terjadinya suatu peristiwa (contohnya seperti pengguna meng-klik mouse, mouse yang di-klik inilah yang disebut sebagai peristiwa). Peristiwa ini dipantau oleh kode yang dikenal sebagai *event listener*. Jika terdeteksi telah terjadinya peristiwa yang sudah ditetapkan, maka ia akan menjalankan *event handler* (merupakan *callback* fungsi yang dipicu saat peristiwa terjadi).
Pada tugas ini sendiri, *Event-Driven Programming* telah diterapkan untuk membuat tombol Add Task yang akan membuka
sebuah modal dengan form untuk menambahkan task. Disini tombol yang ditekan akan menjadi peristiwanya.

# Penerapan asynchronous programming pada AJAX.
Asynchronous programming diterapkan pada AJAX ketika AJAX membuat halaman web memperbarui data secara asinkronus dengan mengirimkan data ke server di balik layar, artinya sebagian elemen data pada halaman dapat diperbaharui tanpa harus di-reload keseluruhan halaman.

# Mengimplementasikan checklist tugas
1. Membuat view show_json yang mengembalikan seluruh data task dalam bentuk JSON.
2. Menambahkan path `/todolist/json` yang mengarah ke view show_json.
3. Membuat view add_task untuk menambahkan task baru ke dalam database.
4. Menambahkan path `/todolist/add` yang mengarah ke view add_task.
5. Mengubah file todolist.html dengan mengimplementasikan AJAX pada fungsionalitas todolist.
6. Membuat modal yang melakukan pengambilan input user.
7. Membuat sebuah tombol `Add Task` yang membuka modal dengan form untuk menambahkan task.
8. Melakukan pengirimkan data task untuk diproses menggunakan AJAX POST.
9. Melakukan pengambilan data task menggunakan AJAX GET.