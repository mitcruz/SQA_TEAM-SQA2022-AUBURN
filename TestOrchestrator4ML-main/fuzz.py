import os

from detect_test import giveTimeStamp
from py_parser import getImport
from attack_model import calculate_k
from dev_count import getDevEmailForCommit
from knn.py import predict


# generate erroneous data
# then use the generated data to fuzz 5 methods.
# this file should have the erroneous data and then you can use the file to then fuzz.

def fuzzGiveTimeStamp():

	strToret = fvalue1

	if strToret = strftime('%Y-%m-%d %H:%M:%S'):

		giveTimeStamp()

	else:

		print("Error: Wrong value for strToret.")


def fuzzGetImport():

	import_list = fvalue2

	if import_list = []:

		getImport()

	else:

	print("Error: Import_list is not a list.") 


def fuzzCalculate_K():

	kVals = fvalue3

	if kVals = (3, 10, 2):

		calculate_k()

	else:

		print("Error: kVals has the wrong value.")



def fuzzGetDevEmailForCommit():

	author_emails = fvalue4

	if author_emails = []:

		getDevEmailForCommit()

	else:

		print("Error: author_emails is not a list.")



def fuzzPredict():

	predictions = fvalue5

	if predictions = []:

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