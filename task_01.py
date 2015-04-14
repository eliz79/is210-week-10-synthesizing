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
        if cust_id not in combined_dict:
            combined_dict[cust_id] = customers.values()
            combined_dict[cust_id] = {'orders': 1}
            combined_dict[cust_id]['total'] = order['total']
        else:
            combined_dict[cust_id]['orders'] = order['customer_id']
            combined_dict[cust_id]['name'] = customers[cust_id]['name']
            combined_dict[cust_id]['email'] = customers[cust_id]['email']
            combined_dict[cust_id]['total'] = (order['total'] + order['total'])
    return combined_dict
