#!/usr/bin/env python
#-*- coding: utf-8 -*-

import itertools, time
import os, psutil


def load_dic():
	fp=open("greek.dic")
	dic_lst=fp.read().decode("utf8").splitlines()
	fp.close()
	return dic_lst

def anagram(scrambled, dic_lst):
		
	results=[]
	scr_len=len(scrambled)
	scr_sorted=sorted(scrambled)	
	results=list(itertools.ifilter(lambda y:sorted(y)==scr_sorted, itertools.ifilter(lambda x:len(x)==scr_len,dic_lst)))
	results.sort()
	if scrambled in results:	
		results.remove(scrambled)
	
	return results
	

	


