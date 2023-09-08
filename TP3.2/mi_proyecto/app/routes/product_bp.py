from flask import Blueprint
from ..controllers.product_controller import productController

product_bp = Blueprint('product_bp', __name__)

product_bp.route('/products/<int:product_id>', methods = ['GET'])(productController.getproduct)
product_bp.route('/products/<int:product_id>', methods = ['PUT'])(productController.modproduct)
product_bp.route('/products/<int:product_id>', methods = ['DELETE'])(productController.delproduct)
product_bp.route('/products', methods = ['GET'])(productController.getproducts)
product_bp.route('/products', methods = ['POST'])(productController.regproduct)