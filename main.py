i = 1
while i is not [19, 22]:
    if i == 1:
        print("Te vagy az iskola rosszfiúja. Késve érkezel a suli elé, még elszívod a cigidet, aztán… \n"
              " 2. elnyomod a csikket az igazgatónő bringájának kerekébe. \n"
              " 3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket.  \n"
              " 4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire. \n"
              "Mit választasz? Írj be a számot: ")

        v = int(input())
        if v in [2, 3, 4]:
            i = v

    if i == 2:
        print("észreveszi az éppen érkező töri tanárod, mit tettél és… \n"
              "5. azonnal felrángat az igazgatói irodába. Te hőzöngve tiltakozol végig a folyosón. \n"
              "6. gratulál neked, hisz szerinte is egy nagyképű szipirtyó a nő. \n"
              "7. szó nélkül tovább sétál, mivel eléggé parázik tőled. \n"
              "Mit választasz? Írj be a számot: ")
        v = int(input())
        if v in [5, 6, 7]:
            i = v

    # TODO további if-ek
