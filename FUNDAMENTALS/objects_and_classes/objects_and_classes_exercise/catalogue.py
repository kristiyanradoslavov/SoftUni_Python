class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        current_product = (x for x in self.products if x.startswith(first_letter))
        return list(current_product)

    def __repr__(self):
        result = ""
        sorted_list = sorted(self.products, key=str)
        result += f"Items in the {self.name} catalogue:\n"
        for index, char in enumerate(sorted_list):
            if index < len(sorted_list) - 1:
                result += f"{char}\n"
            elif index == len(sorted_list) - 1:
                result += f"{char}"

        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
