title: Apa itu CVE-2022-30190 dan Kaitannya Dengan Microsoft Word
author: Widi Afandi
description: Membahas tentang kerentanan CVE-2022-30190 pada Microsoft Word
date: June 11, 2022
tags:
  - Cyber Security
  - CVE
  - Microsoft Word

Microsoft word aplikasi yang dikembangkan oleh perusahaan Microsoft sebagai aplikasi pengolah kata yang digunakan untuk membuat laporan, makalah, tugas akhir, atau dokumen lain. Aplikasi ini dikembangkan untuk berbagai system operasi seperti DOS, Apple Macintosh, SCO UNIX, OS/2, dan tentunya Microsoft Windows. Tentu sebagai sebuah aplikasi, Microsoft word tak terlepas dari bug dan kerentanan-kerentanan yang mengakibatkan pengguna dirugikan secara materiil ataupun imateriil.

Baru-baru ini, terdapat sebuah exploit baru yang tergolong dalam 0day yang dampaknya sangat fatal bagi pengguna sistem operasi windows. Dilansir dari situs LOGIQUE, **Exploit 0day** merupakan serangan cyber yang terjadi pada hari yang sama saat kelemahan atau kerentanan ditemukan di dalam sistem perangkat lunak. Penyerang yang mengetahuinya kemudian akan mengeksploitasi kerentanan sebelum diperbaiki oleh pihak pengembang. Dengan tidak adanya update pada aplikasi, maka kerentanan tersebut dapat digunakan secara bebas oleh penyerang. 

Terkait exploit yang tadi disebutkan, apakah sudah bisa menebak aplikasi apa yang baru-baru ini memiliki kerentanan 0day dimana sampai saat artikel ini dibuat belum ada patchnya? Yap benar, Microsoft word. Exploit ini dinamakan **CVE-2022-30190**. Secara umum, kerentanan ini termasuk pada **remote execution code** yang memungkinkan orang lain bisa mengambil alih computer yang kamu gunakan.
<center><blockquote class="twitter-tweet"><p lang="en" dir="ltr">🚨 CRITICAL ALERT <br><br>A severe 0-day vulnerability called <a href="https://twitter.com/hashtag/Follina?src=hash&amp;ref_src=twsrc%5Etfw">#Follina</a> has been exposed (since May 27th) in MS Word Documents.<br><br>It could allow hackers to take full control of your computer, in some cases WITHOUT even opening the file. 🧵</p>&mdash; Wallet Guard @ Consensus (@wallet_guard) <a href="https://twitter.com/wallet_guard/status/1531848479911432192?ref_src=twsrc%5Etfw">June 1, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></center>
Cara kerja **CVE-2022-30190** ini cukup sederhana, Ketika kita membuka file dengan ekstensi word atau rtf yang sudah disisipi exploit tersebut bahkan preview saja maka computer kita sudah masuk dalam genggaman penyerang. Ya itu penjelasan secara umumnya, secara teknis berdasarkan dari akun twitter @wallaet_guard CVE-2022-30190 bekerja dengan cara:

1. Exploit ini merupakan sebuah exploit gunungan yang bertumpuk di atas satu sama lain. Sayangnya, exploit ini tidak dapat dideteksi oleh antivirus.

2. Sebenarnya, exploit ini disebabkan oleh salah satu fitur microsoft yaitu Microsoft Support Diagnostic Tool (MSDT) dimana fitur ini mengizinkan microsoft word untuk menjalankan kode HTML dan Javascript dari luar.

3. Dengan payload HTML dan Javascript, payload berjalan sesuai perintah powershell dibawah ini untuk menjalankan layanan MSDT. MSDT sendiri mengizinkan untuk remote access ke komputer kamu. <p align="center">
  <img src="https://pbs.twimg.com/media/FUI0zx8WAAMEbNh?format=png&name=small" width="90%" align="tcenter"><div class="fs-6 text-center fst-italic">Perintah powershell untuk menjalankan layanan MSDT</div>
</p> 

4. Umumnya, MSDT akan meminta pengguna memasukan password untuk menjalankan layanannya. Tetapi MSDT memiliki kerentanan bufferoverflow sehingga permintaan password ini dapat terbypass sehingga pada tahap ini penyerang dapat memiliki akses penuh ke komputer kamu jika kamu masuk sebagai administrator. <p align="center"><img src="https://pbs.twimg.com/media/FUI0IHaWQAA5UV-?format=jpg&name=small" width="70%" align="tcenter"><div class="fs-6 text-center fst-italic">Bypass input password melalui bufferoverflow vulnrealibility</div>
</p>

Ketika penyerang sukses mengeksploitasi, maka penyerang dapat **memiliki akses ke komputermu** dan melakukan berbagai hal seperti menginstall program, melihat, mengubah, dan hapus data bahkan membuat user baru.

Lalu bagaimana? Apakah ada solusinya? Sementara ini belum ada solusi untuk menangani kerentanan ini. Ketika kamu sudah terkena serangan ini sangat disarankan untuk **install ulang bersih** dengan memformat seluruh penyimpananmu. Tapi tentunya ada beberapa pencegahan yang bisa dilakukan untuk terhindar dari CVE ini diantaranya:

1.	Matikan MSTD URL protocol dengan cara
	1. Buka Command Prompt sebagai Administrator
	2. Backup file registry key dengan eksekusi perintah dibawah:
	<pre>
		<code class="language-bash fs-6">
			reg export HKEY_CLASSES_ROOT\ms-msdt nama_file
		</code>
	</pre>
	3. Untuk mematikan MSDT eksekusi perintah:
	<pre>
		<code class="language-bash fs-6">
			Execute the command "reg delete HKEY_CLASSES_ROOT\ms-msdt /f"
		</code>
	</pre>
	*Nb: Ganti nama_file dengan nama file yang diinginkan*

2.	Jangan download file mencurigakan dengan format word atau rtf jika kepepet bisa pakai mac, linux, atau android untuk mendownload file tersebut.

Tapi tenang saja, misalkan kamu download dokumen untuk suatu keperluan kuliah pada website <a href="https://ittekom-pwt.ac.id" target="_blank" class="fw-bold">ittekom-pwt.ac.id</a> kamu tidak perlu khawatir terkena kerentanan ini. Atau misalkan kamu sedang daftar menjadi mahasiswa baru di website penerimaan mahasiswa <a href="https://pmb.ittekom-pwt.ac.id" target="_blank" class="fw-bold">pmb.ittekom-pwt.ac.id</a> dan diminta download dokumen ikuti saja dan itu tetap aman. Tapi kalau kamu ragu-ragu mungkin bisa hubungi <a href="https://sisfo.ittekom-pwt.ac.id" target="_blank" class="fw-bold">sisfo.ittekom-pwt.ac.id</a> aja biar nambah yakin dan sisfo akan merespon pertanyaanmu secepat mungkin.
Sekian aja deh ya mungkin yang bisa disampein kita tunggu aja semoga ada patch buat kerentanan ini dan semoga dengan infromasi ini kita lebih aware lagi. Terima kasih.

Terima kasih sudah memberikan informasi yang sangat bermanfaat khususnya kepada:

1. <a href="https://twitter.com/wallet_guard/status/1531848479911432192" target="_blank">https://twitter.com/wallet_guard/</a>

2. <a href="https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/?fbclid=IwAR1rk9HIz4_crvHJSUi6RkdMCs_wDPtRwYIO0xkOyMmNwLyMSzFIxsu3nZ4" target="_blank">msrc-blog.microsoft.com</a>

3. <a href="https://www.logique.co.id/blog/2019/11/06/zero-day-attack/" target="_blank">www.logique.co.id</a>


 

