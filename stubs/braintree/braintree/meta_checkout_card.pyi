from braintree.resource import Resource

class MetaCheckoutCard(Resource):
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def expiration_date(self): ...
    @property
    def masked_number(self): ...