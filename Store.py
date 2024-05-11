class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} добавлен с ценой {price}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из ассортимента.")
        else:
            print(f"Товар {item_name} не найден в ассортименте.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} обновлена до {new_price}")
        else:
            print(f"Товар {item_name} не найден для обновления цены.")

# Создание объектов магазинов
store1 = Store("Магазин А", "ул. Пушкина 1")
store2 = Store("Магазин Б", "ул. Ленина 5")
store3 = Store("Магазин В", "пр. Мира 10")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("oranges", 0.8)
store2.add_item("milk", 1.2)

store3.add_item("bread", 1.1)
store3.add_item("butter", 2.3)

# Тестирование методов на примере store1
print("Цена яблок:", store1.get_item_price("apples"))
store1.update_item_price("apples", 0.55)
print("Новая цена яблок:", store1.get_item_price("apples"))
store1.remove_item("apples")
print("Цена яблок после удаления:", store1.get_item_price("apples"))
