"""
AEGIS-X FINAL - c2_dashboard.py
Komutanın göreceği Karargah İstihbarat (C2 - Command & Control) Arayüzü.
Gelen gerçek JSON verisini ekrana basar.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

def display_dashboard(console, decrypted_data):
    """Şifre çözüldükten sonra gerçek JSON verisini ekrana basar."""
    
    # Başlık
    console.print(Panel(
        Text("AEGIS-X MÜŞTEREK HAREKAT VE İSTİHBARAT MERKEZİ", justify="center", style="bold green"),
        style="green"
    ))
    
    # Hedef Tablosu
    source_name = decrypted_data.get("source", "BİLİNMEYEN KAYNAK")
    table = Table(title=f"{source_name} İSTİHBARAT RAPORU", show_header=True, header_style="bold magenta")
    table.add_column("HEDEF TİPİ", style="cyan", justify="left")
    table.add_column("KOORDİNAT (GPS)", style="yellow", justify="center")
    table.add_column("DURUM / AKSİYON", style="green", justify="left")
    
    # Gerçek Hedefleri (S-400, Jammer) döngüyle bas
    for tgt in decrypted_data.get("targets", []):
        table.add_row(
            tgt["type"], 
            f"LAT: {tgt['lat']}, LON: {tgt['lon']}", 
            f"[red]TESPİT EDİLDİ.[/red] {tgt['lock']} Lazer Kilitli."
        )
        
    # Sahte Hedefleri (Decoy) döngüyle bas
    for decoy in decrypted_data.get("decoys", []):
        table.add_row(
            decoy["type"], 
            f"LAT: {decoy['lat']}, LON: {decoy['lon']}", 
            f"[blue]YOKSAYILDI.[/blue] {decoy['reason']}."
        )

    console.print(table)
    
    # Sonuç Paneli
    summary = """
[bold green][+] SÜRÜ OPERASYONU BAŞARILI.[/bold green]
Elektronik Harp bölgesi (Jammer) içerisindeki tüm hedefler otonom olarak 
bulunmuş, sahte hedefler yapay zeka ile elenmiş ve telsiz üzerinden şifreli aktarılmıştır.

[bold red]>>> VURUŞ ONAYI BEKLENİYOR...[/bold red]
    """
    console.print(Panel(summary, title="OPERASYON SONUCU", border_style="red"))
