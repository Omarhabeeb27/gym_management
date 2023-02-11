import frappe

def get_context(context):
    context.workouts = frappe.get_list("Gym Workout Plan", fields=["plan_name", "description","photo", "route"])
    frappe.log(context.workouts)