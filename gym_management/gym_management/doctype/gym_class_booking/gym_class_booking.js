// Copyright (c) 2023, Omar Habeeb and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Class Booking", {
    after_save: function(frm) {

        frappe.msgprint("Your class has been booked, Enjoy Building with *GOLD* GYM")
       // frappe.throw("This is an error")

},
});
