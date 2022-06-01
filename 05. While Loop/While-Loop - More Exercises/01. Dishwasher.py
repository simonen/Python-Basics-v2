detergent = int(input())

det_vol = detergent * 750  # ml
dishes_in = input()
counter = 0
pots = 0
plates = 0

while dishes_in != "End":
    counter += 1
    if counter % 3 == 0 and counter != 0:
        pots += int(dishes_in)
        det_vol -= int(dishes_in) * 15
    else:
        det_vol -= int(dishes_in) * 5
        plates += int(dishes_in)
    if det_vol < 0:
        print(f"Not enough detergent, {abs(det_vol)} ml. more necessary!")
        break
    dishes_in = input()
else:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {abs(det_vol)} ml.")
