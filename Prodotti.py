import csv
class Prodotto:
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
    def calcola_valore(self):
        return self.prezzo * self.quantita
class Magazzino:
    def __init__(self):
        self.prodotti = []
    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)
    def rimuovi_prodotto(self, nome_prodotto):
        for prodotto in self.prodotti:
            if prodotto.nome == nome_prodotto:
                self.prodotti.remove(prodotto)
                print(f"Prodotto '{nome_prodotto}' rimosso dal magazzino.")
                return
        print(f"Prodotto '{nome_prodotto}' non trovato nel magazzino.")
    def valore_totale(self):
        valore = 0
        for prodotto in self.prodotti:
            valore += prodotto.calcola_valore()
        return valore
    def salva_su_file(self, nome_file):
        with open(nome_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Nome", "Prezzo €", "Quantità"])
            for prodotto in self.prodotti:
                writer.writerow([prodotto.nome, prodotto.prezzo, prodotto.quantita])
    def mostra_prodotti(self):
        if not self.prodotti:
            print("Il magazzino è vuoto.")
            return
        print("Prodotti nel magazzino:")
        for prodotto in self.prodotti:
            print(f"Nome: {prodotto.nome}, Prezzo: {prodotto.prezzo} €, Quantità: {prodotto.quantita}")
if __name__ == "__main__":
    magazzino = Magazzino()
    p1 = Prodotto(nome="Maglietta", prezzo=15.99, quantita=50)
    p2 = Prodotto(nome="Pantaloni", prezzo=29.99, quantita=30)
    magazzino.aggiungi_prodotto(p1)
    magazzino.aggiungi_prodotto(p2)
    magazzino.mostra_prodotti()
    print(f"Valore totale del magazzino: {magazzino.valore_totale():.2f} €")
    magazzino.rimuovi_prodotto("Maglietta")
    print(
        f"Valore totale del magazzino dopo la rimozione: {magazzino.valore_totale():.2f} €")
    magazzino.salva_su_file('inventario.csv')
