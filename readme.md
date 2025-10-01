Tautan :
https://pbp.cs.ui.ac.id/favian.muhammad41/fabrizio-romano-shop

https://github.com/rasyadreswara/fabrizio-romano-shop.git

TUGAS 2
Jelaskan peran settings.py dalam proyek Django! :
settings.py adalah "papan kontrol" utama proyek. Di file inilah kita menyimpan semua konfigurasi penting, misalnya INSTALLED_APPS, allowed hosts, dll.

Bagaimana cara kerja migrasi database di Django? :
saat kita run python manage.py makemigrations, django akan membandingkan model terbaru dengan versi sebelumnya, lalu membuat berkas migration. Kemudian saat kita run python manage.py migrate, akan dieksekusi berkas migration tersebut sehingga perintah berikutnya hanya menjalankan perubahan yang belum diterapkam. Hasilnya, kita tidak perlu menulis SQL manual, cukup ubah model dan run dua command di atas saja.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? :
karena django memiliki dokumentasi & komunitas besar, digunakan di industri, memiliki struktur proyek jelas, dll. Karena kemudahan, kelengkapan fitur, dan nilai praktis yang disediakan, django sering dipilih sebagai entry level framework untuk para pemula.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? :
Tidak

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. :
1. Client meminta URL tertentu
2. urls.py mencari pola yang cocok dan meneruskan request   ke view
3. views.py menjalankan logika
4. Django mengirimkan HttpResponse berisi HTML ke browser.
(bagan ada di file Bagan.drawio.svg)

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). :
1. Membuat sebuah proyek Django baru :
Pertama-tama, buka terminal, pindah ke direktori home, lalu buat folder baru bernama football-news dan masuklah ke dalamnya dengan perintah cd ~, kemudian mkdir fabrizio-romano-shop, diikuti cd football-news. Setelah berada di folder tersebut, buat lingkungan virtual terpisah agar dependensi proyek tidak bercampur dengan proyek lain; pada Windows jalankan python -m venv env, sedangkan di macOS atau Linux gunakan python3 -m venv env. Aktifkan lingkungan itu di Windows dengan env\Scripts\activate, dan di macOS/Linux dengan source env/bin/activate. Jika Windows menolak karena kebijakan eksekusi skrip, buka PowerShell sebagai administrator dan jalankan Set-ExecutionPolicy Unrestricted -Force, lalu aktifkan kembali lingkungan virtualnya.
Selanjutnya, siapkan daftar pustaka yang diperlukan dengan membuat berkas requirements.txt berisi nama-nama paket seperti django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3, dan python-dotenv, kemudian instal semuanya menggunakan pip install -r requirements.txt. Setelah dependensi terpasang, inisiasi proyek Django bernama football_news dengan perintah django-admin startproject football_news . (pastikan ada titik di akhir agar berkas proyek langsung tercipta di folder yang sama).
Terakhir, jalankan perintah python manage.py migrate (atau python3 pada Unix) untuk membuat tabel awal di basis data yang sesuai, lalu hidupkan server pengembangan dengan python manage.py runserver. Jika semua langkah berhasil, buka alamat http://127.0.0.1:8000/ di peramban dan Anda akan melihat halaman awal Django, menandakan proyek sudah siap dikembangkan lebih lanjut.

2. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Di dalam main saya tambahkan 
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [ path('', show_main, name='show_main') ]
Ini artinya ketika user membuka localhost, Django akan memanggil fungsi show_main, kemudian di urls.py tambahkan
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [ path('', show_main, name='show_main') ]
Baris ini akan meneruskan seluruh URL kosong ('') ke aturan yang ada di main/urls.py
Alurnya: browser mengirim permintaan ke server → Django memeriksa urls.py proyek → jika pola cocok dengan include('main.urls') maka dicek lagi di urls.py aplikasi → jika cocok dipanggil view, jika tidak Django menampilkan 404. Setelah konfigurasi, jalankan python manage.py runserver dan buka localhost untuk melihat halaman utama.

3. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
thumbnail sebagai gambar item dengan tipe URLField.
category sebagai kategori item dengan tipe CharField.
is_featured sebagai status unggulan item dengan tipe BooleanField.
Untuk checklist kita hanya perlu menambahkan hal hal tersebut pada models.py

4. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu dan membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Untuk menampilkan data di halaman HTML Django, cukup impor fungsi render di views.py, lalu buat fungsi show_main(request) yang menyiapkan context misalnya `{'npm':'240123456', 'name':'Haru Urara', 'class':'PBP A'}`dan mengembalikannya dengan `render(request, "main.html", context)`. Di template main.html, tampilkan data itu memakai sintaks variabel Django: `{{ npm }}`, `{{ name }}`, dan `{{ class }}`. Dengan cara ini, saat pengguna membuka halaman, Django mengambil nilai dari context dan menuliskannya di tempat yang sudah ditandai di file HTML.

5. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Untuk melakukan deployment ke PWS, perlu kita setup di website PWS pacil secara langsung, kemudian kita run git push pws master di terminal.
---------------------------------------------------------------
TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? :
Data delivery adalah cara data dikemas, dikirim, dan dikonsumsi antar komponen (frontend-backend, dll.). Tanpa data delivery yang rapi, platform akan macet.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? :
JSON, karena sintaksnya lebih sederhana, dan lebih ringan ringkas.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? :
Untuk mencegah data tidak valid/berbahaya masuk DB.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? :
csrf_token digunakan sebagai perlindungan terhadap CSRF, yaitu serangan di mana penyerang membuat browser korban, yang sedang login di situs, mengirimkan request berbahaya ke situs tanpa sepengatahuan korban (misalnya ganti password)

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). :

1. Pertama yang kita lakukan adalah membuat form input data sehingga nantinya bisa digunakan untuk menambah produk, kita lakukan ini dengan membuat class baru pada forms.py yaitu class ProductForm, class ini akan menerima data untuk product yang akan ditambahkan seperti nama, deskripsi, dan kategorinya. Kemudian kita akan buat 2 fungsi baru pada views.py yaitu create_product dan show_product. create_product akan menghasilkan form yang menambahkan data product secara otomatis ketika data disubmit ke dalam form, show_product akan mengambil objek dari produk, jika objek tersebut tidak ditemukan maka akan dikembalikan 404. Setelah membuat fungsi baru, buka urls.py pada main dan import fungsi yang sudah dibuat. Buka main.html pada templates dan update kode sehingga dibuat tombol baru yaitu "Add Product". Buat dua file baru yaitu create_product.html dan product_detail.html, create_product.html akan berfungsi sebagai penampil form yang sudah dibuat pada forms.py, dan product_detail.html akan berfungsi sebagai penampung data atau detail dari product tersebut. 
2. Kedua yang kita lakukan adalah membuat 4 fungsi yaitu, show_xml, show_json, show_xml_by_id, show_json_by_id. Keempat fungsi ini umumnya, menurut pengetahuan saya, memiliki fungsi yaitu mengembalikan data. Perbedaan dari show_xml/json dengan show_xml/json_by_id adalah show_xml/json akan mengembalikan seluruh data menurut format masing masing, sedangkan show_xml/json_by_id akan mengembalikan sebuah data spesifik.
3. Ketiga dan final step yang perlu dilakukan adalah penggunaan postman. Postman akan digunakan sebagai tempat melihat dan mengeksplor data yang dikembalikan dari endpoint (show_json, show_xml, and etc.) Dengan postman sebagai data viewer, kita dapat dengan mudah mencari/memvalidasi data.

TUGAS 5
Prioritas CSS mengikuti urutan: !important paling tinggi, lalu inline style, lalu selector ID, kemudian class/attribute/pseudo-class, lalu tag/pseudo-element; jika tingkatnya sama maka aturan yang ditulis paling akhir menang, dan sebagian properti bisa diwariskan.

Responsive design penting karena tampilan harus nyaman di berbagai ukuran layar, meningkatkan UX dan SEO, serta menghemat biaya perawatan satu basis kode; contoh yang sudah responsif: portal berita atau dokumentasi modern (layout berubah mulus di ponsel), sedangkan situs lama berlebar tetap 960px yang butuh zoom adalah contoh yang belum responsif.

Margin adalah jarak di luar border, border adalah garis pembatas elemen, dan padding adalah jarak di dalam border mengelilingi konten; ketiganya diatur dengan properti margin, border, dan padding (bisa per sisi seperti -top/-right/-bottom/-left).

Flexbox adalah tata letak satu dimensi (baris ATAU kolom) yang cocok untuk navbar, alignment, dan deret tombol; Grid adalah tata letak dua dimensi (baris DAN kolom) yang ideal untuk kerangka halaman atau galeri, gunakan Flexbox untuk merapikan sebaris/sekolom, dan Grid saat butuh kontrol area/layout yang kompleks.




