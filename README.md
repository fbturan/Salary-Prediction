# Doğrusal Regresyon ile Maaş Tahmini

Bu proje, bir veri bilimi uygulamasıdır. Amacı, çalışanların tecrübe (yıllar) bilgisine dayanarak maaşlarını tahmin etmektir. Bu projede, doğrusal regresyon yöntemi kullanılarak bir tahmin modeli oluşturulmuştur.

## Kullanılan Kütüphaneler

- pandas: Veri setini okumak ve işlemek için kullanıldı.
- matplotlib.pyplot: Verilerin görselleştirilmesi için kullanıldı.
- sklearn.model_selection.train_test_split: Veri setini eğitim ve test setlerine ayırmak için kullanıldı.
- sklearn.linear_model.LinearRegression: Doğrusal regresyon modelinin oluşturulması ve eğitilmesi için kullanıldı.

## Veri Seti

Veri seti, "YearsExperience" (deneyim yılları) ve "Salary" (maaş) özelliklerinden oluşan bir CSV dosyasından okundu. Bu özellikler, bağımsız ve bağımlı değişkenler olarak sırasıyla kullanıldı.

## Model Oluşturma ve Değerlendirme

Veri seti, %80 eğitim ve %20 test setleri olarak ayrıldı. Ardından, doğrusal regresyon modeli eğitildi ve test seti üzerinde değerlendirildi.

## Projeyi Çalıştırma

Projeyi çalıştırmak için Python 3 ve gerekli kütüphanelerin yüklü olması gerekmektedir. Daha sonra, `salary_pre.py` dosyasını çalıştırarak modeli eğitebilir ve sonuçları görselleştirebilirsiniz.

