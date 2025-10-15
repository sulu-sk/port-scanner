import socket
import argparse

def scan_ports(target, start_port, end_port):
    print(f"Сканирование хоста {target} с портов {start_port} по {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Порт {port} открыт")
            sock.close()
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break
        except socket.gaierror:
            print("Хост недоступен.")
            break
        except socket.error:
            print("Ошибка подключения к серверу.")
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Простой сканер портов на Python")
    parser.add_argument("target", help="IP-адрес или домен цели")
    parser.add_argument("start_port", type=int, help="Начальный порт")
    parser.add_argument("end_port", type=int, help="Конечный порт")
    args = parser.parse_args()

    scan_ports(args.target, args.start_port, args.end_port)
