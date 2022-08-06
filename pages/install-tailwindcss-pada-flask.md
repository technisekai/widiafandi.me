title: Catatan Install Tailwindcss pada Microservice Flask
author: Widi Afandi
description: Cara membuild TailwindCSS pada microservice flask untuk kebutuhan production
date: August 06, 2022
image: https://picsum.photos/id/180/600/400
tags:
  - web-dev
  - css
  - tailwindcss

## 1. Install Tailwindcss
Ketik perintah berikut untuk instalasi tailwindcss pada **terminal/cmd kamu**. Untuk direktorinya bebas sih mau dimanapun aja<pre><code class="language-bash">npm install -D tailwindcss</code></pre>

## 2. Buat File Konfigurasi Tailwindcssmu di Dalam Project
Pindah ke dalam direktori project flask. Misalkan project flasknya bernama **my_projects** maka masuk ke dalam direktori **my_projects**  terlebih dahulu dan ketik perintah dibawah untuk membuat file konfigurasi tailwindnya. <pre><code class="language-bash">npx tailwindcss init</code></pre>

## 3. Buka File Konfigurasi Tailwind
Kamu akan mendapatkan file dengan nama `tailwind.config.js`. Buka file tersebut dan tambahkan path file html dan js.
<pre>
    <code class="language-js">
        module.exports = {
            content: [
                "./templates/*.html", 
                "./static/js/*.js"
            ],
            theme: {
                extend: {},
            },
            plugins: [],
        }
    </code>
</pre>

## 4. Tambahkan Tailwind directives ke CSS Utama
Buat file baru dengan nama input.css pada direktori static/css. Kemudian di dalam file tersebut tambahkan script berikut
<pre>
    <code class="language-css">
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
    </code>
</pre>

## 5. Build TailwindCSS
Ketikkan perintah berikut untuk build CSS Tailwind. Setelah mendapat file baru kamu bisa import di project flasknya seperti biasa
<pre><code class="language-bash">npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch</code></pre>
