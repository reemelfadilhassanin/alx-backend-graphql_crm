# import datetime

# def log_crm_heartbeat():
#     now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
#     with open('/tmp/crm_heartbeat_log.txt', 'a') as f:
#         f.write(f"{now} CRM is alive\n")
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import datetime
import requests
import json

def update_low_stock():
    url = "http://localhost:8000/graphql"
    mutation = """
    mutation {
      updateLowStockProducts {
        success
        updatedProducts
      }
    }
    """
    payload = {"query": mutation}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        success = data.get("data", {}).get("updateLowStockProducts", {}).get("success", False)
        products = data["data"]["updateLowStockProducts"].get("updatedProducts", []) if success else []
    except Exception as e:
        success = False
        products = []
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} - "
    log_line += "Updated: " + ", ".join(products) if success else "Update failed"
    log_line += "\n"

    with open("/tmp/low_stock_updates_log.txt", "a") as f:
        f.write(log_line)

def log_crm_heartbeat():
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    healthy = False

    # GraphQL health check
    try:
        transport = RequestsHTTPTransport(url="http://localhost:8000/graphql", verify=False, retries=1)
        client = Client(transport=transport, fetch_schema_from_transport=False)
        query = gql('{ hello }')
        response = client.execute(query)
        healthy = response.get('hello') is not None
    except Exception:
        healthy = False

    with open('/tmp/crm_heartbeat_log.txt', 'a') as f:
        f.write(f"{now} CRM is alive — GraphQL {'OK' if healthy else 'DOWN'}\n")
