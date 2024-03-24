import frappe


# Getting all data of article Doctype with ORM
@frappe.whitelist(allow_guest=True)
def get_all_articles_by_specific_fields_by_orm():
	articles = frappe.get_all("Article", fields=["article_name", "auther", "status"])
	return articles


# Getting all data of article Doctype with ORM
@frappe.whitelist(allow_guest=True)
def get_all_articles_by_all_fields_by_orm():
	articles = frappe.get_all("Article", fields=["*"])
	return articles


# Getting all data of article Doctype with SQL
@frappe.whitelist(allow_guest=True)
def get_all_articles_by_all_fields_by_sql():
	articles = frappe.db.sql("""SELECT * FROM tabArticle;""", as_dict=True)
	return articles


# Getting some data of article Doctype with SQL
@frappe.whitelist(allow_guest=True)
def get_all_articles_by_specific_fields_by_sql():
	articles = frappe.db.sql("""SELECT article_name, auther, status FROM tabArticle;""", as_dict=True)
	return articles


