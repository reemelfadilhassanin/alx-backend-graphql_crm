INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # GraphQL
    "graphene_django",
    "crm",
]

GRAPHENE = {
    "SCHEMA": "alx_backend_graphql_crm.schema.schema"  # point to schema
}

DEBUG = True   # during development

ALLOWED_HOSTS = ["*"]  # allow all hosts for local dev

