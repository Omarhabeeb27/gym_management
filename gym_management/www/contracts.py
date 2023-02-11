import frappe
from frappe import _
import frappe.www.list
from frappe.utils import getdate
from gym_management.gym_management.doctype.gym_membership.gym_membership import get_plan_status, get_days_left_in_plan

no_cache = 1

def get_context(context):
    
   
    # extract the list of contracts for member, some are virtual attributes so need to recalculate as not in DB call
    contracts = frappe.get_list("Gym Membership", fields=["*"], order_by='start_date DESC')
    curr_contracts = []
    for contract in contracts:
        status = get_plan_status(contract.start_date, contract.end_date)
        days_left = get_days_left_in_plan(contract.end_date)
        contract.update({ "contract_status": status})
        contract.update({"days_left": days_left})
        if status == "Active":
            contract.update({ "badge": "badge badge-success"})
        elif status == "Expired":
            contract.update({ "badge": "badge badge-pill badge-warning"})
        elif status == "Not Started":
            contract.update({ "badge": "badge badge-pill badge-info"})
        curr_contracts.append(contract)  

    context.contracts = curr_contracts

    
