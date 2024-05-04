from loan import loan
from loan.controllers import   loan_controller, home_controller, repayment_controller
from loan.controllers import customer_controller, officer_controller, admin_controller
    
if __name__ == "__main__":    
    # loan.run(debug=True)
    loan.run(host='0.0.0.0', port=5001, debug=True)
