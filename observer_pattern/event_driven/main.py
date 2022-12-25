import time

from observer import Publisher, Subscriber

publisher = Publisher()

subs_1 = Subscriber('swadhi', 'elders')
subs_2 = Subscriber('kanishka', 'kids')
subs_3 = Subscriber('keethu', 'kids')
subs_4 = Subscriber('sridhar', 'elders')

print()
for n in range(1, 11):
    time.sleep(0.25)
    publisher.notify_subscribers('elders', f'{n * 2}')
    print()
    time.sleep(0.25)
    publisher.notify_subscribers('kids', f'{n * 3}')
    print()
