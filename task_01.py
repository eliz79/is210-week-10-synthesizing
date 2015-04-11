#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionairies combined for lookup capability."""

import pprint 
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
        t_orders = order['total']
        if cust_id not in combined_dict:
            combined_dict[cust_id] = {'orders':1, 'total': t_orders}
    else:
        combined_dict[cust_id]['orders']+=1
        combined_dict[cust_id]['total']+=t_orders
        pprint.pprint(combined_dict)

    for customer in customers.iterkeys():
        cust_email = customers.values()
        cust_key = customers.keys()
        pprint.pprint(cust_key)
        cust_email = customers.values()
        pprint.pprint(cust_email)
        #if cust_key in customers.keys():
         #   print 'yes'
        #pprint.pprint(final)
         #   combined_dict[customer].update(order)
            #pprint.pprint(customers)

       # cust_name = combined_dict.keys()
       # pprint.pprint(cust_name)
        #cust_email = customer['email': 'email@one.com']
        #print customer
      #  if customer in combined_dict:
       #     combined_dict[cust_id][t_orders] += t_orders
        #    print customer
        #else:
        #    combined_dict[cust_name]
    

