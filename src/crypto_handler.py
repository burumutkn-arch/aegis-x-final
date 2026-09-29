"""
AEGIS-X FINAL - crypto_handler.py
GERÇEK AES Şifreleme Modülü. 
Bu kod donanıma (Drone ve Karargah) yüklendiğinde, veriyi gerçekten kriptolar.
"""

import json
from cryptography.fernet import Fernet

# GERÇEK BİR AES ANAHTARI ÜRETİMİ
# Gerçek bir operasyonda bu anahtar uçuştan önce drone'a ve karargaha fiziksel olarak yüklenir (Pre-Shared Key).
SECRET_KEY = Fernet.generate_key()
cipher_suite = Fernet(SECRET_KEY)

def generate_real_drone_payload():
    """Drone'un jammer'dan çıkınca oluşturacağı GERÇEK JSON istihbarat verisi."""
    drone_data = {
        "source": "AEGIS-X KUS-1 (Kurye)",
        "targets": [
            {"type": "S-400 (Batarya)", "lat": 39.851, "lon": 33.420, "lock": "KUS-3"},
            {"type": "KRASUKHA-4 (Jammer)", "lat": 39.865, "lon": 33.411, "lock": "KUS-5"}
        ],
        "decoys": [
            {"type": "SAHTE HEDEF (Decoy)", "lat": 39.890, "lon": 33.390, "reason": "Termal isi yok"}
        ]
    }
    
    # 1. Veriyi JSON string'e çevir
    json_str = json.dumps(drone_data)
    
    # 2. GERÇEK AES ile şifrele (Bytes formatına çevrilir)
    encrypted_bytes = cipher_suite.encrypt(json_str.encode('utf-8'))
    return encrypted_bytes

def decrypt_payload(encrypted_bytes):
    """Karargahın telsizden gelen şifreli veriyi AES Anahtarı ile çözdüğü GERÇEK fonksiyon."""
    # Şifreyi çöz
    decrypted_bytes = cipher_suite.decrypt(encrypted_bytes)
    # Geri JSON (Dictionary) objesine çevir
    json_str = decrypted_bytes.decode('utf-8')
    return json.loads(json_str)
