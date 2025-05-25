from scanner import scan_target
from report import generate_report, generate_html_report
from utils import is_valid_target
from shodan_lookup import shodan_info

def main():
    target = input("Enter IP or domain to scan: ")

    if not is_valid_target(target):
        print("Invalid IP/domain.")
        return

    results = scan_target(target)
    generate_report(target, results)
    generate_html_report(target, results)

    # Print Shodan info in terminal
    info = shodan_info(target)
    print("\n📡 Shodan Info:")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
