from celery import shared_task
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

@shared_task
def generate_crm_report():
    transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', verify=False, retries=1)
    client = Client(transport=transport, fetch_schema_from_transport=False)
    query = gql("""
        query {
            totalCustomers
            totalOrders
            totalRevenue
        }
    """)
    result = client.execute(query)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (f"{ts} - Report: {result['totalCustomers']} customers, "
              f"{result['totalOrders']} orders, {result['totalRevenue']} revenue\n")

    with open('/tmp/crm_report_log.txt', 'a') as f:
        f.write(report)
