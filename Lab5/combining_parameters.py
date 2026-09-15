# create log event
def create_log_event(event_type, *messages, **metadata):
    log_event = {
        "event_type": event_type,
        "messages": messages,
        "metadata": metadata
    }
    return log_event


messages = ["Order placed", "New Order created for Saranya",
            "Awaiting payment confirmation"]
metadata = {"customer": "Saranya",
            "total_amount": 1234, "payment_method": "card"}
print(create_log_event("ORDER_CREATED", *messages, **metadata))
print(create_log_event("ORDER_CREATED",
      "Awaiting for payment response", **{"customer": "Allan"}))


# calculate order


def calculate_order(customer, *prices, **options):
    order_details = {"customer": customer}
    subtotal, discount, shipping_fee = 0, 0, 0

    for price in prices:
        subtotal += price
    if options.get("discount"):
        discount = subtotal * options["discount"]/100
    if options.get("shipping_fee"):
        shipping_fee = subtotal * options["shipping_fee"]/100

    total = subtotal - discount + shipping_fee
    order_details["disount"] = discount
    order_details["subtotal"] = subtotal
    order_details["shipping_fee"] = shipping_fee
    order_details["total"] = total

    return order_details


print(calculate_order("saranya", 1300, 120, options={"discount": 30}))
print(calculate_order("saranya", 1300, options={"discount": 3}))
