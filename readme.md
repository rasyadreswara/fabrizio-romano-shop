Tautan :
https://pbp.cs.ui.ac.id/favian.muhammad41/fabrizio-romano-shop

https://github.com/rasyadreswara/fabrizio-romano-shop.git

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

TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? :
Data delivery adalah cara data dikemas, dikirim, dan dikonsumsi antar komponen (frontend-backend, dll.). Tanpa data delivery yang rapi, platform akan macet.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? :
JSON, karena sintaksnya lebih sederhana, dan lebih ringan ringkas.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? :
Untuk mencegah data tidak valid/berbahaya masuk DB.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? :
csrf_token digunakan sebagai perlindungan terhadap CSRF, yaitu serangan di mana penyerang membuat browser korban, yang sedang login di situs, mengirimkan request berbahaya ke situs tanpa sepengatahuan korban (misalnya ganti password)






