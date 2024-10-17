"""
Wimbledon
Estimate: 40 minutes
Actual:   39 minutes
"""
FILENAME = "wimbledon.csv"

def main():

    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def process_records(records):

    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    max_champ_len = max([len(name) for name in champion_to_count.keys()])

    for name, count in champion_to_count.items():
        print(f"{name:{max_champ_len}}: {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()