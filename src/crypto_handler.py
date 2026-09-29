"""
AEGIS-X FINAL - crypto_handler.py
Kuryeden (KUS-1) gelen AES-256 şifreli ham veriyi ve çözümleme (decryption) 
algoritmasını simüle eder.
"""

import time
import random

def get_encrypted_payload():
    """Havadan yakalanan sahte şifreli HEX verisi üretir."""
    chars = "0123456789ABCDEF"
    payload = ""
    for _ in range(8):
        block = "".join(random.choice(chars) for _ in range(16))
        payload += block + " "
    return payload.strip()

def simulate_decryption(console):
    """Şifre kırma (Brute-force / AES key) animasyonu."""
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        task1 = progress.add_task("[red]AES-256 Sifresi Cozuluyor...", total=100)
        
        while not progress.finished:
            time.sleep(0.04) # Simülasyon hızı
            progress.update(task1, advance=random.uniform(1, 4))
