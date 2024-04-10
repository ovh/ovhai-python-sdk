# ovhai - OVHcloud's AI Python SDK

The `ovhai` library is a Python client that allows developers to easily use the OVHcloud AI API. With this SDK, you can run, manage, automate your notebooks, training and deployments in the cloud using OVHcloud's AI products (AI Notebooks, AI Training, AI Deploy).

## ⚠️ Alpha Warning ⚠️

This package is currently in the alpha phase of development. The APIs and functionality of the package may not be fully tested.

## Installation
To install the SDK, run the following command:

```bash
pip install ovhai
```

The SDK requires Python 3.8 or higher. For information about how to update your Python version, see the [official Python documentation](https://www.python.org/downloads/).

## Getting started

Once you've installed the AI SDK, you can import it to use OVHcloud's AI products using the API.

You can start by the client creation:

```python
from ovhai import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://gra.training.ai.cloud.ovh.net", 
    token="YOUR_AI_TOKEN",
)
```

The token used to create the client can be created via the Control Panel (UI), from the AI Dashboard.

Once your client is defined, you can call an endpoint:

```python
from ovhai.models import Me
from ovhai.ovhai_types import Response

with client as client:
    res: Me = me.sync(client=client)

    # or if you need more info (e.g. status_code)
    response: Response[Me] = me.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
import asyncio
from ovhai.models import Me
from ovhai.ovhai_types import Response

async def main(client):
    res: Me = await me.asyncio(client=client)
    response: Response[Me] = await me.asyncio_detailed(client=client)
    print("res:", res)
    print("response:", response)
    
# Run the main function asynchronously
asyncio.run(main(client=client))
```

## Things to know

Every OVHcloud's AI API endpoint has its dedicated Python module that comes with four functions:
1. `sync`: Blocking request that returns parsed data (if successful) or `None`
2. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
3. `asyncio`: Like `sync` but async instead of blocking
4. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking


## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from ovhai import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://gra.training.ai.cloud.ovh.net",
    token="YOUR_AI_TOKEN",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from ovhai import Client

client = Client(
    base_url="https://gra.training.ai.cloud.ovh.net",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://gra.training.ai.cloud.ovh.net", proxies="http://localhost:8030"))
```
