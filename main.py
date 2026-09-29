"""
AEGIS-X FINAL - main.py
Tüm sistemin final noktası. Karargah ekranı simülasyonunu başlatır.
"""

import sys
import os
import time
from rich.console import Console

sys.path.insert(0, os.path.dirname(__file__))

from src.crypto_handler import get_encrypted_payload, simulate_decryption
from src.c2_dashboard import display_dashboard

def main():
    console = Console()
    
    # 1. Bekleme ekranı
    console.print("[bold cyan][*] Karargah dinleme modu aktif. Ufuk hatti taranıyor...[/bold cyan]")
    time.sleep(2)
    
    # 2. Sinyal yakalama
    console.print("\n[bold yellow][!] DIKKAT: Jammer sınırından bilinmeyen bir 'BURST' sinyali yakalandı![/bold yellow]")
    time.sleep(1.5)
    
    encrypted_data = get_encrypted_payload()
    console.print(f"[dim]Kriptolu Ham Veri: {encrypted_data}[/dim]\n")
    time.sleep(1)
    
    # 3. Kripto Çözümü
    console.print("[bold red][+] Kaynak Dogrulandı: AEGIS-X KUS-1 (Kurye Drone).[/bold red]")
    console.print("[bold red][+] Istihbarat paketi cozumleniyor (AES-256 Key Match)...[/bold red]")
    simulate_decryption(console)
    
    console.print("\n[bold green][+] SIFRE COZULDU. ISTIHBARAT RAPORU EKRANA YANSITILIYOR...[/bold green]\n")
    time.sleep(1.5)
    
    # 4. Ana Ekran
    display_dashboard(console)

if __name__ == "__main__":
    main()
