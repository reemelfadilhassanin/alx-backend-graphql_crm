# import datetime

# def log_crm_heartbeat():
#     now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
#     with open('/tmp/crm_heartbeat_log.txt', 'a') as f:
#         f.write(f"{now} CRM is alive\n")
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

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
