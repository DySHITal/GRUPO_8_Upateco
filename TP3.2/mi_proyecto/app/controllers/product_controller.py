from ..models.product_model import Product
from flask import request

class productController:
    @classmethod
    def getproduct(self, product_id):
        Product(product_id=request.args.get('product_id'))
        prod = Product.get_product(product_id)
        return prod

    @classmethod
    def getproducts(self):
        brand_id = request.args.get('brand_id')
        category_id = request.args.get('category_id')

        if brand_id is not None:
            prod = Product.get_products_bid(brand_id)
            response = {
                'Products: ':prod,
                'Total': len(prod)
            }
            return response, 200
        
        elif category_id is not None:
            prod = Product.get_products_cid(category_id)
            response = {
                'Products: ':prod,
                'Total': len(prod)
            }
            return response, 200
        
        else:
            prod = Product.get_products()
            response = {
                'Products: ':prod,
                'Total: ':len(prod)
            }
            return response, 200
        
    @classmethod
    def regproduct(self):
        prod = Product(
            product_name= request.args.get('product_name', ''),
            brand_id= request.args.get('brand_id', ''),
            category_id= request.args.get('category_id', ''),
            model_year= request.args.get('model_year', ''),
            list_price= request.args.get('list_price', '')
        )
        Product.reg_product(prod)
        return {'msg': 'El producto se registró con éxito'}, 201
    
    @classmethod
    def modproduct(self, product_name, brand_id, category_id, model_year, list_price, product_id):
        Product(
            product_name=request.args.get('product_name'),
            brand_id=request.args.get('brand_id'),
            category_id=request.args.get('category_id'),
            model_year=request.args.get('model_year'),
            list_price=request.args.get('list_price'),
            product_id=request.args.get('product_id')
            )
        Product.mod_product(product_name, brand_id, category_id, model_year, list_price, product_id)
        return {'msg':'Producto modificado con éxito'}
    
    @classmethod
    def delproduct(self, product_id):
        Product(product_id=request.args.get('product_id'))
        Product.del_product(product_id)
        return {'msg':'El producto fué eliminado con éxito'}