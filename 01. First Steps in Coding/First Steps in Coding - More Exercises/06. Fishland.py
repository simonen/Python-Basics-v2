skumria_price = float(input())
tzatza_price = float(input())

palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

palamud_price = skumria_price * 1.6
safrid_price = tzatza_price * 1.8
midi_price = 7.5

grand_total = palamud_price * palamud_kg + safrid_price * safrid_kg + midi_price * midi_kg

print(f"{grand_total:.2f}")