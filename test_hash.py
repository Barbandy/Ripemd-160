#coding: UTF-8
import hashlib
import pytest
import ripemd160

def hash_ripemd160(data):
    h = hashlib.new('ripemd160')
    h.update(data)
    return  h.hexdigest()


def test_ripemd160():
    data = 'ripemd160'
    assert hash_ripemd160(data) == ripemd160.calc_ripemd160(data)
	
#if __name__ == '__main__':
    #test_ripemd160()
