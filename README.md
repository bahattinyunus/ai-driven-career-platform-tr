# 🇹🇷 İŞKUR Next - Yeni Nesil İstihdam ve Kariyer Platformu

![İŞKUR Next Banner](static/img/banner.png)

[![Durum](https://img.shields.io/badge/Durum-Aktif%20Geliştirme-blue?style=for-the-badge&logo=git)](https://github.com/bahattinyunus/opensource-job-portal)
[![Sürüm](https://img.shields.io/badge/Sürüm-v2.0.0-green?style=for-the-badge)](https://github.com/bahattinyunus/opensource-job-portal/releases)
[![Lisans](https://img.shields.io/badge/Lisans-MIT-orange?style=for-the-badge)](LICENSE)

> **Vizyonumuz:** Türkiye'nin istihdam piyasasını, LinkedIn standartlarında modern, sosyal ve yapay zeka destekli bir ekosisteme dönüştürmek. **"Sadece iş bulma değil, kariyer inşa etme yeri."**

---

## 🚀 Proje Hakkında

**İŞKUR Next**, klasik iş arama portallarının ötesine geçerek, adaylar ve işverenler arasında etkileşimi artıran, **"Premium Government Tech"** felsefesiyle tasarlanmış, devlet destekli yeni nesil bir kariyer platformudur.

Bu proje, açık kaynaklı `PeelJobs` altyapısı üzerine inşa edilmiş olup, Türk iş kültürüne ve modern web standartlarına (Django 5, Tailwind CSS v4) göre tamamen yeniden yazılmıştır.

### 🌟 Neden İŞKUR Next?

1.  **Modern ve Prestijli Tasarım:** Devlet ciddiyeti ile özel sektör dinamizmini birleştiren "Glassmorphism" arayüz.
2.  **Sosyal Kariyer Ağı:** İş arayanlar sadece CV bırakmaz; gönderi paylaşır, network kurar ve etkileşime girer.
3.  **Akıllı Eşleşme (AI):** Adayları doğru işlerle, işverenleri en uygun yeteneklerle nokta atışı buluşturur.
4.  **Yerelleştirilmiş Deneyim:** Tamamen Türkçe, Türkiye'nin 81 iline ve yerel sektör dinamiklerine uygun altyapı.

---

## 🎨 Tasarım Felsefesi: "Premium Public Tech"

Kullanıcı deneyimi (UX), sadece estetik değil, bir saygınlık meselesidir. **İŞKUR Next**, devlet hizmetlerinin soğuk ve bürokratik yüzünü yıkarak; güven veren, modern ve akıcı bir arayüz sunar.

*   **Glassmorphism Estetiği:** Şeffaf katmanlar, bulanıklık efektleri ve canlı renk geçişleri ile derinlik ve hiyerarşi hissi yaratılır.
*   **Mikro-Etkileşimler:** Butonlar, kartlar ve geçişlerdeki ince animasyonlar, kullanıcıya "canlı" bir sistemde olduğu hissini verir.
*   **Tipografi Odaklılık:** Okunabilirliği artıran, modern font aileleri ile içerik ön plana çıkarılır.


---

## 🛠 Teknoloji Yığını (Tech Stack)

Proje, yüksek performans, güvenlik ve ölçeklenebilirlik için en güncel teknolojileri kullanır:

| Alan | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **Backend** | ![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white) | Güçlü ve güvenli sunucu tarafı mimarisi. |
| **Frontend** | ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.0-38B2AC?logo=tailwind-css&logoColor=white) | Modern, responsive ve özelleştirilebilir arayüz. |
| **Veritabanı** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white) | İlişkisel veri ve JSON desteği. (Localde SQLite) |
| **Arama** | ![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.17-005571?logo=elasticsearch&logoColor=white) | Hızlı ve ilgili sonuçlar için tam metin arama motoru. |
| **Asenkron** | ![Celery](https://img.shields.io/badge/Celery-5.5-37814A?logo=celery&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-6.2-DC382D?logo=redis&logoColor=white) | Arka plan görevleri ve önbellekleme. |

---

## � Güvenlik ve Altyapı

Bir devlet projesi ciddiyetiyle, verileriniz en üst düzey güvenlik protokolleriyle korunur.

*   **Uçtan Uca Şifreleme:** Hassas kullanıcı verileri AES-256 standardında şifrelenerek saklanır.
*   **RBAC (Rol Tabanlı Erişim):** İşveren, Aday ve Yönetici yetkileri kesin çizgilerle ayrılmıştır; kimse görmemesi gereken veriye erişemez.
*   **Rate Limiting:** API endpoint'leri, kötü niyetli saldırılara (DDoS) karşı korumalıdır.
*   **Dockerize Yapı:** Proje, konteyner mimarisi sayesinde her ortamda (Dev/Test/Prod) aynı kararlılıkla çalışır.

---

## ⚡ Performans ve Ölçeklenebilirlik

Sistem, yüksek trafik altında bile minimum gecikme (latency) ile yanıt verecek şekilde optimize edilmiştir.

*   **Load Balancing (Yük Dengeleme):** Gelen trafik, Nginx üzerinden birden fazla uygulama sunucusuna dağıtılır.
*   **Database Partitioning:** Büyük veri setleri için veritabanı bölümleme stratejileri uygulanmıştır.
*   **CDN Entegrasyonu:** Statik dosyalar (CSS, JS, Görseller) dünya genelindeki sunuculardan (CDN) servis edilerek yüklenme hızı maksimize edilir.



---

## �🔥 Temel Özellikler

### 1. Sosyal Ağ (Yeni!)
*   **Akış (Feed):** Bağlantılarınızın ve takip ettiğiniz firmaların güncellemelerini, makalelerini ve başarılarını görün.
*   **Bağlantı Kurma:** Sektördeki profesyonellerle iletişime geçin, ağınızı genişletin.
*   **Etkileşim:** Gönderileri beğenin, yorum yapın ve paylaşarak görünürlüğünüzü artırın.

### 2. Gelişmiş İş Arama
*   **Akıllı Filtreler:** Konum, yetenek, deneyim yılı ve çalışma şekline (hibrit/uzaktan) göre detaylı arama.
*   **Harita Bazlı Arama:** Size en yakın iş fırsatlarını harita üzerinde görüntüleyin.

### 3. Aday Odaklı Profil
*   **Canlı İstatistikler:** Profilinizin kaç kez görüntülendiğini ve başvurularınızın durumunu anlık takip edin.
*   **Portfolyo Yönetimi:** Projelerinizi, sertifikalarınızı ve yeteneklerinizi sergileyin.

---

## 💻 Kurulum ve Geliştirme

Projeyi yerel ortamınızda ayağa kaldırmak için aşağıdaki adımları izleyin.

### Gereksinimler
*   Python 3.10+
*   Git

### Adım Adım Kurulum

1.  **Repoyu Klonlayın:**
    ```bash
    git clone https://github.com/bahattinyunus/opensource-job-portal.git
    cd opensource-job-portal
    ```

2.  **Sanal Ortam Oluşturun ve Aktif Edin:**
    ```bash
    python -m venv venv
    # Windows için:
    venv\Scripts\activate
    # Linux/Mac için:
    source venv/bin/activate
    ```

3.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Veritabanını Hazırlayın:**
    *Proje yerel geliştirme için varsayılan olarak SQLite kullanacak şekilde ayarlanmıştır.*
    ```bash
    python manage.py migrate
    ```

5.  **Örnek Veri ve Süper Kullanıcı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Sunucuyu Başlatın:**
    ```bash
    python manage.py runserver
    ```
    Tarayıcınızda `http://127.0.0.1:8000/` adresine gidin.

---

## 🌍 Evrensel Erişim (Accessibility)

Teknoloji herkes içindir. İŞKUR Next, engelsiz bir deneyim sunmayı taahhüt eder.

*   **WCAG 2.1 Uyumu:** Görme engelli vatandaşlarımız için ekran okuyucu (Screen Reader) tam desteği.
*   **Yüksek Kontrast Modu:** Görme güçlüğü çekenler için özel renk paleti seçenekleri.
*   **Klavye Navigasyonu:** Fare kullanmadan, sadece klavye ile tüm sitede gezinebilme özgürlüğü.

---

## 🤖 Etik Yapay Zeka İlkeleri

Yapay zeka algoritmalarımızda **şeffaflık**, **adil kullanım** ve **hesap verebilirlik** esastır.

*   **Önyargı Karşıtlığı (Anti-Bias):** Algoritmalar, cinsiyet, yaş veya etnik kökene dayalı ayrımcılık yapmayacak şekilde eğitilir.
*   **Açıklanabilirlik (XAI):** "Neden bu iş bana önerildi?" sorusunun cevabı kullanıcılara şeffaf bir şekilde sunulur.
*   **Veri Mahremiyeti:** AI modelleri eğitilirken kişisel veriler anonimleştirilir (GDPR/KVKK uyumlu).

---

## 📊 Teknolojik Hazırlık Seviyesi (TRL)

Projemiz, **TRL 7 - Gerçek Ortamda Sistem Prototipi Gösterimi** seviyesindedir.

> **Mevcut Durum:** Tüm temel fonksiyonlar (iş arama, başvuru, profil oluşturma, sosyal akış) entegre edilmiş ve gerçekçi veri setleriyle stres testlerinden başarıyla geçmiştir.



---

## 🗺 Yol Haritası (Roadmap)

- [x] **Faz 1:** Marka Dönüşümü ve Altyapı Hazırlığı (Tamamlandı)
- [x] **Faz 2:** Modern UI/UX Tasarımı (Tamamlandı)
- [x] **Faz 3:** Temel Sosyal Özellikler (Feed, Bağlantılar) (Tamamlandı)
- [ ] **Faz 4:** Gelişmiş Özellikler (Planlanan)
    - [ ] WebSockets ile Anlık Mesajlaşma
    - [ ] Video Özgeçmiş (Video Resume)
    - [ ] AI Tabanlı Mülakat Simülasyonu
    - [ ] Mobil Uygulama (React Native)

---

## 🤝 Katkıda Bulunma

Açık kaynak komünitesinin gücüne inanıyoruz! Katkıda bulunmak isterseniz:

1.  Bu repoyu **Fork** edin.
2.  Yeni bir özellik dalı (feature branch) oluşturun (`git checkout -b ozellik/HarikaOzellik`).
3.  Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik eklendi'`).
4.  Dalınızı Push edin (`git push origin ozellik/HarikaOzellik`).
5.  Bir **Pull Request** açın.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

## 👨‍💻 Proje Mimarı

**Bahattin Yunus Çetin**  
*IT Architect*

Trabzon, Of'ta üniversite eğitimine devam eden Bahattin Yunus Çetin, modern yazılım mimarileri ve ölçeklenebilir sistemler üzerine uzmanlaşmış bir **IT Architect** olarak çalışmalarını sürdürmektedir. Bu proje, kamu istihdam süreçlerine yenilikçi, profesyonel ve yüksek standartlarda bir yaklaşım getirmek amacıyla geliştirilmiştir.

[![GitHub](https://img.shields.io/badge/GitHub-Profil-181717?style=for-the-badge&logo=github)](https://github.com/bahattinyunus)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bağlantı_Kur-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/bahattinyunus/)
