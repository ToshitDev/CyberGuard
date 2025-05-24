def generate_report(target, results):
    filename = f"{target}_report.txt"
    with open(filename, "w") as file:
        file.write(f"Scan Report for {target}\n")
        file.write("=" * 40 + "\n")
        for entry in results:
            file.write(f"Port: {entry['port']}\n")
            file.write(f"State: {entry['state']}\n")
            file.write(f"Banner: {entry['banner']}\n")
            file.write("-" * 20 + "\n")
    print(f"Report saved to {filename}")
