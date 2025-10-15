import socket
import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def scan_port(target, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            return port, (result == 0)
    except Exception:
        return port, False

def save_csv(filename, target, results):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["target", "port", "open", "timestamp"])
        ts = datetime.utcnow().isoformat()
        for port, is_open in results:
            writer.writerow([target, port, is_open, ts])

def main():
    parser = argparse.ArgumentParser(description="Многопоточный сканер портов")
    parser.add_argument("--target", required=True, help="IP или домен")
    parser.add_argument("--start", type=int, default=1, help="Начальный порт")
    parser.add_argument("--end", type=int, default=1024, help="Конечный порт")
    parser.add_argument("--threads", type=int, default=50, help="Число потоков")
    parser.add_argument("--timeout", type=float, default=0.5, help="Таймаут в секундах")
    parser.add_argument("--output", help="Файл для сохранения (CSV)")
    args = parser.parse_args()

    target = args.target
    start_port = max(1, args.start)
    end_port = min(65535, args.end)

    ports = range(start_port, end_port + 1)
    results = []

    print(f"Start scanning {target} ports {start_port}-{end_port} with {args.threads} threads...")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(scan_port, target, p, args.timeout): p for p in ports}
        for fut in as_completed(futures):
            port, is_open = fut.result()
            if is_open:
                print(f"[+] {port} open")
            results.append((port, is_open))

    if args.output:
        save_csv(args.output, target, results)
        print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()
