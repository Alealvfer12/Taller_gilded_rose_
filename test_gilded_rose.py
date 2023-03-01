# -*- coding: utf-8 -*-

import unittest

from gilded_rose import GildedRose, Item




class GildedRoseTest(unittest.TestCase):
    #EJEMPLO PRUEBA PROFE
    #def test_sell_in_decreases_by_one_every_day(self):
        #item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        #gilded_rose = GildedRose([item])
        #days = 3
        #for _ in range(days):
            #gilded_rose.update_quality()

        #self.assertEquals(7, item.sell_in)

#"REQUERIMIENTO La calidad nunca es negativa, se crea un articulo X"
    def test_quality_never_negative(self):
        items = [Item(name="itemX", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
   
#"REQUERIMIENTO "Aged Brie"
#"la calidad de "Aged Brie" aumenta a medida que envejece, hasta un máximo de 50"
def test_aged_brie_(self):
    item = Item(name="Aged Brie", sell_in=2, quality=0)
    gilded_rose = GildedRose([item])
  # Simular el paso de 3 días 
    for _ in range(3):
        gilded_rose.update_quality()
  #La calidad aumenta a 2 han pasado 3 días
  #La calidad debería haber aumentado en 3, pero como no puede superar 50, se detiene en un valor de 2.
    self.assertEquals(3, item.quality)
    self.assertEquals(2, item.quality)


#"REQUERIMIENTO la calidad de "Aged Brie" nunca es mayor a 50
def test_aged_brie_quality_never_more_than_50(self):
    item = Item(name="Aged Brie", sell_in=2, quality=0)
    gilded_rose = GildedRose([item])
    days = 5
    for _ in range(days):
        gilded_rose.update_quality()
    self.assertEqual(50, item.quality)

#"REQUERIMIENTO Sulfuras"
#Es un  artículo legendario y, como tal, su calidad es 80 y nunca se altera.
def test_sulfuras0(self):
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    gilded_rose = GildedRose([item])
    days = 5
    for _ in range(days):
        gilded_rose.update_quality()
        print(item.quality)

#"REQUERIMIENTO Backstage"
#La calidad aumenta en 2 cuando hay 10 días o menos y en 3 cuando hay 5 días o menos, 
#pero  la calidad cae a 0 después del concierto.

def test_backstage_passes_TAFKAL80ETC(self):
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
    gilded_rose = GildedRose([item])
    days = 5
    for _ in range(days):
        gilded_rose.update_quality()
        print("Day", _+1, "Sell-in:", item.sell_in, "Quality:", item.quality)


#"REQUERIMIENTO "Conjured Mana Cake"
# Los artículos "conjurados" se degradan en calidad dos veces más rápido que los artículos normales
item = Item(name="Conjured Mana Cake", sell_in=3, quality=6)
gilded_rose = GildedRose([item])
days = 3
for _ in range(days):
    gilded_rose.update_quality()


        



if __name__ == '__main__':
    unittest.main()
