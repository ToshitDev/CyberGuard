import shodan

def shodan_info(ip):
    api_key = "ys7jGUzXFUOhudU2R5ffhr8hGj0K4mgB"
    api = shodan.Shodan(api_key)
    try:
        host = api.host(ip)
        return {
            "organization": host.get("org", "N/A"),
            "operating_system": host.get("os", "N/A"),
            "open_ports": host.get("ports", []),
            "hostnames": host.get("hostnames", []),
            "city": host.get("city", "N/A"),
            "country": host.get("country_name", "N/A")
        }
    except shodan.APIError as e:
        return {"error": str(e)}
