n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

attended_guests = set()

while True:
    guest = input()
    if guest == "END":
        break
    attended_guests.add(guest)

absent_vip_guests = sorted([guest for guest in vip_guests if guest not in attended_guests])
absent_regular_guests = sorted([guest for guest in regular_guests if guest not in attended_guests])

print(len(absent_vip_guests) + len(absent_regular_guests))
for guest in absent_vip_guests:
    print(guest)
for guest in absent_regular_guests:
    print(guest)
