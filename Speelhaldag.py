personen = 3
toegangticket = 7.45
bedragper5minuten = 0.37
aantalkeer = 9
aantalminuten = 45

saldo = personen * (toegangticket + bedragper5minuten * aantalkeer)

print('Dit geweldige dagje-uit met ' + str(personen) + ' mensen in de Speelhal met ' + str(aantalminuten) + ' minuten VR kost je maar ' + str(saldo) + ' euro')