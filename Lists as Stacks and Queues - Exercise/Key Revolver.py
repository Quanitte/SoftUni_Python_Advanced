bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
intelligence_value = int(input())

bullets_used = 0
ammo = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_bullet <= current_lock:
        print("Bang!")
        locks.pop(0)
    else:
        print("Ping!")

    bullets_used += 1
    ammo += 1
    if ammo == gun_barrel_size and bullets:
        print("Reloading!")
        ammo = 0

money_earned = intelligence_value - (bullets_used * bullet_price)

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
