from ..database import DatabaseConnection

class Product:
    def __init__(self, product_id = None, product_name = None, brand_id = None, category_id = None, model_year = None, list_price = None):
        self.product_id = product_id
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price

    @classmethod
    def get_product(cls, product_id):
        query = '''SELECT
         p.product_id,
         p.product_name,
         b.brand_name,
         c.category_name,
         p.model_year,
         p.list_price
         FROM products p 
         INNER JOIN brands b ON p.brand_id = b.brand_id
         INNER JOIN categories c ON p.category_id = c.category_id 
         WHERE p.product_id = %s
         '''
        params = (product_id,)
        result = DatabaseConnection.fetch_one(query, params, db_name = 'production')
        if result is not None:
            return{
                'product_id':product_id,
                'product_name':result[1],
                'brand':result[2],
                'category':result[3],
                'model_year':result[4],
                'list_price':result[5],
            }
        return {'msg':'Producto no encontrado'}, 404
    
    @classmethod
    def get_products_bid(cls, brand_id):
        query = '''SELECT
         p.product_id,
         p.product_name,
         b.brand_name,
         c.category_name,
         p.model_year,
         p.list_price
         FROM products p 
         INNER JOIN brands b ON p.brand_id = b.brand_id
         INNER JOIN categories c ON p.category_id = c.category_id 
         WHERE p.brand_id = %s
         '''
        params = (brand_id,)
        result = DatabaseConnection.fetch_all(query, params, db_name = 'production')
        if result is not None:
            return{
                'product_id':result[0],
                'product_name':result[1],
                'brand':brand_id,
                'category':result[3],
                'model_year':result[4],
                'list_price':result[5],
            }
        return {'msg':'Producto no encontrado'}, 404
    
    @classmethod
    def get_products_cid(cls, category_id):
        query = '''SELECT
         p.product_id,
         p.product_name,
         b.brand_name,
         c.category_name,
         p.model_year,
         p.list_price
         FROM products p 
         INNER JOIN brands b ON p.brand_id = b.brand_id
         INNER JOIN categories c ON p.category_id = c.category_id 
         WHERE p.category_id = %s
         '''
        params = (category_id,)
        result = DatabaseConnection.fetch_all(query, params, db_name = 'production')
        if result is not None:
            return{
                'product_id':result[0],
                'product_name':result[1],
                'brand':[2],
                'category':category_id,
                'model_year':result[4],
                'list_price':result[5],
            }
        return {'msg':'Producto no encontrado'}, 404
    
    @classmethod
    def get_products(cls):
        query = '''SELECT
         p.product_id,
         p.product_name,
         b.brand_name,
         c.category_name,
         p.model_year,
         p.list_price
         FROM products p 
         INNER JOIN brands b ON p.brand_id = b.brand_id
         INNER JOIN categories c ON p.category_id = c.category_id
         '''
        result = DatabaseConnection.fetch_all(query, db_name = 'production')
        if result is not None:
            return{
                'product_id':result[0],
                'product_name':result[1],
                'brand':[2],
                'category':[3],
                'model_year':result[4],
                'list_price':result[5],
            }
        return {'msg':'Producto no encontrado'}, 404
    
    @classmethod
    def reg_product(cls, prod):
        query = 'INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s)'
        params = (prod.product_name, prod.brand_id, prod.category_id, prod.model_year, prod.list_price)
        DatabaseConnection.execute_query(query, params, db_name='production')

    @classmethod
    def mod_product(cls, product_name, brand_id, category_id, model_year, list_price, product_id):
        query = '''UPDATE production.products
        SET product_name = %s, brand_id = %s, category_id = %s, model_year = %s, list_price = %s
        WHERE product_id = %s
        '''
        params = (product_name, brand_id, category_id, model_year, list_price, product_id)
        DatabaseConnection.execute_query(query, params, db_name='production')

    @classmethod
    def del_product(cls, product_id):
        query = '''DELETE FROM products p
        INNER JOIN brands b ON p.brand_id = b.brand_id
        INNER JOIN categories c ON p.category_id = c.category_id
        WHERE p.product_id = %s
        '''
        params = (product_id,)
        DatabaseConnection.execute_query(query, params, db_name='production')