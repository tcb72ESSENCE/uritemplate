"""

uritemplate.api
===============

This module contains the very simple API provided by uritemplate.

"""
from uritemplate.template import URITemplate


def expand(uri, var_dict=None, **kwargs):
    """Expand the template with the given parameters.

    :param dict var_dict: Optional dictionary with variables and values
    :param kwargs: Alternative way to pass arguments
    :returns: str

    Example::

        expand('https://api.github.com{/end}', {'end': 'users'})
        expand('https://api.github.com{/end}', end='gists')

    .. note:: Passing values by both parts, will override values in
              ``var_dict``.
    """
    t = URITemplate(uri)
    return t.expand(var_dict, **kwargs)
