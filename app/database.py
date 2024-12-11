from tinydb import TinyDB

database = TinyDB("app/data_base.json", indent=4)


if __name__ == "__main__":
    query1 = {"name": "Order Form",
             "fields": {"user_email": "email", "user_phone": "phone",
                        "order_date": "date"}}
    query2 = {"name": "Registration Form",
              "fields": {"email": "email", "phone": "phone"}}

    if not database.all():
        database.insert(query1)
        database.insert(query2)