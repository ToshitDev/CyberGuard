from scanner import scan_target
from report import generate_report
from utils import is_valid_target

def main():
    target = input("Enter IP or domain to scan: ")

    if not is_valid_target(target):
        print("Invalid IP/domain.")
        return

    results = scan_target(target)
    generate_report(target, results)

if __name__ == "__main__":
    main()