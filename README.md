# Python-Exe
# Excel Veri Çekme ve Birleştirme Aracı

Bu Python skripti, belirtilen bir klasördeki Excel dosyalarından belirli sütunlardaki verileri çeker ve bunları tek bir Excel dosyasında birleştirir. Bu araç, özellikle birden çok Excel dosyasında aynı yapıda veri bulunan senaryolarda kullanışlıdır.

## Kullanım

1. **Gereksinimler:**
   - Python yüklü olmalıdır.
   - Gerekli Python paketleri yüklenmelidir: `pip install pandas`

2. **Kodun Çalıştırılması:**
   - `Çoklu excelden veri çekme.py` dosyasını çalıştırarak programı başlatabilirsiniz.
   - Skript, belirtilen klasördeki tüm Excel dosyalarını tarayacak ve 'D' sütunundaki verileri birleştirerek yeni bir Excel dosyasına kaydedecektir.

3. **Çıktı:**
   - Programın çıktısı, konsol ekranında ilerleme durumunu gösterir.
   - Toplanan veriler, 'Toplam_Veri.xlsx' adlı yeni bir Excel dosyasında saklanır.

4. **Hata Durumları:**
   - Eğer bir dosyada 'D' sütunu bulunamazsa veya dosya okunamazsa, ilgili hata mesajı konsola yazdırılır.

## Notlar

- Skriptin düzgün çalışabilmesi için işlenecek Excel dosyalarının aynı yapıda olması önemlidir.
- Herhangi bir hata durumunda, konsol çıktısını kontrol etmek faydalı olabilir.
