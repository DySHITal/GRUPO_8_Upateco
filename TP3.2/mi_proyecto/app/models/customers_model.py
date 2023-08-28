from ..database import DatabaseConnection

class Customer:
    def __init__(self, customer_id = None, first_name = None, last_name = None, email = None, phone = None, street = None, city = None, state = None, zip_code = None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    @classmethod
    def get_customer(cls, customer_id):
        query = 'SELECT * FROM sales.customers WHERE customer_id = %s'
        params = (customer_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return{
                'id': customer_id,
                'Nombre': result[1],
                'Apellido': result[2],
                'Email': result[3],
                'Telefono': result[4],
                'Calle': result[5],
                'Ciudad': result[6],
                'Provincia': result[7],
                'Códifo Postal': result[8]
            }
        return {'msg':'Cliente no encontrado'}, 404
    
    @classmethod
    def get_customers_state(cls, state):
        query = 'SELECT * FROM sales.customers WHERE state = %s'
        params = (state,)
        result = DatabaseConnection.fetch_all(query, params)
        if result is not None:
            return{
                'id': result[0],
                'Nombre': result[1],
                'Apellido': result[2],
                'Email': result[3],
                'Telefono': result[4],
                'Calle': result[5],
                'Ciudad': result[6],
                'Provincia': result[7],
                'Códifo Postal': result[8]
            }
        return {'msg':'Clientes no encontrados'}, 404
    
    @classmethod
    def get_customers(cls):
        query = 'SELECT * FROM sales.customers'
        result = DatabaseConnection.fetch_all(query)
        if result is not None:
            return{
                'id': result[0],
                'Nombre': result[1],
                'Apellido': result[2],
                'Email': result[3],
                'Telefono': result[4],
                'Calle': result[5],
                'Ciudad': result[6],
                'Provincia': result[7],
                'Códifo Postal': result[8]
            }
        return {'msg':'Clientes no encontrados'}, 404
    
    @classmethod
    def create_customers(cls, customer):
        query = 'INSERT INTO sales.customers (first_name, last_name, email, phone, street, city, state, zip_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        params = (customer.first_name, customer.last_name, customer.email, customer.phone, customer.street, customer.city, customer.state, customer.zip_code)
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def modify_customer(cls, first_name, last_name, email, phone, street, city, state, zip_code, customer_id):
        query = '''UPDATE sales.customers 
        SET first_name = %s, last_name = %s, email = %s, phone = %s, street = %s, city = %s, state = %s, zip_code = %s
        WHERE customer_id = %s
        '''
        params = (first_name, last_name, email, phone, street, city, state, zip_code, customer_id)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete_customer(cls, customer_id):
        query = 'DELETE FROM sales.customers WHERE customer_id = %s'
        params = (customer_id,)
        DatabaseConnection.execute_query(query, params)