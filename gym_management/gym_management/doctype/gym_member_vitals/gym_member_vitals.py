# Copyright (c) 2023, Omar Habeeb and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class GymMemberVitals(Document):
	#BMI Calculate
	def before_save(self):
		if self.height:
			self.bmi = (self.weight / (self.height * self.height))
		return self.bmi

	