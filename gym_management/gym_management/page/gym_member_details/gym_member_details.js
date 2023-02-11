frappe.pages['gym-member-details'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Gym member details',
		single_column: true
	});

	let gym_member = page.add_field(
			{
				label: "Gym Member",
				fieldname: "gym_member",
				fieldtype: "Link",
				options: "Gym Member",
				change: () => {
					frappe.call('gym_management.gym_management.page.gym_member_details.gym_member_details.get_data', {
						gym_member: gym_member.get_value()
					}).then(r => {
						if (r) {
							console.log(r)
							var html = frappe.render_template("gym_member_details", { data: r.message })
							$(html).appendTo(page.body)
						} else {
							 $(frappe.render_template("gym_member_details")).appendTo(page.body.addClass("no-border"));
						}
					})
	
					
				}
			}
		)
			
	}
