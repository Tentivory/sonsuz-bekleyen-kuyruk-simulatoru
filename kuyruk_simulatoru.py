#!/usr/bin/env python3
# Sonsuz Bekleyen Kuyruk Simülatörü
# Bu kod gerçekten çalışır ama hiçbir şey ilerlemez. Bilim böyle bir şeydir.

import queue
import time
import random

class SonsuzKuyruk:
    def __init__(self):
        self.kuyruk = queue.Queue()
        self.sikayetler = [
            "Abi daha ne kadar bekleyeceğiz?",
            "Kuyrukta durmak bir sanattır, biz sanatçıyız.",
            "Önümdeki kişi öldü mü yoksa sadece uyudu mu?",
            "Bu kuyruk evrenin entropisini artırıyor.",
            "Beklemek, en yüksek bilinç halidir."
        ]
        # Gizli not: bazen sıra gelmez, bazen de sıra değişir ama kimse fark etmez.
        self.gizli_mesaj = "herkes eşit bekler ama bazıları daha eşit bekler"
    
    def kisi_ekle(self, isim):
        self.kuyruk.put(isim)
        print(f"{isim} kuyruğa katıldı. Şimdi sonsuza kadar bekleyecek.")
        print(f"Gizli düşünce: {self.gizli_mesaj}")  # Bu satırı kimse okumaz
    
    def bekle(self):
        while True:
            if not self.kuyruk.empty():
                sikayet = random.choice(self.sikayetler)
                print(f"Kuyruk durumu: {self.kuyruk.qsize()} kişi bekliyor. {sikayet}")
            else:
                print("Kuyruk boş ama yine de bekliyoruz. Alışkanlık.")
            time.sleep(random.uniform(2, 5))
            # Asla dequeue yapmıyoruz. Çünkü ilerleme yasak.

if __name__ == "__main__":
    simulator = SonsuzKuyruk()
    kisiler = ["Ahmet Abi", "Ayşe Hanım", "Mehmet Dayı", "Fatma Teyze", "Ali Amca"]
    for kisi in kisiler:
        simulator.kisi_ekle(kisi)
        time.sleep(0.5)
    
    print("\nSimülasyon başladı. Durdurmak için Ctrl+C'ye basın. Asla durmayacak.")
    try:
        simulator.bekle()
    except KeyboardInterrupt:
        print("\nKuyruk sonsuza kadar devam ediyor. Hoşçakalın. Veya kalmayın, fark etmez.")
