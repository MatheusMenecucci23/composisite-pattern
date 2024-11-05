from conjunto import elements


class caixa(elements):
    def __init__(self):
        self.contents = []

    def calulate_price(self):
        total_price = 0
        for item in self.contents:
            print(item)
            total_price += item[0].calulate_price()
        return total_price

    def add(self, component: elements):
        self.contents.append(component)

    def showContent(self):

        content_info = "Conteúdo da caixa:\n"
        for item in self.contents:
            content_info += f"- {item[0].showContent()}\n"
        return content_info.strip()