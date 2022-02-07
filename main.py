from elementos import CableCorto, CableLargo, Transformador
import postes


poste_1 = postes.NormalPost()
print(poste_1)

c1 = CableCorto()
t1 = Transformador()

poste_1.install(c1)
poste_1.install(t1)
print(poste_1)

c1.connect(t1)
c1.print_connections()

