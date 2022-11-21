import os
import pandas as pd

from detection import constants
from datetime import datetime
from detect_test import giveTimeStamp
from detection import py_parser
from generation import attack_model
from select_repos import dev_count
from label_perturbation_attack import knn


# generate erroneous data
# then use the generated data to fuzz 5 methods.
# this file should have the erroneous data and then you can use the file to then fuzz.

def fuzzGiveTimeStamp():

	strToret = fvalue1

	if strToret == strftime('%Y-%m-%d %H:%M:%S'):

		giveTimeStamp()

	else:

		print("Error: Wrong value for strToret.")


def fuzzGetImport():

	import_list = fvalue2

	if import_list == []:

		getImport()

	else:

		print("Error: Import_list is not a list.") 


def fuzzCalculate_K():

	kVals = fvalue3

	if kVals == (3, 10, 2):

		calculate_k()

	else:

		print("Error: kVals has the wrong value.")



def fuzzGetDevEmailForCommit():

	author_emails = fvalue4

	if author_emails == []:

		getDevEmailForCommit()

	else:

		print("Error: author_emails is not a list.")



def fuzzPredict():

	predictions = fvalue5

	if predictions == []:

		predict()

	else:

		print("Error: predictions did not equal a list.")


def fuzzValues():
	
	fValue1 = "Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ"
	fvalue2 = "-9223372036854775808/-1"
	fvalue3 = "<script\\x0Dtype=\"text/javascript\">javascript:alert(1);</script>"
	fvalue4 = "../../../../../../../../../../../etc/hosts"
	fvalue5 = "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"





if __name__ == '__main__':
	
	fuzzGiveTimeStamp()
	fuzzCalculate_K()
	fuzzGetDevEmailForCommit()
	fuzzPredict()
	fuzzGetImport()