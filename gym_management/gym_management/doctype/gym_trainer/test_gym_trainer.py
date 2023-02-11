# Copyright (c) 2023, Omar Habeeb and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymTrainer(FrappeTestCase):
	def test_gym_trainer(self):
	    test_gym_trainer=frappe.get_doc({
		     "doctype": "Gym Trainer",
			"first_name": "Omar",
			"last_name": "sexy",
			"trainer_id": "24294"
	 }).insert()