#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionairies combined for lookup capability."""

from data import CUSTOMERS, ORDERS


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
        2: {'name': 'Person One',
            'email': 'email@one.com',
            'orders': 2,
            'total': 20}
        3: {'name': 'Person Two',
            'email': 'email@two.com',
            'orders': 1,
            'total': 15}}
    """
    combined_dict = {
        'name': 'Person One',
        'email': 'email@email.com',
        'orders': orders.itervalues(),
        'total': sum(orders)
    }
    for customer_id in combined_dict:
        customer_id = customers.copy()
        combined_dict.update(orders)
        #zipped = zip(customer_id, combined_dict)
        return combined_dict
