#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionairies combined for lookup capability."""


def sum_orders(customers, orders):
    """Combining dictionaries for a data function.
    Args:
        customers(dict): a dictionary of customers keyed by customer_id.
        orders(dict): a dictionary of orders keyed by order_id.

    Return:
        Will return a combined dictionary.

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
            3: {'customer_id': 2, 'total': 10},
            4: {'customer_id': 3, 'total': 15}}

        >>> CUSTOMERS = {2: {'name': 'person one', 'email': 'email@one.com'},
            3: {'name': 'person two', 'email': 'email@two.com'}}

        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
            'email': 'email@one.com',
            'orders': 2,
            'total': 20}
        3: {'name': 'Person Two',
            'email': 'email@two.com',
            'orders': 1,
            'total': 15}}
    """
    combined_dict = {}
    for order in orders.itervalues():
        cust_id = order['customer_id']
        cust_name = customers[cust_id]['name']
        cust_email = customers[cust_id]['email']
        if cust_id not in combined_dict and customers.keys():
            counter = 1
            t_orders = order['total']
        else:
            combined_dict[cust_id]['orders'] += 1
            t_orders = ((combined_dict[cust_id]['total']) + (order['total']))
        final_order = dict(name=cust_name, email=cust_email, orders=counter,
                           total=t_orders)
        cust_final_order = {cust_id: final_order}
        combined_dict.update(cust_final_order)
    return combined_dict
