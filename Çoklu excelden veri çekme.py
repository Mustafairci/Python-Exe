import os
import pandas as pd

# İlgili klasörü belirtin
klasor_yolu = r'C:\Users\Mustafa\Desktop\Yeni klasör (2)'

# Tüm Excel dosyalarını bul
excel_dosyalari = [dosya for dosya in os.listdir(klasor_yolu) if dosya.endswith('.xlsx') or dosya.endswith('.xls')]

# Toplanacak veriler için boş bir DataFrame oluştur
toplam_veri = pd.DataFrame()

# Her Excel dosyasını işle
for dosya_adi in excel_dosyalari:
    dosya_yolu = os.path.join(klasor_yolu, dosya_adi)
    
    try:
        # Excel dosyasını oku
        df = pd.read_excel(dosya_yolu)
        
        # 3. ve 4. sütunları bulmaya çalış
        if len(df.columns) >= 4:
            sutun_3 = df.iloc[:, 2]  # 3. sütun (0'dan başlayarak)
            sutun_4 = df.iloc[:, 3]  # 4. sütun (0'dan başlayarak)
            
            # Yeni DataFrame'e dosya adını ve sütunları ekle
            yeni_veri = pd.DataFrame({'Dosya Adı': [dosya_adi] * len(sutun_3),
                                      '3. Sütun Değerleri': sutun_3,
                                      '4. Sütun Değerleri': sutun_4})
            
            # Toplam veriye ekle
            toplam_veri = pd.concat([toplam_veri, yeni_veri], ignore_index=True)
        else:
            print(f"{dosya_adi} dosyasında en az 4 sütun bulunamadı.")
    except Exception as e:
        print(f"{dosya_adi} dosyasını okurken bir hata oluştu: {str(e)}")

# Sonuçları yeni bir Excel dosyasına yaz
cikti_yolu = os.path.join(klasor_yolu, 'Toplam_Veri.xlsx')
toplam_veri.to_excel(cikti_yolu, index=False)

print(f"İşlem tamamlandı. Sonuçlar '{cikti_yolu}' dosyasına yazıldı.")
