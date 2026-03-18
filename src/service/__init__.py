'''
This file makes the `service` package a namespace package,
allowing you to organize your GUI-related modules and subpackages under this directory.
You can add any initialization code for the `service` package here if needed.
service should not depend on  gui
'''
from .book import Book
from .account import Account

__all__ = ['Book', 'Account']
