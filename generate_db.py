import csv

products = [
    {
        "id": 1,
        "model": "AK-74M",
        "desc": "The AK-74M is by all standards an average assault rifle with fairly manageable recoil but a slow fire rate.",
        "magazine": 40,
        "pros": "Low vertical recoil, High magazine capacity, Good damage per shot",
        "cons": "Low rate of fire, High horizontal recoil"
    },
    {
        "id": 2,
        "model": "M590A1",
        "desc": "The M590A1 is a jack-of-all-trades among pump-action shotguns, decent in damage and mid-ranged combat.",
        "magazine": 6,
        "pros": "High damage per pellet, Relatively quick pump cycle, Decent damage drop off, Utility use",
        "cons": "Low reserve ammo"
    },
    {
        "id": 3,
        "model": "M4",
        "desc": "he M4 is a well-rounded weapon with decent handling, above-average damage, and adaquate rate of fire.",
        "magazine": 30,
        "pros": "Above average damage output, Good rate of fire, Versatile attachments",
        "cons": "Subpar vertical recoil, Harsch damage drop off"
    },
    {
        "id": 4,
        "model": "M249",
        "desc": "The M249 has a rather mediocre fire rate of 650, but it makes up for it with its high damage, controllable recoil and great accuracy.",
        "magazine": 100,
        "pros": "High damage per shot, High magazine capacity, Low vertical recoil",
        "cons": "Low rate of fire, Slow reload time"
    },
    {
        "id": 5,
        "model": "SR-25",
        "desc": "The SR-25 is a relatively subpar Marksman Rifle, it outputs a moderate single-shot damage of 61, comparable to that of the Mk 14 EBR.",
        "magazine": 20,
        "pros": "High damage per shot, Versatile attachments",
        "cons": "Steep damage drop off after 40 m, Slow reload speed"
    },
    {
        "id": 6,
        "model": "Commando 9",
        "desc": "The Commando 9 is designated as an assault rifle, despite its SMG-like damage drop-off and ADS time identical to that of the SMG class",
        "magazine": 25,
        "pros": "High damage output, Low recoil, Quick reload time, Quick ADS time compared to other assault rifles, Mild damage drop off",
        "cons": "Low magazine capacity"
    },
    {
        "id": 7,
        "model": "M870",
        "desc": "One of the most powerful pump-action shotguns available, the M870 packs one hell of a punch at close range and can kill a victim outright if all pellets connect.",
        "magazine": 6,
        "pros": "High rate of fire, High damage per pellet, Fast pump cycle, Decent damage drop off",
        "cons": "None"
    },
    {
        "id": 8,
        "model": "TCSG12",
        "desc": "The TCSG12, like the BOSG.12.2 and the ACS12, fires single slugs that have a long range and are capable of headshots.",
        "magazine": 10,
        "pros": "High damage per shot, High destruction / penetration",
        "cons": "High vertical recoil kick per shot, Low magazine capacity"
    },
    {
        "id": 9,
        "model": "MP7",
        "desc": "The MP7 is optimal at close range, the submachine gun boasts a blistering fire rate of 900 RPM and one of the highest damage outputs in the SMG class",
        "magazine": 30,
        "pros": "High rate of fire, High damage output",
        "cons": "Moderate vertical recoil, Lacks grips"
    },
    {
        "id": 10,
        "model": "SASG-12",
        "desc": "The SASG-12 is one of the most potent, close-ranged, semi-automatic shotguns next to the FO-12",
        "magazine": 10,
        "pros": "High damage per pellet, Quick ADS time, Fast rate of fire, High magazine capacity",
        "cons": "Moderate recoil kick per shot, High damage drop off"
    }
]



# Define the CSV file path
csv_file_path = "db_products.csv"

# Write the products data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "model", "desc", "magazine", "pros", "cons"])
    writer.writeheader()  # Write the header row
    writer.writerows(products)  # Write the product data

print(f"Data successfully saved to {csv_file_path}")