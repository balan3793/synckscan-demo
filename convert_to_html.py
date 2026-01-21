import json
from pathlib import Path

# Load Snyk JSON report
with open("report.json", "r") as f:
    data = json.load(f)

html = """<html><head><title>Snyk Vulnerability Report</title>
<style>
body { font-family: Arial; padding: 20px; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }
</style></head><body>
<h1>Snyk Vulnerability Report</h1>
"""

vulns = data.get("vulnerabilities", [])
if not vulns:
    html += "<p>No vulnerabilities found.</p>"
else:
    html += "<table><tr><th>ID</th><th>Severity</th><th>Title</th><th>Package</th><th>Version</th><th>Description</th></tr>"
    for v in vulns:
        html += "<tr>"
        html += f"<td>{v.get('id','')}</td>"
        html += f"<td>{v.get('severity','')}</td>"
        html += f"<td>{v.get('title','')}</td>"
        html += f"<td>{v.get('packageName','')}</td>"
        html += f"<td>{v.get('version','')}</td>"
        html += f"<td>{v.get('description','')}</td>"
        html += "</tr>"
    html += "</table>"

html += "</body></html>"

Path("report.html").write_text(html)
