import datetime
import requests  # Required for making HTTP requests to the GraphQL endpoint

from celery import shared_task

@shared_task
def generate_crm_report():
    url = 'http://localhost:8000/graphql'
    query = """
    query {
        totalCustomers
        totalOrders
        totalRevenue
    }
    """
    response = requests.post(url, json={'query': query}, headers={'Content-Type': 'application/json'})
    data = response.json().get('data', {})

    customers = data.get('totalCustomers', 'N/A')
    orders = data.get('totalOrders', 'N/A')
    revenue = data.get('totalRevenue', 'N/A')

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"{timestamp} - Report: {customers} customers, {orders} orders, {revenue} revenue\n"

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(log_msg)
