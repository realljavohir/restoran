ovqatlar = {
    "palov": [60, 35000],
    "shorva": [25, 30000],
    "somsa": [50, 8000],
    "lavash": [65, 32000],
    "pelmen": [105, 18000],
}
menyu = """
    Oshxonamizga xush kelibsiz!    

    1) Ovqatlar
    2) Xarajatlar
    0) Chiqish
"""
balans = 700000
savat = {}
sanoq = 0

while True:
    print(menyu)
    menyu_tanlash = int(input("\tMenyulardan birini tanlang: "))

    if menyu_tanlash == 1:
        menyu_ovqat = f"""
    1) Palov {ovqatlar["palov"][0]} kg        ->   {ovqatlar["palov"][1]} so'mdan
    2) Shorva {ovqatlar["shorva"][0]} porsa    ->   {ovqatlar["shorva"][1]} so'mdan
    3) Somsa {ovqatlar["somsa"][0]} dona      ->   {ovqatlar["somsa"][1]} so'mdan
    4) Lavash {ovqatlar["lavash"][0]} dona     ->   {ovqatlar["lavash"][1]} so'mdan
    5) Pelmen {ovqatlar["pelmen"][0]} kg      ->   {ovqatlar["pelmen"][1]} so'mdan 
    0) Bosh menyuga qaytish
        """
        print(menyu_ovqat)
        ovqat_tanlash = int(input("\n\tOvqatlardan birini tanlang: "))

        if ovqat_tanlash == 1:
            if balans >= ovqatlar["palov"][1]:
                ovqat_miqdori = int(input("\tQancha kg/porsa/dona sotib olmoqchisiz: "))
                if ovqat_miqdori <= ovqatlar["palov"][0]:
                    ovqatlar["palov"][0] -= ovqat_miqdori
                    xarajat = ovqat_miqdori * ovqatlar["palov"][1]
                    balans -= xarajat
                    print("\n\tPalov sotib olindi!")
                    print(f"\tXarajatingiz: {xarajat} so'm!")
                    sanoq += 1
                    savat.update({f"Palov {sanoq}-xarid": [ovqat_miqdori, xarajat]})
                else:
                    print("\n\tBuncha miqdorda palov yo'q!")
            else:
                print("\n\tSizda palovga yetgulik pul yo'q!")
        elif ovqat_tanlash == 2:
            if balans >= ovqatlar["shorva"][1]:
                ovqat_miqdori = int(input("\tQancha kg/porsa/dona sotib olmoqchisiz: "))
                if ovqat_miqdori <= ovqatlar["shorva"][0]:
                    ovqatlar["shorva"][0] -= ovqat_miqdori
                    xarajat = ovqat_miqdori * ovqatlar["shorva"][1]
                    balans -= xarajat
                    print("\n\tShorva sotib olindi!")
                    print(f"\tXarajatingiz: {xarajat} so'm!")
                    sanoq += 1
                    savat.update({f"Shorva {sanoq}-xarid": [ovqat_miqdori, xarajat]})
                else:
                    print("\n\tBuncha miqdorda shorva yo'q!")
            else:
                print("\n\tSizda shorvaga yetgulik pul yo'q!")
        elif ovqat_tanlash == 3:
            if balans >= ovqatlar["somsa"][1]:
                ovqat_miqdori = int(input("\tQancha kg/porsa/dona sotib olmoqchisiz: "))
                if ovqat_miqdori <= ovqatlar["somsa"][0]:
                    ovqatlar["somsa"][0] -= ovqat_miqdori
                    xarajat = ovqat_miqdori * ovqatlar["somsa"][1]
                    balans -= xarajat
                    print("\n\tSomsa sotib olindi!")
                    print(f"\tXarajatingiz: {xarajat} so'm!")
                    sanoq += 1
                    savat.update({f"Somsa {sanoq}-xarid": [ovqat_miqdori, xarajat]})
                else:
                    print("\n\tBuncha miqdorda somsa yo'q!")
            else:
                print("\n\tSizda somsaga yetgulik pul yo'q!")
        elif ovqat_tanlash == 4:
            if balans >= ovqatlar["lavash"][1]:
                ovqat_miqdori = int(input("\tQancha kg/porsa/dona sotib olmoqchisiz: "))
                if ovqat_miqdori <= ovqatlar["lavash"][0]:
                    ovqatlar["lavash"][0] -= ovqat_miqdori
                    xarajat = ovqat_miqdori * ovqatlar["lavash"][1]
                    balans -= xarajat
                    print("\n\tLavash sotib olindi!")
                    print(f"\tXarajatingiz: {xarajat} so'm!")
                    sanoq += 1
                    savat.update({f"Lavash {sanoq}-xarid": [ovqat_miqdori, xarajat]})
                else:
                    print("\n\tBuncha miqdorda lavash yo'q!")
            else:
                print("\n\tSizda lavashga yetgulik pul yo'q!")
        elif ovqat_tanlash == 5:
            if balans >= ovqatlar["pelmen"][1]:
                ovqat_miqdori = int(input("\tQancha kg/porsa/dona sotib olmoqchisiz: "))
                if ovqat_miqdori <= ovqatlar["pelmen"][0]:
                    ovqatlar["pelmen"][0] -= ovqat_miqdori
                    xarajat = ovqat_miqdori * ovqatlar["pelmen"][1]
                    balans -= xarajat
                    print("\n\tPelmen sotib olindi!")
                    print(f"\tXarajatingiz: {xarajat} so'm!")
                    sanoq += 1
                    savat.update({f"pelmen {sanoq}-xarid": [ovqat_miqdori, xarajat]})
                else:
                    print("\n\tBuncha miqdorda pelmen yo'q!")
            else:
                print("\n\tSizda pelmenga yetgulik pul yo'q!")

    elif menyu_tanlash == 2:
        print(f"\n\tSizning balansingiz: {balans} so'm!")
        print(f"\t{savat}")

    elif menyu_tanlash == 0:
        print("\n\tTashrifingiz uchun rahmat!")
        break

    else:
        print("\n\tBunday menyu mavjud emas!")
