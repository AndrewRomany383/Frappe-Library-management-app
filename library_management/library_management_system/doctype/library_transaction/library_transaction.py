# Copyright (c) 2024, Andrew Romany and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):

	def before_submit(self):
		if self.type == 'Issue':
			self.validate_issue()
			# set the article status to be Issued
			article = frappe.get_doc("Article", self.article)
			article.status = "Issued"
			article.save()

		elif self.type == "Return":
			self.validate_return()
			# setting the article status to 'Available'
			article = frappe.get_doc("Article", self.article)
			article.status = "Available"
			article.save()

	def validate_issue(self):
		self.validate_membership()
		# check if the article is issued
		article = frappe.get_doc("Article", self.article)
		if article.status == "Issued":
			frappe.throw("Article is already issued by another member ")

	def validate_return(self):
		# check if the article is already available
		article = frappe.get_doc("Article", self.article)
		if article.status == "Available":
			frappe.throw("Article is already available")

	def validate_maximum_limit(self):
		max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
		count = frappe.db.count(
			"Library Transaction",
			{
				"library_member": self.library_member,
				"type": "Issue",
				"docstatus": DocStatus.submitted()
			},
		)
		if count > max_articles:
			frappe.throw("Member has already reached the maximum limit of articles")

	def validate_membership(self):
		# check if the member has valid membership
		existing_valid_membership = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				"from_date": ("<", self.date),
				"to_date": (">", self.date)
			}
		)
		if not existing_valid_membership:
			frappe.throw("Member does not have a valid membership")
