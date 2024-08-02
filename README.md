# **Daegu Apartment**

Capstone Project Module 3 Kevin Tasyah Rahmatullah.
Capstone ini bertujuan untuk memenuhi standar kelulusan Purwadhika Digital Technology School Jakarta.

## **Context**

**Apartemen** adalah jenis unit perumahan yang biasanya merupakan bagian dari bangunan atau kompleks yang lebih besar dan biasanya disewakan kepada individu atau keluarga. Unit-unit ini mungkin "mandiri", artinya memiliki dapur, kamar mandi, dan ruang tamu sendiri, atau mungkin lebih mirip studio, dengan gabungan ruang tamu dan ruang tidur.
Apartemen menjadi salah satu jawaban atas kebutuhan hunian masyarakat modern akibat terbatasnya lahan hunian dan padatnya aktivitas bisnis di perkotaan. Oleh karena itu, akan sangat menarik untuk mengkaji harga apartemen yang dipengaruhi oleh berbagai faktor internal dan eksternal.

## **Business Problem**

Cukup sulit bagi pemilik, yang dimana sebagai *stakeholder* yang ingin menyewakan unit mereka untuk menyesuaikan dengan harga pasar tersebut. Jika harganya terlalu tinggi dibandingkan harga pasar tentu akan sulit melakukan sewa. Sebaliknya, jika harganya terlalu rendah maka pemilik akan kesulitan mendapatkan keuntungan yang maksimal.

## **Goal**

*Stakeholder* merekrut *Data Scientist* untuk **membuat "tool" yang dapat membuat prediksi harga unit apartemen** untuk pemilik unit yang mana bisa menentukan harga sewa unit apartemen yang tepat, dan juga membantu *tenant* untuk mendapatkan harga sewa unit apartement yang terjangkau.

## **Analytic Approach**

Maka dari itu, *Data Scientist* harus **menganalisis dataset *Daegu* Apartemen** untuk mendapatkan pola sewa unit dari fitur-fitur yang terdapat dari dataset tersebut, yang mana bisa membedakan antara unit apartemen satu dengan unit apartemen yang lainnya.

## **Metric Evaluation**

Evaluasi metrik yang akan digunakan adalah **RMSE**, **MAE**, dan **MAPE**.

1) **RMSE** adalah akar dari Jumlah selisih kuadrat antara nilai yang dipasang pada model regresi dan nilai observasi yang dibagi dengan jumlah titik historis, dikurangi jumlah parameter dalam model regresi. Jumlah parameter dalam model regresi dikurangi dari jumlah titik historis agar konsisten dengan estimasi varians model regresi yang tidak bias.
2) **MAE** dihitung sebagai perbedaan absolut rata-rata antara nilai yang dipasang oleh model regresi (perkiraan satu langkah lebih maju dalam sampel), dan data historis yang diamati.
3) **MAPE** adalah perbedaan persentase absolut rata-rata antara nilai yang dipasang oleh model regresi dan nilai data yang diamati ing-statistical-details).

**Semakin kecil** nilai RMSE, MAE, dan MAPE yang dihasilkan, berarti model regresi **semakin akurat** dalam memprediksi harga sewa unit apartemen sesuai dengan limitasi fitur yang digunakan. 

Selain itu, kita juga bisa menggunakan nilai *R-squared* atau *adj. R-squared* jika model regresi yang nanti terpilih sebagai final model adalah model **linear**. Nilai *R-squared* digunakan untuk mengetahui seberapa baik model regresi dapat merepresentasikan varians keseluruhan data. Semakin nilai *R-squared* mendekati 1, maka semakin *fit* pula model regresinya terhadap data observasi. Namun, metrik evaluasi ini **tidak valid** jika model yang terpilih adalah model **non-linear**.

## **Data Understanding**

- Dataset merupakan data listing *Daegu* Apartemen
- Setiap baris data merepresentasikan informasi terkait Apartemen dan harga sewa yang sudah ada

**Attributes Information**

| **Attribute** | **Tipe Data** | **Deskripsi Data** |
| --- | --- | --- |
| HallwayType | Object | Tipe-tipe *hallway* |
| TimeToSubway | Object | Rentang waktu dari Apartemen ke stasiun |
| SubwayStation | Object | Nama stasiun subway terdekat |
| N_FacilitiesNearBy(ETC) | Float64 | Jumlah gedung/fasilitas lain yang dekat dari Apartemen |
| N_FacilitiesNearBy(PublicOffice) | Float64 | Jumlah gedung perkantoran yang dekat dari Apartemen |
| N_SchoolNearBy(University) | Float64 | Jumlah universitas yang dekat dari Apartemen |
| N_Parkinglot(Basement) | Float64 | Jumlah parkir *basement* yang ada di Apartemen |
| YearBuilt | Integer64 | Tahun berapa Apartemen itu dibangun |
| N_FacilitiesInApt | Integer64 | Jumlah fasilitas yang ada di dalam Apartemen |
| Size(sqf) | Integer64 | Luas Apartemen |
| SalePrice	 | Integer64 | Harga sewa unit Apartemen per bulan |

## **Conclusion**

Dari hasil modeling tersebut, bisa kita tarik kesimpulan sebagai berikut:

1. Model terbaik untuk dataset *Daegu* apartemen yang digunakan untuk memprediksi harga sewa suatu unit apartemen di *Daegu* adalah **Random Forest Regressor** dengan nilai MAPE sebesar 19.3%.
2. Setelah kita menggunakan *hyperparameter tuning* untuk model *random forest regressor*, ternyata hasil tuningnya membuat performa model sedikit meningkat untuk semua nilai RMSE, MAE, dan juga MAPE dibandingkan dengan sebelum dituning.
3. 5 Fitur yang paling berpengaruh terhadap memprediksikan harga sewa unit apartemen di *Daegu* adalah *HallwayType* (*terraced*), *Size (Squared Feet)*, *N_Parkinglot(Basement)* (Jumlah parkir *basement*), *YearBuilt* (tahun kapan apartemen itu dibangun), dan *N_FacilitiesNearBy(ETC)* (Jumlah gedung/fasilitas yang lain yang berdekatan di apartemen tersebut).
4. Jika ditinjau dari nilai MAPE yang dihasilkan oleh model sebelum dilakukan *hyperparameter tuning*, nilai MAPE yang didapatkan sebesar 19.3%, kita dapat menyimpulkan bahwa bila nanti model yang kita buat ini digunakan untuk memprediksikan harga sewa unit apartemen di *Daegu* ini menyimpang (meleset) dari *actual rent price* sebesar 19.3%.
5. Dengan proporsi 80% *training data* dan 20% *testing data*, dan juga berdasarkan dari hasil nilai MAPE tersebut, model tersebut sudah dibilang cukup bagus untuk memprediksi harga sewa unit apartemen di *Daegu*.

## **Recommendation**

Hal-hal yang bisa dilakukan untuk meng-*improve* harga sewa unit apartemen di *Daegu* adalah sebagai berikut:

1. Jika memungkinkan, pertimbangkan menambahkan fitur fitur seperti "jumlah keamanan apartemen", "lantai berapa unit itu ditempatkan", dan fitur lainnya yang bisa berdampak langsung terhadap peningkatan maupun penurunan harga sewa unit.
2. Jika bisa, untuk fitur "N_FacilitiesInApt" bisa kita *breakdown* menjadi fitur fitur yang baru seperti fitur "jumlah kamar tidur", "jumlah kamar mandi", "jumlah AC (*Air Conditioner*)", dan fitur yang bisa kita *breakdown* dari fitur tersebut untuk dapat meningkatkan akurasi model prediksi harga sewa apartemen.
3. Pertimbangkan menggunakan *GridSearchCV* sebagai tuning model tersebut. Bisa saja hasil tuningnya lebih bagus atau bisa saja lebih buruk dibandingkan dengan *RandomizedSearchCV*.
4. Perluas dataset dengan mengumpulkan data yang lebih terkini dan informatif terkait harga sewa apartemen di Daegu, Korea Selatan. Model regresi ini diharapkan dapat lebih memahami pola dalam data, sehingga pada akhirnya meningkatkan akurasi prediksi.
5. Untuk *stakeholder*, rumuskan strategi pemasaran yang menyasar fitur-fitur properti yang berpengaruh signifikan terhadap peningkatan harga sewa apartemen supay mendapatkan keuntungan secara maksimal.
6. Terapkan model *machine learning* yang lebih canggih untuk membuat prediksi harga sewa apartemen. Meskipun model yang lebih kompleks dapat memberikan hasil yang lebih akurat, perlu diingat bahwa kompleksitas model tersebut juga dapat menghambat pemahaman terhadap model yang dihasilkan.

## **Limitasi Model**

1. Model ini hanya bisa memprediksikan harga sewa unit apartemen dari rentang 32743 won sampai dengan 530973 won, nilai selain dari rentang tersebut tidak bisa diprediksi.
2. Model ini hanya berlaku untuk harga sewa apartemen di *Daegu* saja, untuk di wilayah lain bisa saja berbeda untuk menentukan prediksi harga sewanya.
3. Model ini perlu dilakukan *maintenance* secara berkala.

## **Note**

1. Untuk lebih jelasnya ada di notebook (ipynb).
2. Anda boleh melakukan modifikasi notebook saya jika diinginkan.

## **Cara Membuka Streamlit Deployment**

1. Cek requirements.txt, jika belum ada maka anda harus menginstall terlebih dahulu.
    - Contoh: Jika anda belum mempunyai library scikit learn, maka caranya adalah: buka command prompt, lalu ketik "python -m venv sklearn-env", lalu "sklearn-env\Scripts\activate", dan "pip install -U scikit-learn".
2. Jika library sudah terinstall, download "apps.py" dan "RF_Model_Daegu_Apartment"
3. Jika sudah didownload, maka buka command prompt, ketik "cd path kedua file yang sudah kalian download". Setelah itu, ketik "streamlit run apps.py"
4. Streamlit sudah bisa anda deploy!
