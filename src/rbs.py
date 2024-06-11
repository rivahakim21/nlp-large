from datetime import datetime
import csv
def handle_intent(intent):
    # Dictionary berisi fungsi penangan untuk setiap intent
    intent_handlers = {
        "create_account": handle_create_account,
        "delete_account": handle_delete_account,
        "edit_account": handle_edit_account,
        "recover_password": handle_recover_password,
        "registration_problems": handle_registration_problems,
        "switch_account": handle_switch_account,
        "place_order": handle_place_order,
        "change_order": handle_change_order,
        "cancel_order": handle_cancel_order,
        "track_order": handle_track_order,
        "contact_customer_service": handle_contact_customer_service,
        "contact_human_agent": handle_contact_human_agent,
        "complaint": handle_complaint,
        "review": handle_review,
        "delivery_options": handle_delivery_options,
        "delivery_period": handle_delivery_period,
        "check_cancellation_fee": handle_check_cancellation_fee,
        "check_payment_methods": handle_check_payment_methods,
        "payment_issue": handle_payment_issue,
        "check_refund_policy": handle_check_refund_policy,
        "get_refund": handle_get_refund,
        "track_refund": handle_track_refund,
        "change_shipping_address": handle_change_shipping_address,
        "set_up_shipping_address": handle_set_up_shipping_address
    }

    # Panggil fungsi penangan yang sesuai dengan intent yang diberikan
    handler = intent_handlers.get(intent, handle_unknown_intent)
    return handler()

# Fungsi penangan untuk setiap intent
def handle_create_account():
    return "To create an account, please provide your email and choose a password. You will receive a confirmation email to complete the registration."

def handle_delete_account():
    return "If you'd like to delete your account, please confirm your identity and we'll proceed with the deletion. Note that this action cannot be undone."

def handle_edit_account():
    return "To edit your account details, please log in and navigate to the 'Account Settings' section. You can update your personal information there."

def handle_recover_password():
    return "To recover your password, please enter your email address. We'll send you a password reset link to your registered email."

def handle_registration_problems():
    return "If you're experiencing issues with registration, please let us know the error message or problem, and we'll assist you further."

def handle_switch_account():
    return "To switch accounts, log out of your current account and log in with your other account's credentials."

def handle_place_order():
    return "To place an order, add the items to your cart and proceed to checkout. Follow the prompts to complete your purchase."

def handle_change_order():
    return "To change an existing order, please contact our customer service with your order number and the changes you'd like to make."

def handle_cancel_order():
    return "To cancel an order, contact customer service with your order number. Cancellations are possible before the order is shipped."

def handle_track_order():
    return "To track your order, enter your order number on our website's tracking page. You'll see the current status of your order."

def handle_contact_customer_service():
    return "To contact customer service, you can use our online chat, email us at [email address], or call our support hotline at [phone number]."

def handle_contact_human_agent():
    return "Connecting you to a human agent. Please wait while we transfer you to a customer service representative."

def handle_complaint():
    return "We're sorry to hear that you're experiencing issues. Please let us know the details of your complaint, and we'll work to resolve it."

def handle_review():
    return "Thank you for your feedback! If you'd like to leave a review, you can do so on our website or through our app."

def handle_delivery_options():
    return "We offer various delivery options, including standard, express, and next-day delivery. You can select your preferred option at checkout."

def handle_delivery_period():
    return "Delivery times depend on your location and the shipping method chosen. Standard delivery usually takes 3-5 business days."

def handle_check_cancellation_fee():
    return "Cancellation fees depend on the order's status. If it's already been processed, a fee might apply. Contact customer service for details."

def handle_check_payment_methods():
    return "We accept various payment methods, including credit/debit cards, PayPal, and bank transfers. Check our website for more details."

def handle_payment_issue():
    return "If you're experiencing payment issues, make sure your payment method is valid and has sufficient funds. If the problem persists, contact customer service."

def handle_check_refund_policy():
    return "Our refund policy allows returns within 30 days of purchase, provided the item is in its original condition. Contact customer service for more details."

def handle_get_refund():
    return "To request a refund, contact customer service with your order number and the reason for the refund. We'll guide you through the process."

def handle_track_refund():
    return "To track your refund, enter your refund request number on our website's tracking page. You'll see the status of your refund request."

def handle_change_shipping_address():
    return "To change your shipping address, log into your account and update your address details. Note that changes may not be possible once the order is processed."

def handle_set_up_shipping_address():
    return "To set up a new shipping address, add it to your account under 'Shipping Addresses.' You can select this address during checkout."

# Fungsi untuk menangani intent yang tidak dikenali
def handle_unknown_intent():
    return "I'm sorry, I didn't understand that. Could you please rephrase or contact customer service for further assistance?"



def record_data(intent, sentiment):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [current_time, intent, sentiment]
    
    with open('../model/sentiment_analysis/record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
def get_response(intent, sentiment):
    record_data(intent,sentiment)
    if sentiment == 'negative':
        response = handle_intent(intent)
        response = response+' Please contact our live agent for more information.'
        return response
    else:
        response = handle_intent(intent)
        return response