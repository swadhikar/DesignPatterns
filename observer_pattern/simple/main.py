import time

from observer import Publisher, Subscriber

publisher = Publisher()

subs_1 = Subscriber('swadhi')
subs_2 = Subscriber('kanishka')
subs_3 = Subscriber('keethu')

publisher.subscribe(subs_1)
publisher.subscribe(subs_2)
publisher.subscribe(subs_3)

for n in range(1, 11):
    m = n * 2
    time.sleep(0.5)
    publisher.notify_subscribers(f'{m}')
    print()
