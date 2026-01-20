# IMPLEMENTASI DEEP LEARNING BERBASIS ARSITEKTUR EFFICIENTNET-B0 UNTUK KLASIFIKASI PENYAKIT DAUN MANGGA

![Universitas Mikroskil](https://img.shields.io/badge/Universitas-Mikroskil-blue)
![Machine Learning](https://img.shields.io/badge/Course-Machine%20Learning-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/Framework-TensorFlow-orange)

## 📌 Identitas Proyek
[cite_start]**Mata Kuliah:** Pembelajaran Mesin (Semester Ganjil 2025-2026) [cite: 4]  
[cite_start]**Institusi:** Universitas Mikroskil, Fakultas Informatika, Program Studi S-1 Teknik Informatika [cite: 10, 11, 12]

### [cite_start]👥 Tim Pengembang (KELOMPOK MEUREUN) [cite: 6]
* [cite_start]**221112050** – Helga Yuliani Putri Aritonang [cite: 7]
* [cite_start]**221111780** – M. Adrian Syahputra [cite: 8]
* [cite_start]**221110676** – Raja Wira Utama [cite: 9]

---

## 📝 Deskripsi Proyek
[cite_start]Proyek ini berfokus pada penerapan *Deep Learning* untuk klasifikasi penyakit daun mangga berdasarkan data citra digital[cite: 15]. [cite_start]Penyakit daun mangga adalah masalah nyata yang dapat menurunkan produktivitas tanaman, dan inspeksi manual sering kali subjektif serta rentan terhadap kesalahan manusia (human error)[cite: 16, 50].

[cite_start]Untuk mengatasi masalah ini, kami membangun model **Convolutional Neural Network (CNN)** menggunakan arsitektur **EfficientNet-B0**[cite: 17]. [cite_start]Model ini dirancang untuk mengklasifikasikan kondisi daun mangga secara otomatis ke dalam **8 kelas**, termasuk daun sehat dan berbagai jenis penyakit[cite: 17].

### Fitur Utama:
1.  [cite_start]**Arsitektur EfficientNet-B0:** Memanfaatkan *transfer learning* dari ImageNet dengan *fine-tuning* untuk efisiensi dan akurasi tinggi[cite: 63, 64].
2.  [cite_start]**Data Augmentation:** Penerapan augmentasi data *on-the-fly* (rotasi, *flipping*, *zooming*, kecerahan) untuk meningkatkan generalisasi model pada dataset berukuran sedang[cite: 19, 70].
3.  [cite_start]**Explainability (Grad-CAM):** Menggunakan visualisasi Grad-CAM untuk meningkatkan interpretabilitas model dengan menyoroti area citra yang mempengaruhi keputusan prediksi[cite: 20].
4.  [cite_start]**Deployment:** Sistem eksperimental berbasis *cloud* menggunakan Google Colab dan aplikasi Streamlit[cite: 22, 82].

---

## 📂 Dataset
[cite_start]Dataset yang digunakan adalah **MangoLeafBD Dataset** yang diperoleh dari Kaggle[cite: 18].
* [cite_start]**Jumlah Data:** 4.000 citra *real-world* dari perkebunan mangga[cite: 18, 69].
* [cite_start]**Kelas:** 8 Kategori (7 penyakit + 1 sehat)[cite: 68].
* [cite_start]**Preprocessing:** Resizing ke 224x224 piksel, normalisasi nilai piksel[cite: 70].

---

## 🛠️ Teknologi yang Digunakan
[cite_start]Proyek ini dikembangkan menggunakan lingkungan dan *library* berikut[cite: 84]:
* **Bahasa:** Python
* **Framework DL:** TensorFlow / Keras
* **Data Processing:** NumPy, Pandas
* **Machine Learning Lib:** Scikit-learn
* **Deployment:** Streamlit
* **Environment:** Google Colab (GPU Support)

---

## 📊 Hasil Evaluasi
Berdasarkan pengujian pada data testing, model yang diusulkan mencapai performa yang sangat baik:
* [cite_start]**Akurasi:** ± 98% [cite: 21]

[cite_start]Hasil ini menunjukkan bahwa EfficientNet-B0 memberikan keseimbangan yang efektif antara akurasi dan efisiensi komputasi untuk deteksi penyakit tanaman[cite: 23].


---

## 📂 Struktur Direktori
[cite_start](Contoh struktur berdasarkan deskripsi modul [cite: 80])