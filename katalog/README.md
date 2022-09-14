Membuat sebuah README.md yang berisi link menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;


- Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment dikarenakan setiap program ataupun aplikasi yang kita kerjakan memiliki modul atau library dengan versi yang spesifik nya sendiri agar dapat dijalankan dengan baik. Contohnya kita mengerjakan suatu proyek dengan menggunakan django versi 1.1, aplikasi berjalan dengan baik pada modul versi 1.1. Selang beberapa waktu kemudian, django merilis versi baru dan kita mengupgradenya ke versi baru tersebut. Tetapi, ternyata proyek yang sudah kita kerjakan tadi tidak dapat berjalan dengan baik pada modul versi terbaru ini, dikarenakan adanya perubahan-perubahan fungsi. Oleh karena itu, kita memnggunakan virtual environment agar masing-masing aplikasi atau program memiliki modulnya masing-masing. Akan tetapi, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment.

- Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Pertama-tama, di dalam view.py, saya membuat fungsi show_katalog yang menerima parameter request dan mengembalikan render(request, "katalog.html", context). 

data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama' : 'Stelline Claudia',
    'id' : '2106700933'
}

kemudian saya juga menanbahkan code diatas yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam variabel context.

Setelah itu, saya membuat sebuah routing untuk memetakan fungsi yang telah saya buat pada views.py, yaitu dengan menanbahkkan code berikut pada katalog.html

{% for barang in list_barang %}
    <tr>
      <th>{{barang.item_name}}</th>
      <th>{{barang.item_price}}</th>
      <th>{{barang.item_stock}}</th>
      <th>{{barang.rating}}</th>
      <th>{{barang.description}}</th>
      <th>{{barang.item_url}}</th>
    </tr>
{% endfor %} 

Saya juga mengubah Fill me menjadi {{nama}} dan{{id}} untuk menampilkan nama dan id yang telah saya tulis pada variabel context diatas