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
git clone https://github.com/<твой_логин>/port-scanner.git
cd port-scanner
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
