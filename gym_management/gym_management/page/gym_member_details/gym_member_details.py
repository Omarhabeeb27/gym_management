import frappe


@frappe.whitelist()

def get_data(gym_member):
     member_info = frappe.get_doc("Gym Member", gym_member)
     membership_info = frappe.db.get_list("Gym Membership", fields=["*"], filters={"gym_member": gym_member}, limit=1)

     return {"gym_member": member_info, "gym_membership": membership_info}