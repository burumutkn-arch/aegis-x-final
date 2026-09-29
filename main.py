"""
AEGIS-X FINAL - main.py
Tüm sistemin final noktası. Telsizden (Drone'dan) gelen GERÇEK 
AES şifreli veriyi yakalar, anahtarla çözer ve Karargah ekranına basar.
"""

import sys
import os
import time
from rich.console import Console

sys.path.insert(0, os.path.dirname(__file__))

from src.crypto_handler import generate_real_drone_payload, decrypt_payload
from src.c2_dashboard import display_dashboard

def main():
    console = Console()
    
    # 1. Bekleme ekranı
    console.print("[bold cyan][*] Karargah Radyo (RF) dinleme modu aktif. Ufuk hatti taranıyor...[/bold cyan]")
    time.sleep(2)
    
    # 2. Sinyal yakalama (DRONE BURADA GERÇEK VERİYİ ŞİFRELER VE YOLLAR)
    encrypted_bytes = generate_real_drone_payload()
    
    console.print("\n[bold yellow][!] DIKKAT: Jammer sınırından GERÇEK AES ŞİFRELİ bir 'BURST' sinyali yakalandı![/bold yellow]")
    # Gerçek şifreli byteları Base64'e çevirip ekranda gösterelim ki inandırıcı olsun
    console.print(f"[dim]Kriptolu Ham Veri (Bytes): {encrypted_bytes.decode('utf-8')[:100]}...[/dim]\n")
    time.sleep(2)
    
    # 3. Kripto Çözümü (KARARGAH ANAHTAR İLE ŞİFREYİ ÇÖZER)
    console.print("[bold red][+] Önceden paylaşılan (Pre-Shared) AES Anahtarı ile şifre çözülüyor...[/bold red]")
    time.sleep(2)
    
    try:
        decrypted_json_data = decrypt_payload(encrypted_bytes)
        console.print("[bold green][+] ŞİFRE BAŞARIYLA ÇÖZÜLDÜ. JSON VERİSİ AYRIŞTIRILDI.[/bold green]\n")
        time.sleep(1)
        
        # 4. Ana Ekranı Gerçek Veriyle Çiz
        display_dashboard(console, decrypted_json_data)
        
    except Exception as e:
        console.print(f"[bold red]ŞİFRE ÇÖZME HATASI (Yetkisiz Erişim): {e}[/bold red]")

if __name__ == "__main__":
    main()
