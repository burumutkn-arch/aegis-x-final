"""
AEGIS-X FINAL - c2_dashboard.py
Komutanın göreceği Karargah İstihbarat (C2 - Command & Control) Arayüzü.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.layout import Layout
import time

def display_dashboard(console):
    """Şifre çözüldükten sonra ekrana basılacak ana askeri istihbarat raporu."""
    
    # Başlık
    console.print(Panel(
        Text("AEGIS-X MÜŞTEREK HAREKAT VE İSTİHBARAT MERKEZİ", justify="center", style="bold green"),
        style="green"
    ))
    
    time.sleep(1)
    
    # Hedef Tablosu
    table = Table(title="KUS-1 (KURYE) İSTİHBARAT RAPORU", show_header=True, header_style="bold magenta")
    table.add_column("HEDEF TİPİ", style="cyan", justify="left")
    table.add_column("KOORDİNAT (GPS)", style="yellow", justify="center")
    table.add_column("DURUM / AKSİYON", style="green", justify="left")
    
    table.add_row(
        "S-400 (Batarya)", 
        "LAT: 39.851, LON: 33.420", 
        "[red]TESPİT EDİLDİ.[/red] KUS-3 ve KUS-4 Lazer Kilitli."
    )
    table.add_row(
        "KRASUKHA-4 (Jammer)", 
        "LAT: 39.865, LON: 33.411", 
        "[red]TESPİT EDİLDİ.[/red] KUS-5 ve KUS-6 Lazer Kilitli."
    )
    table.add_row(
        "SAHTE HEDEF (Decoy)", 
        "LAT: 39.890, LON: 33.390", 
        "[blue]YOKSAYILDI.[/blue] Termal ısı izi saptanmadı."
    )

    console.print(table)
    
    time.sleep(1)
    
    # Sonuç Paneli
    summary = """
[bold green][+] SÜRÜ OPERASYONU BAŞARILI.[/bold green]
Elektronik Harp bölgesi (Jammer) içerisindeki tüm hedefler otonom olarak 
bulunmuş, sahte hedefler yapay zeka ile elenmiş ve dışarıya sızdırılmıştır.

[bold red]>>> VURUŞ ONAYI BEKLENİYOR...[/bold red]
    """
    console.print(Panel(summary, title="OPERASYON SONUCU", border_style="red"))
