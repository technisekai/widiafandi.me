title: Deploy Flask App ke Hosting Vercel
author: Widi Afandi
description: Deploy flask ke hosting vercel
date: August 11, 2021
image: https://picsum.photos/id/1018/600/400
tags:
  - Flask
 
Halo semuanya kali ini saya akan membahas bagaimana cara untuk mendeploy web yang menggunakan flask pada vercel.
Vercel merupakan hosting gratis namun soal kecepetan akses ke web yang dideploy menurut saya pribadi vercel lebih cepat dibandingkan herokuapp.
Untuk flask sendiri ialah sebuah microservices dari python yang digunakan sebagai backend. Flask ini mirip-mirip dengan django tapi katanya sih lebih simple flask.

### **1. Siapkan web flask**
Pertama siapkan web flask yang akan didideploy. Bila belum punya, temen-temen bisa download di <a href="https://github.com/technisekai/flask-project" target="_blank">**github**</a> saya. 
atau bisa membuat web flask sederhana sendiri mengikut dokumentasi dari flask.

### **2. Masuk ke folder yang ingin dideploy dan lakukan export**
Masuk ke folder project temen-temen kemudian ketik perintah dibawah pada terminal/cmd
<pre>
	<code class="language-bash ">
		export FLASK_APP=app.py
		export FLASK_ENV=development
	</code>
</pre>

### **3. Jalankan script**
Ketik perintah dibawah pada terminal/cmd untuk menjalankan project flask kita pada localhost <pre><code class="language-bash">flask run</code></pre>

### **4. Buat akun vercel**
Buat akun atau login pada akun <a href="https://vercel.com/login" target="_blank">**vercel**</a>

### **5. Install vercel**
Install vercel pada terminal atau cmd. disini saya menggunakan npm untuk install<pre><code class="language-bash">npm i -g vercel</code></pre>
*Jika gagal bisa tambahkan sudo di depan*

### **6. Buat script vercel.json**
Buatlah file berformat .json dan isi dengan code berikut. Untuk src dan dest sesuaikan dengan nama file pythonnya. Kemudian save pada folder root project
<pre>
	<code class="language-javascript">
		{
			"version": 2,
			"builds": [
				{
					"src": "./app.py",
					"use": "@vercel/python"
				}
			],
			"routes": [
				{
					"src": "/(.*)",
					"dest": "app.py"
				}
			]
		}

	</code>
</pre>

### **7. Buat file requirements.txt**
Teman-teman bisa langsung menggunakan library freeze untuk melist library yang digunakan.
<pre><code class="language-bash ">pip freeze > requirements.txt</code></pre>

### **8. Mari mendeploy**
Persiapan telah selesai, sekarang waktunya mendeploy project kita ke vercel. pertama jalankan perintah dibawah pada terminal atau cmd
<pre><code class="language-bash ">vercel --prod</code></pre>
Kemudian bisa diikuti seperti gambar dibawah

*Untuk "What’s the name of your existing project?" bisa disesuakan dengan nama web temen-temen misal mau nama web
makanankhas ya ganti aja dengan itu*
<figure><img src="{{ url_for('static', filename='assets/images/articles-image/deploy_flask_app_vercel/step-7.png') }}" class="mx-auto mt-2 md:w-4/5 sm:w-96"><figcaption class="text-sm font-bold text-center lg:text-base">Fig 1 - Konfigurasi sebelum deploy</figcaption></figure>

**Special thanks to:** 

1. [**dev.to**](https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k)
