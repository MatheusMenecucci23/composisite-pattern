from caixa import caixa
from objeto import objeto


def main():
        box1 = caixa()
        box2 = caixa()
        box3 = caixa()

        objects = []
        for i in range(6):
            objects.append(objeto(10.00))

        box1.add([objects[0]])
        box1.add([objects[1]])

        box2.add([objects[2]])
        box2.add([objects[3]])

        box3.add([objects[4]])
        box3.add([objects[5]])


        # Chama o método price
        print(f"\nPreço total da Caixa 1: R${box1.calulate_price():.2f}")
        print(f"\nPreço total da Caixa 2: R${box2.calulate_price():.2f}")
        print(f"\nPreço total da Caixa 3: R${box3.calulate_price():.2f}")


        print(box1.showContent())




if __name__ == "__main__":
    main()