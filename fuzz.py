import traceback
import pandas as pd


from dataclasses import dataclass
from detection import constants
from datetime import datetime
from generation import py_parser
from detection import py_parser
from generation import attack_model
from select_repos import dev_count
from label_perturbation_attack import knn

#test comment
# generate erroneous data
# then use the generated data to fuzz 5 methods.
# this file should have the erroneous data and then you can use the file to then fuzz.

def fuzzCheckAlgoNames(fuzz):

	algo_list = fuzz.fValue1
	
	if not algo_list:

		checkAlgoNames()

	else:

		print("Error: Wrong value for algo_list.")


def fuzzGetImport(fuzz):

	import_list = fuzz.fValue2

	if not import_list:

		getImport()

	else:

		print("Error: Import_list is not a list.") 


def fuzzCalculate_K(fuzz):

	kVals = fuzz.fValue3

	if kVals == (3, 10, 2):

		calculate_k()

	else:

		print("Error: kVals has the wrong value.")



def fuzzGetDevEmailForCommit(fuzz):

	author_emails = fuzz.fValue4

	if not author_emails:

		getDevEmailForCommit()

	else:

		print("Error: author_emails is not a list.")



def fuzzPredict(fuzz):

	predictions = fuzz.fValue5

	if not predictions:

		predict()

	else:

		print("Error: predictions did not equal a list.")

@dataclass
class fuzzValues:
	
	fValue1 = "Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ"
	fValue2 = "-9223372036854775808/-1"
	fValue3 = "<script\\x0Dtype=\"text/javascript\">javascript:alert(1);</script>"
	fValue4 = "../../../../../../../../../../../etc/hosts"
	fValue5 = "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"






if __name__ == '__main__':
	fuzz = fuzzValues()
	fuzzCheckAlgoNames(fuzz)
	fuzzCalculate_K(fuzz)
	fuzzGetDevEmailForCommit(fuzz)
	fuzzPredict(fuzz)
	fuzzGetImport(fuzz)