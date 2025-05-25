from shodan_lookup import shodan_info
from jinja2 import Template

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

        # ✅ Shodan Info Section
        file.write("\n📡 Shodan Info:\n")
        info = shodan_info(target)
        for key, value in info.items():
            file.write(f"{key.capitalize()}: {value}\n")

    print(f"Report saved to {filename}")

def generate_html_report(target, results):
    with open("template.html") as f:
        template = Template(f.read())

    html = template.render(
        target=target,
        results=results,
        shodan_info=shodan_info(target)
    )
    filename = f"{target}_report.html"
    with open(filename, "w") as f:
        f.write(html)

    print(f"HTML report saved to {filename}")
