# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self._update_sell_in()
        self._update_quality()

    def _update_sell_in(self):
        self.sell_in -= 1

    def _update_quality(self):
        pass

#Cada uno de los articulos con su requerimientos 

class DexterityVest(Item):
    def _update_quality(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1
        self.quality = max(self.quality, 0)
#la calidad de "Aged Brie" aumenta a medida que envejece y su máxima calidad es de 50
class AgedBrie(Item):
    def _update_quality(self):
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1
        self.quality = min(self.quality, 50)
#
class ElixirMongoose(Item):
    def _update_quality(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1
        self.quality = max(self.quality, 0)

#Es un  artículo legendario y, como tal, su calidad es 80 y nunca se altera.
class Sulfuras(Item):
    def _update_quality(self):
        pass
    
#La calidad aumenta en 2 cuando hay 10 días o menos y en 3 cuando hay 5 días o menos, 
#pero  la calidad cae a 0 después del concierto.
class BackstagePass(Item):
    def _update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality += 3
        elif self.sell_in < 10:
            self.quality += 2
        else:
            self.quality += 1
        self.quality = min(self.quality, 50)

#Los artículos "conjurados" se degradan en calidad dos veces más rápido que los artículos normales
class ConjuredManaCake(Item):
    def _update_quality(self):
        if self.sell_in < 0:
            self.quality -= 4
        else:
            self.quality -= 2
        self.quality = max(self.quality, 0)

class GildedRose:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def create_item(name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(name, sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        elif name == "Conjured Mana Cake":
            return ConjuredManaCake(name, sell_in, quality)
        elif name == "+5 Dexterity Vest":
            return DexterityVest(name, sell_in, quality)
        elif name == "Elixir of the Mongoose":
            return ElixirMongoose(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)

    def update_quality(self):
        for item in self.items:
            item
