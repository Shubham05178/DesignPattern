from Weather import Weather
from mobile import Mobile
from tv import TV
t=TV()
m=Mobile()
w=Weather()
w.subscribe(t)
w.subscribe(m)
w.update(19)
w.unsubscribe(m)
w.unsubscribe(t)
w.subscribe(t)
w.subscribe(m)
w.subscribe(t)
w.subscribe(m)
w.subscribe(t)
w.subscribe(m)
w.update(20)