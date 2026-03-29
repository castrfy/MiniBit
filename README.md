🛰️ Minibit — Veri Sıkıştırma Paneli
Uzay araçlarına aktarım için veri sıkıştırma işlemi yapan bir uygulama. Python ve CustomTkinter ile oluşturuldu.

Önizleme
Minibit binlerce kilometre uzaklıktaki uzay araçlarına veri göndermek için kullanımı kolay bir arayüz sunar. Dosya yüklenir veya elle girilir, sıkıştırma yöntemi seçilir, sonuç görüntülenir ve bir sunucu adresi üzerinden araca iletilir.

Özellikler
📂 Dosya yükleme — cihazdan doğrudan .txt cosyalarını yüklemek
✏️ Elle giriş — elle metin kopyalayıp yapıştırabilmek
⚙️ Birçok Sıkıştırma Seçeneği — Durum gereksinimlerine göre en uygun seçeneği seçebilmek
📡 Uzay Aracına İletim — API sunucu adresi girip sıkıştırılmış verileri göndermek
Başlangıç:
Gereklilikler
Python 3.8+
customtkinter
pip install customtkinter
Uygulamayı Çalıştırma
python main.py
Make sure icon.ico is in the same directory as main.py.

Kullanım
Veri yükleme — Browse File alanını kullanarak .txt dosyas yüklenebilir veya manuel olarak elle veri girilebilir.
Sunucu adresi girme — Uzay aracının API adresi girilir ve Set API tuşu kullanılır.
Sıkıştırma yöntemi seçme Dropdown kutusundan istenen sıkıştırma yöntemi seçilir.
Compress Butonuna bas — Sıkıştırılan veri sonuç ekranında gözükür.
Deliver To Spacecraft Tuşunu kullan — Sıkıştırılan veriyi uzay aracına gönderir.
Proje Yapısı
MiniBit/
├── main.py        # Ana uygulama
├── icon.ico       # Uygulama ikonu
└── README.md
Yol Haritası
 Gerçek sıkıştırma algoritmaları entegre etmek.
 Sunucu transfer feedback'i eklemek (success/failure response from server)
 Farklı tür dosyaları desteklemek (.csv, .json, .bin)
 Sıkıştırma bilgilerini gösteren ekran oluşturmak.
 Gönderi geçmişi
Katkılar
Pull isteklerine açığız.

Lisans
MIT
