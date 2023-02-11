# Copyright (c) 2023, Omar Habeeb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, date_diff

class GymMembership(Document):
	# Virtual property on contract to evaluate contract status
	@property
	def plan_status(self):
		return get_plan_status(self.start_date, self.end_date)

	# Virtual property to calculate days left in contract
	@property
	def days_left(self):
		return get_days_left_in_plan(self.end_date)	

@frappe.whitelist()
def get_plan_status(start_date, end_date):
	today = getdate()
	end = getdate(end_date)
	start = getdate(start_date)
	if end < today:
		return "Expired"
	elif start > today:	
		return "Not Started"
	else:
		return "Active"	

@frappe.whitelist()
def get_days_left_in_plan(end_date):
	if end_date:
		today = getdate()
		end = getdate(end_date)
		days_left = date_diff(end,today)
	else:
		return 0	
	
	if days_left < 0:
		return 0
	else:	
		return days_left