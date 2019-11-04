import graphene
from graphql_jwt.decorators import login_required

from healthid.apps.orders.schema.suppliers_query import (SuppliersType)
from healthid.apps.orders.models import Suppliers
from healthid.utils.app_utils.database import (SaveContextManager)
from healthid.utils.app_utils.validators import \
    validate_email, validate_mobile
from healthid.utils.messages.orders_responses import ORDERS_ERROR_RESPONSES
from graphql import GraphQLError


class SuppliersInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String()
    mobile_number = graphene.String()
    address_line_1 = graphene.String()
    address_line_2 = graphene.String()
    lga = graphene.String()
    city_id = graphene.Int()
    tier_id = graphene.Int()
    country_id = graphene.Int()
    credit_days = graphene.Int()
    logo = graphene.String()
    payment_terms_id = graphene.Int()
    commentary = graphene.String()


class AddSupplier(graphene.Mutation):
    """
    Add a new supplier to the database

    args:
        name(str): supplier name
        email(str): supplier contact email
        mobile_number(str): contact number
        address_line_1(str): first address line
        address_line_2(str): second address line
        lga(str): name of the supplier's local goverment area
        city_id(int): id of the supplier city location
        tier_id(int): id of the supplier's category
        country_id(int): supplier country
        credit_days(int): average number of days expected to settle outstanding
                          payments to the supplier
        logo(str): image URL for the supplier logo
        payment_terms_id(int): id of the preferred payment method
        commentary(str): additional comments

    returns:
        supplier(obj): 'Suppliers' model object detailing the created supplier.
    """

    class Arguments:
        input = SuppliersInput(required=True)

    supplier = graphene.Field(SuppliersType)

    @classmethod
    @login_required
    def mutate(cls, root, info, input=None):
        user = info.context.user
        supplier = Suppliers()

        if validate_email(input.email) is None:
            raise GraphQLError(ORDERS_ERROR_RESPONSES["\
                invalid_supplier_email"])
        if validate_mobile(input.mobile_number) is None:
            raise GraphQLError(ORDERS_ERROR_RESPONSES["\
                invalid_supplier_phone"])
        if input.credit_days == 0:
            input['payment_terms_id'] = 1
        for (key, value) in input.items():
            setattr(supplier, key, value)
        supplier.user = user
        with SaveContextManager(supplier, model=Suppliers) as supplier:
            return cls(supplier=supplier)
