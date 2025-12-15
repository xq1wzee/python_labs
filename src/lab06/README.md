# ЛАБОРАТОРНАЯ РАБОТА №6

# Задание А — модуль `src/lab06/cli_text.py`
**Реализую модуль с подкомандами:** 
  - `stats --input <txt> [--top 5]` — анализ частот слов в тексте (использовны функции из `lab04`);
  - `cat --input <path> [-n]` — вывод содержимого файла построчно (с нумерацией при `-n`).
```python
import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        p = Path(args.input)
        if not p.exists():
            raise FileNotFoundError("Файл не найден")
        with p.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.rstrip("\n")
                if args.n:
                    print(f"{i}\t{line}")
                else:
                    print(line)

    elif args.command == "stats":
        p = Path(args.input)
        if not p.exists():
            raise FileNotFoundError("Файл не найден")
        text = p.read_text(encoding="utf-8")
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)
        for word, count in top_n(freq, args.top):
            print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```

## Результат:

1. Вывод содержимого файла построчно (с нумерацией при `-n`).
Команда:
`python3 -m src.lab06.cli_text cat --input data/samples/cities.csv -n`
![Output 6.A](./images/lab06/lab06_1.png)

2. Анализ частот слов в тексте. 
Команда:
`python3 -m src.lab06.cli_text stats --input src/lab03/input.txt --top 5`
![Output 6.A2](./images/lab06/lab06_2.png)

# Задание B — модуль `src/lab06/cli_convert.py`
**Реализую модуль с подкомандами:** 
  - `json2csv --in data/samples/people.json --out data/out/people.csv`  
  - `csv2json --in data/samples/people.csv --out data/out/people.json`  
  - `csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx`
```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv", help="JSON -> CSV")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="CSV -> JSON")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="CSV -> XLSX")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
```

## Результат:

1. **Конвертация `JSON -> CSV`**

 Команда:
`python3 -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv`
 
 Исходная директория `data/samples/people.json`:
![people.json](./images/lab06/lab06_3.png)
 
 Результат в `data/out/people_from_json.csv`:
![people_from_json.csv](./images/lab06/lab06_4.png)

2. **Аналогично и для `csv2json` & `csv2xlsx`**:

 -`python3 -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json`
 
 -`python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/cities.csv --out data/out/cities.xlsx`
