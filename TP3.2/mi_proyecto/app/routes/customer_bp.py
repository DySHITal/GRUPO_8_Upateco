from flask import Blueprint
from ..controllers.customer_controller import CustomerController

customer_bp = Blueprint('customer_bp', __name__)

customer_bp.route('/customers', methods = ['GET', 'POST'])(CustomerController.getcustomers)
# customer_bp.route('/customers', methods = ['POST'])(CustomerController.createcustomer)
customer_bp.route('/customers/<int:customer_id>', methods = ['GET'])(CustomerController.getcustomer)
customer_bp.route('/customers/<int:customer_id>', methods = ['PUT'])(CustomerController.modifycustomer)
customer_bp.route('/customers/<int:customer_id>', methods = ['DELETE'])(CustomerController.deletecustomer)
customer_bp.route('/customers/<string:state>', methods = ['GET'])(CustomerController.getcustomers_state)