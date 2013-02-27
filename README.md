outbound-python
===============

Python library for [Outbound](http://www.outbound.io/docs)

### [Identify](http://www.outbound.io/docs/identify)
These are usually in places where your user objects are [created or updated](http://www.outbound.io/docs/identify).

    from outbound import Client
    client = Client(MY_API_KEY)
    client.identify("UNIQUE_USER_ID", traits={'name': 'Bill Lee Johnson', 'email': 'billlee@johnson.com'})


### [Track](http://www.outbound.io/docs/track)
These are used in places where events occur in your system. Checkout, Signup, user messaging, etc.

    from outbound import Client
    client = Client(MY_API_KEY)
    client.track("UNIQUE_USER_ID", event="Checkout", payload={'price': 24.95, 'item': 'Magic wand'})
