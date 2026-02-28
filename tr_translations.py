#!/usr/bin/env python3
"""Turkish translations for breed pages - fixing mixed English/Turkish text."""

# Fix partial translations - replace broken mixed-language text with proper Turkish
FIXES = {
    # === ANA SAYFAS FIXES (mistranslation of "Homes") ===
    "Ana Sayfas with yards": "Bahçeli evler",
    "Ana Sayfas with space": "Geniş evler",
    "Ana Sayfas with children": "Çocuklu evler",
    "Ana Sayfas with older children": "Büyük çocuklu evler",
    "Ana Sayfas with young children": "Küçük çocuklu evler",
    "Ana Sayfas with rough children": "Sert oyun oynayan çocuklu evler",
    "Ana Sayfas with toddlers": "Yürümeye yeni başlayan çocuklu evler",
    "Ana Sayfas with secure yards": "Güvenli bahçeli evler",
    "Ana Sayfas with small pets": "Küçük evcil hayvanlı evler",
    "Ana Sayfas with small pets (prey drive)": "Küçük evcil hayvanlı evler (av güdüsü)",
    "Ana Sayfas with small pets (high prey drive)": "Küçük evcil hayvanlı evler (yüksek av güdüsü)",
    "Ana Sayfas with other köpeks": "Diğer köpekli evler",
    "Ana Sayfas with many stairs": "Çok merdiveni olan evler",
    "Ana Sayfas near water": "Su yakınındaki evler",
    "Ana Sayfas without small children": "Küçük çocuksuz evler",
    "Ana Sayfas without small pets": "Küçük evcil hayvansız evler",
    
    # === AKTIF FAMILIES/HOUSEHOLDS ===
    "Aktif families with children": "Çocuklu aktif aileler",
    "Aktif families with older children": "Büyük çocuklu aktif aileler",
    "Aktif families": "Aktif aileler",
    "Aktif households": "Aktif haneler",
    "Aktif individuals": "Aktif bireyler",
    "Aktif seniors": "Aktif yaşlılar",
    "Very aktif households": "Çok aktif haneler",
    "Very aktif outdoor families": "Çok aktif açık hava aileleri",
    "Very aktif sahipler": "Çok aktif sahipler",
    
    # === BUSY/SESSIZ HOUSEHOLDS ===
    "Busy households": "Meşgul haneler",
    "sessiz households": "Sessiz haneler",
    
    # === EXPERIENCED SAHIPLER ===
    "Experienced sahipler": "Deneyimli sahipler",
    
    # === FAMILIES ===
    "Families": "Aileler",
    "Aileler ile older children": "Büyük çocuklu aileler",
    
    # === DAIRE SAKINLERI ===
    "Daire sakinleri (with exercise)": "Daire sakinleri (egzersizle)",
    
    # === SOĞUK IKLIMLER ===
    "Soğuk iklimler without protection": "Korumasız soğuk iklimler",
    
    # === SABIRLI SAHIPLER ===
    "Sabırlı sahipler who can handle drool and hair": "Salya ve tüyü kaldırabilecek sabırlı sahipler",
    
    # === İSTEYEN KIŞILER FIXES (malformed "Those wanting" translations) ===
    "İsteyen kişiler adanmış dost": "Adanmış bir arkadaş isteyenler",
    "İsteyen kişiler adanmış guardian": "Adanmış bir koruyucu isteyenler",
    "İsteyen kişiler arkadaş canlısı dost": "Dost canlısı bir arkadaş isteyenler",
    "İsteyen kişiler arkadaş canlısı ırk": "Dost canlısı bir ırk isteyenler",
    "İsteyen kişiler dost canlısı ırk": "Dost canlısı bir ırk isteyenler",
    "İsteyen kişiler eğitilebilir ırk": "Eğitilebilir bir ırk isteyenler",
    "İsteyen kişiler fluffy köpek": "Tüylü bir köpek isteyenler",
    "İsteyen kişiler guardian": "Koruyucu isteyenler",
    "İsteyen kişiler heybetli dost": "Heybetli bir arkadaş isteyenler",
    "İsteyen kişiler koruyucu köpek": "Koruyucu bir köpek isteyenler",
    "İsteyen kişiler mutlu dost": "Mutlu bir arkadaş isteyenler",
    "İsteyen kişiler mutlu ırk": "Mutlu bir ırk isteyenler",
    "İsteyen kişiler nazik giant": "Nazik bir dev isteyenler",
    "İsteyen kişiler oyuncu dost": "Oyuncu bir arkadaş isteyenler",
    "İsteyen kişiler quiet köpek": "Sessiz bir köpek isteyenler",
    "İsteyen kişiler sadık dost": "Sadık bir arkadaş isteyenler",
    "İsteyen kişiler sakin Japonyaese ırk": "Sakin bir Japon ırkı isteyenler",
    "İsteyen kişiler sakin terrier": "Sakin bir terrier isteyenler",
    "İsteyen kişiler sessiz dost": "Sessiz bir arkadaş isteyenler",
    "İsteyen kişiler trainable toy köpek": "Eğitilebilir bir oyuncak köpek isteyenler",
    "İsteyen kişiler unique ırk": "Benzersiz bir ırk isteyenler",
    "İsteyen kişiler unique, ancient ırk": "Benzersiz, kadim bir ırk isteyenler",
    "İsteyen kişiler çok yönlü köpek": "Çok yönlü bir köpek isteyenler",
    "İsteyen kişilern hevesli-to-please köpek": "Hoşnut etmeye hevesli bir köpek isteyenler",
    "İsteyen kişilern uyanık dost": "Uyanık bir arkadaş isteyenler",
    "İsteyen sahipler a sakin köpek": "Sakin bir köpek isteyen sahipler",
    "İsteyenler off-leash reliability": "Tasmasız güvenilirlik isteyenler",
    
    # === TAKDIR EDENLER FIXES ===
    "Takdir edenler an bağımsız köpek": "Bağımsız bir köpeği takdir edenler",
    "Takdir edenler elegant, bağımsız köpeks": "Zarif, bağımsız köpekleri takdir edenler",
    "Takdir edenler rare ırks": "Nadir ırkları takdir edenler",
    
    # === SHOW KALITESINDE ===
    "Show kalitesinde terrier isteyenler": "Şov kalitesinde terrier isteyenler",
    
    # === DENEYIMLI BÜYÜK IRK SAHIPLERI (duplicate word fix) ===
    "Deneyimli büyük ırk sahipleri ırk sahipler": "Deneyimli büyük ırk sahipleri",
}

if __name__ == "__main__":
    print(f"Total Turkish fixes: {len(FIXES)}")
