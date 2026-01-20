# IMPLEMENTASI DEEP LEARNING BERBASIS ARSITEKTUR EFFICIENTNET-B0 UNTUK KLASIFIKASI PENYAKIT DAUN MANGGA

![Universitas Mikroskil](https://img.shields.io/badge/Universitas-Mikroskil-blue)
![Machine Learning](https://img.shields.io/badge/Course-Machine%20Learning-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/Framework-TensorFlow-orange)

## 📌 Identitas Proyek
**Mata Kuliah:** Pembelajaran Mesin (Semester Ganjil 2025-2026) 
**Institusi:** Universitas Mikroskil, Fakultas Informatika, Program Studi S-1 Teknik Informatika 

### 👥 Tim Pengembang (KELOMPOK MEUREUN)
* **221112050** – Helga Yuliani Putri Aritonang 
* **221111780** – M. Adrian Syahputra 
* **221110676** – Raja Wira Utama 

---

## 📝 Deskripsi Proyek
Proyek ini berfokus pada penerapan *Deep Learning* untuk klasifikasi penyakit daun mangga berdasarkan data citra digital[cite: 15].Penyakit daun mangga adalah masalah nyata yang dapat menurunkan produktivitas tanaman, dan inspeksi manual sering kali subjektif serta rentan terhadap kesalahan manusia (human error).

Untuk mengatasi masalah ini, kami membangun model **Convolutional Neural Network (CNN)** menggunakan arsitektur **EfficientNet-B0**. Model ini dirancang untuk mengklasifikasikan kondisi daun mangga secara otomatis ke dalam **8 kelas**, termasuk daun sehat dan berbagai jenis penyakit.

### Fitur Utama:
1. **Arsitektur EfficientNet-B0:** Memanfaatkan *transfer learning* dari ImageNet dengan *fine-tuning* untuk efisiensi dan akurasi tinggi.
2. **Data Augmentation:** Penerapan augmentasi data *on-the-fly* (rotasi, *flipping*, *zooming*, kecerahan) untuk meningkatkan generalisasi model pada dataset berukuran sedang.
3. **Deployment:** Sistem eksperimental berbasis *cloud* menggunakan Google Colab dan aplikasi Streamlit.

---

## 📂 Dataset
Dataset yang digunakan adalah **MangoLeafBD Dataset** yang diperoleh dari Kaggle.
* **Jumlah Data:** 4.000 citra *real-world* dari perkebunan mangga.
***Kelas:** 8 Kategori (7 penyakit + 1 sehat).
***Preprocessing:** Resizing ke 224x224 piksel, normalisasi nilai piksel

---

## 🛠️ Teknologi yang Digunakan
Proyek ini dikembangkan menggunakan lingkungan dan *library* berikut:
* **Bahasa:** Python
* **Framework DL:** TensorFlow / Keras
* **Data Processing:** NumPy, Pandas
* **Machine Learning Lib:** Scikit-learn
* **Deployment:** Streamlit
* **Environment:** Google Colab (GPU Support)

---

## 📊 Hasil Evaluasi
Berdasarkan pengujian pada data testing, model yang diusulkan mencapai performa yang sangat baik:
**Akurasi:** ± 98% 

Hasil ini menunjukkan bahwa EfficientNet-B0 memberikan keseimbangan yang efektif antara akurasi dan efisiensi komputasi untuk deteksi penyakit tanaman.