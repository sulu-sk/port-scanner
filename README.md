# Port Scanner (Python)

Простой многопоточный сканер портов на Python.  
Учебный проект для портфолио: показывает навыки работы с Python, сокетами, Linux и обработкой логов.

## Возможности
- Сканирование диапазона портов
- Многопоточное выполнение (для ускорения)
- Настраиваемый таймаут
- Сохранение отчёта в CSV или TXT

## Установка
```bash
git clone https://github.com/<sulu-sk>/port-scanner.git
cd port-scanner
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

python port_scanner.py --target scanme.nmap.org --start 1 --end 1024 --threads 100 --timeout 0.5 --output report.csv

python port_scanner.py --target 127.0.0.1 --start 20 --end 1024 --threads 50 --timeout 0.3 --output open_ports.csv

Автор

Sultan Kamil — студент информационной безопасности.
