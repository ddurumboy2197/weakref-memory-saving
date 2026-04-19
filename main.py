import weakref
import gc

class KattaObekt:
    def __init__(self, nom):
        self.nom = nom

    def __del__(self):
        print(f"{self.nom} obekti o'chirildi")

def main():
    katta_obektlar = weakref.WeakValueDictionary()

    for i in range(10):
        katta_obekt = KattaObekt(f"Obekt {i}")
        katta_obektlar[katta_obekt] = katta_obekt

    # Obektlar o'chirilishi uchun GC ni ishga tushuramiz
    gc.collect()

    # Obektlar o'chirilganmi yoki yo'qmi tekshiramiz
    for key in katta_obektlar:
        print(f"{key.nom} obekti mavjudmi: {key is not None}")

if __name__ == "__main__":
    main()
