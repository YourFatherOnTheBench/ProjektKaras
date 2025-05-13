import csv
from io import StringIO

network = {}
select_month = 3  # np. Marzec

with open('lotnisko.csv', encoding='utf-8') as csv_file:
    line_count = 0

    for raw_line in csv_file:
        # 1. Usuń końce linii i podwójne cudzysłowy
        cleaned_line = raw_line.strip().replace('""', '"')
        
        # 2. Zamień string na listę kolumn
        row = next(csv.reader(StringIO(cleaned_line), delimiter=',', quotechar='"'))

        # 3. Spróbuj naprawić zlepione dane
        if len(row) < 13 and ',' in row[0]:
            extra_split = row[0].split(',')  # Rozbij np. "2.00,0.00,0.00,..."
            row = extra_split + row[1:]  # Dołącz resztę

        if line_count == 0:
            print(f"Kolumny: {row}")
        else:
            try:
                month = int(row[12])
                if month == select_month:
                    origin = row[7]
                    dest = row[10]
                    key = (origin, dest)
                    network[key] = network.get(key, 0) + 1
            except Exception as e:
                print(f"Błąd w linii {line_count}: {e} → {row}")
        
        line_count += 1

# 🔟 Najczęstsze połączenia
sorted_network = sorted(network.items(), key=lambda x: x[1], reverse=True)

print("\n10 najczęstszych połączeń w wybranym miesiącu:")
for i, ((origin, dest), count) in enumerate(sorted_network[:10], 1):
    print(f"{i}. {origin} → {dest}: {count} lotów")
