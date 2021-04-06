#!/usr/bin/env python3

from subprocess import check_output

def generate_token(pin="0000"):
    '''
    Returns token generated from stoken.

            Parameters:
                    pin (str): pin for token code
            Returns:
                    token (str): generated token from stoken
    '''
    # Execute command stoken tokencode --pin=pin, decode from byte to string UTF-8, and strip \n from from stoken result
    token = check_output(["stoken","tokencode","--pin=" + pin]).decode("utf-8").rstrip('\n')
    # return the genereated token
    return token
