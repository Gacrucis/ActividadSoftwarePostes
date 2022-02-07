from elements import ShortCable, LongCable, Transformer
import posts


poste_1 = posts.NormalPost()
print(poste_1)

c1 = ShortCable()
c2 = LongCable()
t1 = Transformer()

poste_1.install(c1)
poste_1.install(t1)
poste_1.install(c2, 4)
print(poste_1)

c1.connect(t1)
c1.print_connections()

