from yorum_kaynak import yorumlari_getir
from ozetleyici import ozet_cikar

url = "https://www.hepsiburada.com/16-24-ay-temel-setler-kolisi-p-HBCV00006JTPUV"
API_KEY = "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"  # ← OpenRouter API anahtarını buraya yaz

yorumlar = yorumlari_getir(url)

if not yorumlar:
    print("Yorum bulunamadı.")
    exit()

print(f"{len(yorumlar)} yorum alındı. Özetleniyor...")

ozet = ozet_cikar(API_KEY, yorumlar)

if ozet:
    print("Yorum Özeti:\n", ozet)
    with open("ozet.txt", "w", encoding="utf-8") as f:
        f.write(ozet)
