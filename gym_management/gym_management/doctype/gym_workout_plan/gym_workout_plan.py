# Copyright (c) 2023, Omar Habeeb and contributors
# For license information, please see license.txt

#import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class GymWorkoutPlan(WebsiteGenerator):
	# set the route for the workout plan
	def before_save(self):
		if not self.route:
			self.route = f"/workout/{self.name}"