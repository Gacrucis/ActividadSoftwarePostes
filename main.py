from elements import Relay, ShortCable, LongCable, Transformer
import posts


p1 = posts.NormalPost()
p2 = posts.BigPost()
p3 = posts.NormalPost()

c1 = ShortCable()
c2 = LongCable()
c3 = LongCable()
c4 = LongCable()
t1 = Transformer()
t2 = Transformer()
t3 = Transformer()
r1 = Relay()
r2 = Relay()
r3 = Relay()

p1.install(c1)
p1.install(t1)
p1.install(c3, 2)

p2.install(c4, 6)
p2.install(c2, 4)

p3.install(r1)
p3.install(r2)
p3.install(r3)
p3.install(t3)

print(p1)
print(p2)
print(p3)

c1.connect(t1)
c1.connect(c4)
c4.connect(r1)

c1.print_connections()
c4.print_connections()