# Evaluation Results

## Scoring Rubric

## Evaluation Method

Each response was manually evaluated based on relevance, coherence, and helpfulness. Scores were assigned on a scale of 1 to 5 for each criterion.

- Relevance (1-5): How well the response answers the query
- Coherence (1-5): Grammar and clarity
- Helpfulness (1-5): Practical usefulness

---

## Score Summary Table

| Query | Method     | Relevance | Coherence | Helpfulness |
|-------|-----------|----------|----------|-------------|
| 1     | Zero-Shot | 5        | 5        | 5           |
| 1     | One-Shot  | 5        | 5        | 4           |
| 2     | Zero-Shot | 4        | 5        | 4           |
| 2     | One-Shot  | 5        | 5        | 4           |
| 3     | Zero-Shot | 5        | 5        | 5           |
| 3     | One-Shot  | 5        | 5        | 5           |
| 4     | Zero-Shot | 4        | 5        | 4           |
| 4     | One-Shot  | 5        | 5        | 4           |
| 5     | Zero-Shot | 5        | 5        | 4           |
| 5     | One-Shot  | 5        | 5        | 5           |
| 6     | Zero-Shot | 5        | 5        | 5           |
| 6     | One-Shot  | 5        | 5        | 5           |
| 7     | Zero-Shot | 4        | 5        | 3           |
| 7     | One-Shot  | 4        | 5        | 3           |
| 8     | Zero-Shot | 4        | 4        | 4           |
| 8     | One-Shot  | 5        | 5        | 4           |
| 9     | Zero-Shot | 4        | 5        | 4           |
| 9     | One-Shot  | 5        | 5        | 4           |
| 10    | Zero-Shot | 5        | 5        | 4           |
| 10    | One-Shot  | 5        | 5        | 4           |
| 11    | Zero-Shot | 5        | 5        | 5           |
| 11    | One-Shot  | 5        | 5        | 5           |
| 12    | Zero-Shot | 5        | 5        | 4           |
| 12    | One-Shot  | 5        | 5        | 5           |
| 13    | Zero-Shot | 4        | 5        | 3           |
| 13    | One-Shot  | 5        | 5        | 4           |
| 14    | Zero-Shot | 5        | 5        | 5           |
| 14    | One-Shot  | 5        | 5        | 5           |
| 15    | Zero-Shot | 5        | 5        | 4           |
| 15    | One-Shot  | 5        | 5        | 4           |
| 16    | Zero-Shot | 5        | 5        | 5           |
| 16    | One-Shot  | 5        | 5        | 5           |
| 17    | Zero-Shot | 4        | 5        | 4           |
| 17    | One-Shot  | 4        | 5        | 3           |
| 18    | Zero-Shot | 5        | 5        | 5           |
| 18    | One-Shot  | 5        | 5        | 4           |
| 19    | Zero-Shot | 5        | 5        | 5           |
| 19    | One-Shot  | 5        | 5        | 5           |
| 20    | Zero-Shot | 5        | 5        | 4           |
| 20    | One-Shot  | 5        | 5        | 4           |

---

## Observations

- One-shot prompting generally produced more consistent and structured responses.
- Zero-shot responses were sometimes more detailed but less predictable.
- Both approaches performed well in coherence and grammar.
- One-shot responses slightly improved relevance and helpfulness in most cases.

---

## Conclusion

The Llama 3.2 (3B) model performs effectively for offline customer support tasks.  
One-shot prompting enhances response quality by guiding the model with examples.

Overall, the system demonstrates that local LLMs can be a viable solution for privacy-focused applications.

---

## Query 1
**Customer Query:** How can I track my order?

### Zero-Shot Response:
To track your order on ShopSmart, please follow these steps:

1. Log in to your account on our website.
2. Click on the "Order History" tab at the top of the page.
3. Select the specific order you'd like to track from the list of recent orders.
4. Click on the "Track Order" button next to the order number.
5. You will be redirected to a tracking page where you can enter your shipping address and receive real-time updates on the status of your package.

If you need any further assistance, feel free to contact us!

### One-Shot Response:
"Once your order ships, you'll receive an email with tracking information. You can use this to monitor the status of your package on the shipping carrier's website. If you have any issues or concerns, feel free to reply to the original shipment notification email and our support team will be happy to help."

---

## Query 2
**Customer Query:** My discount code is not working at checkout.

### Zero-Shot Response:
I'm so sorry to hear that your discount code isn't working at checkout.

To help resolve the issue, could you please provide me with the following details:

1. The name of the discount code you're trying to use.
2. The error message you're seeing on the screen (if any).
3. The specific items in your cart where you're applying the code.

I'll do my best to look into this for you and get you a refund or an alternative solution as soon as possible!

### One-Shot Response:
"Sorry to hear that your discount code isn't working. Can you please provide me with the details of the code and the error message you're seeing? I'll do my best to help you troubleshoot or look into an alternative solution."

---

## Query 3
**Customer Query:** What is your return policy?

### Zero-Shot Response:
At ShopSmart, we want you to be completely satisfied with your purchase. Our return policy allows you to return or exchange items within 30 days of delivery.

To initiate a return, please contact our customer service team via phone, email, or live chat within the 30-day timeframe. We will provide a Return Merchandise Authorization (RMA) number and instructions on how to proceed with the return process.

Items must be in their original condition, with all tags, packaging, and accessories included. Refunds will be issued in the original payment method, minus any shipping costs.

If you have any questions or concerns about our return policy, feel free to ask!

### One-Shot Response:
"We offer a 30-day return policy for unused items with original packaging. You can initiate a return from your account or contact our dedicated customer support team for assistance."

---

## Query 4
**Customer Query:** Can I cancel my order after placing it?

### Zero-Shot Response:
"Hello! Unfortunately, we can't cancel orders once they've shipped. However, if you haven't received your order yet, please contact us immediately so we can try to resolve the issue and get a replacement or refund for you. Please have your order number ready when you reach out."

### One-Shot Response:
"Please note that we try to process orders as quickly as possible, and cancellations may not always be possible once the order has been processed. However, if you would like to initiate a return or make changes to your order before it ships, please contact our support team and we'll do our best to accommodate your request."

---

## Query 5
**Customer Query:** How long does shipping take?

### Zero-Shot Response:
At ShopSmart, we strive to get your orders to you as quickly as possible.

Our standard shipping options include:

* Expedited Shipping (3-5 business days): $9.99
* Express Shipping (2 business days): $19.99

Please note that these times are estimates and may vary depending on your location. You can track the status of your order on our website once it's shipped.

If you have any further questions or concerns, feel free to ask!

### One-Shot Response:
"Typically, orders are processed and shipped within 24-48 hours of receiving payment. Standard shipping takes 3-7 business days, while express shipping is available for an additional fee and typically arrives in 1-2 business days."

---

## Query 6
**Customer Query:** I received a damaged product. What should I do?

### Zero-Shot Response:
Thank you for reaching out to ShopSmart!

We apologize for the inconvenience of receiving a damaged product. To resolve this issue, please follow these steps:

1. Take a clear photo of the damaged item and send it to us at [support@shopsmart.com](mailto:support@shopsmart.com).
2. Contact our Customer Service team via phone at 1-800-SHOPS-ME (1-800-746-7663) or reply to this email, and we'll guide you through the next steps.
3. We'll provide a return shipping label, so you can send the damaged item back to us for a full refund or exchange it for a new product.

Your satisfaction is our top priority. We appreciate your patience and cooperation in resolving this issue.

Thank you for shopping with ShopSmart!

### One-Shot Response:
"Sorry to hear that you received a damaged product. Please contact our support team immediately so we can assist you with a replacement or store credit. You'll need to provide us with your order number and photos of the damage for our review. We'll take care of the issue promptly."

---

## Query 7
**Customer Query:** Do you offer cash on delivery?

### Zero-Shot Response:
"Hello! Yes, we do offer cash on delivery (COD) option for certain orders. However, COD is only available on orders exceeding a minimum amount of ₹1,500. Please check the shipping details and payment options during checkout to confirm if COD is an option for your order."

### One-Shot Response:
"Unfortunately, we do not offer cash on delivery at this time. However, you can choose to have your order delivered and pay by credit card, debit card, or other accepted payment methods."

---

## Query 8
**Customer Query:** How can I change my delivery address?

### Zero-Shot Response:
"Hello! Thanks for reaching out to ShopSmart. To update your delivery address, simply log in to your account on our website, go to 'My Account' and click on 'Order History'. Find the order you'd like to update, then click on 'Edit Address' next to it. Enter your new address details and we'll do our best to make the changes for you. If you need any help or have questions, feel free to ask!

### One-Shot Response:
"Before you make any changes, please note that we require a minimum of 3 working days' notice to update your delivery address. You can do this by logging into your account, going to 'Order History', selecting the order for which you'd like to change the address, and clicking 'Edit Delivery Address'. Alternatively, you can contact our support team via phone or email with your new address details, and we'll be happy to assist you."

---

## Query 9
**Customer Query:** My payment was deducted but order not confirmed.

### Zero-Shot Response:
"Hello! Sorry to hear that your payment wasn't reflected in the confirmation of your order. Can you please provide me with your Order Number so I can look into this further for you? Additionally, were you able to complete your purchase successfully or did it fail somewhere along the way?"

### One-Shot Response:
"We apologize for the inconvenience. Please check your email for the confirmation message that may have been sent to you once the order was processed. If you didn't receive it, please contact our support team and we'll be happy to help you track down your order or resubmit it for processing."

---

## Query 10
**Customer Query:** Do you have international shipping?

### Zero-Shot Response:
"Yes, we do offer international shipping! We partner with reliable carriers to deliver our products worldwide. Please note that international shipping rates and estimated delivery times may vary depending on your location. Would you like me to provide more information on our international shipping options?"

### One-Shot Response:
"Yes, we offer international shipping to many countries worldwide. Please note that shipping rates and delivery times may vary depending on your location. For more information, please visit our shipping page or contact us directly."

---

## Query 11
**Customer Query:** How do I apply a coupon code?

### Zero-Shot Response:
To apply a coupon code on ShopSmart, simply follow these steps:

1. Add the item you'd like to purchase to your shopping cart.
2. On our checkout page, click on the "Apply Coupon" button below the subtotal section.
3. Enter your coupon code in the designated box and select it from the dropdown list if available.
4. Click "Apply" to see the updated subtotal and any applicable discounts.

If you're having trouble entering your code or need assistance with another issue, feel free to ask!

### One-Shot Response:
"To apply a coupon code, simply navigate to the product page where you'd like to apply the discount and look for the 'Apply Coupon' or 'Use Discount Code' field. Enter your coupon code in the designated box and click 'Apply'. The discount amount will be applied automatically. If you have any issues applying the code, feel free to contact support for assistance."

---

## Query 12
**Customer Query:** Can I exchange a product for a different size?

### Zero-Shot Response:
Hello! At ShopSmart, we want to ensure you get the best fit. Yes, you can definitely exchange a product for a different size. Please see our return policy page (link provided) for more information on how to initiate an exchange and any applicable restocking fees. If you have any questions or need assistance with the process, feel free to reply to this message or give us a call at [phone number].

### One-Shot Response:
"Yes, we offer exchanges for different sizes on many of our products. Please ensure the item is in its original condition with all tags and packaging intact. You can initiate an exchange from your account or contact support to receive a return shipping label and instructions."

---

## Query 13
**Customer Query:** Why is my order delayed?

### Zero-Shot Response:
"Hi there! Sorry to hear that your order is delayed. We're here to help. Could you please provide us with your order number so we can look into this further? Additionally, did the delay start after a specific date or was it always expected?"

### One-Shot Response:
"We apologize for the delay in your order. Our system indicates that there might have been an issue with inventory availability or shipping processing time. We're investigating this matter and will provide you with a revised estimated delivery date as soon as possible."

---

## Query 14
**Customer Query:** How can I contact customer support?

### Zero-Shot Response:
At ShopSmart, we're here to help. You can contact our customer support team in three easy ways:

1. **Email**: Send us an email at [support@shopsmart.com](mailto:support@shopsmart.com) and we'll respond within 24-48 hours.
2. **Live Chat**: Click the "Chat with Us" button on our website and we'll connect you with a representative in real-time.
3. **Phone**: Call us at 1-800-SHOPSMART (1-800-746-6768) Monday to Friday, 9am to 6pm EST.

We're always here to help!

### One-Shot Response:
"We have multiple ways to get in touch with us! You can reach us through our website's 'Contact Us' page, where you'll find a form to fill out and submit your query. Alternatively, you can send an email directly to [support@shopsmart.com](mailto:support@shopsmart.com). If you prefer to speak with someone, feel free to call or text us at 1-800-SHOPSMART (1-800-746-7767) during our business hours. We're here to help!"

---

## Query 15
**Customer Query:** Is there any warranty on your products?

### Zero-Shot Response:
"Yes, ShopSmart offers a 1-year limited warranty on most of our products. This warranty covers manufacturing defects and provides repair or replacement options if a product fails to function as expected within the first year of purchase. For more information and details about our warranty policy, please visit our FAQ section or contact us directly."

### One-Shot Response:
"We stand behind the quality of our products, and most items come with a 1-year limited warranty covering manufacturing defects. For more information on warranties and specific product details, please visit our Help & Support section or contact us directly."

---

## Query 16
**Customer Query:** How do I reset my account password?

### Zero-Shot Response:
To reset your account password on ShopSmart, please follow these steps:

1. Go to the login page and click on "Forgot Password" below the login fields.
2. Enter your email address or username associated with your account.
3. Click "Send Reset Link".
4. Check your inbox for an email from ShopSmart with a password reset link.
5. Click on the link, then create a new password and confirm it.

If you have any issues or need assistance, feel free to reply to this email or contact our customer support team at [support@shopsmart.com](mailto:support@shopsmart.com). We're here to help!

### One-Shot Response:
"Please click on the 'Forgot Password' link on our login page, enter your email address associated with your account, and follow the instructions to reset your password. If you need further assistance, contact our support team."

---

## Query 17
**Customer Query:** Can I return a product without the original packaging?

### Zero-Shot Response:
At ShopSmart, we strive to make returns as easy as possible for you.

According to our return policy, you can return a product without its original packaging. However, please note that the product must be in its original condition with all tags attached and in its original box or packaging material whenever possible.

Please package the item securely and include a copy of your order number and a brief explanation of why you're returning the item. We'll process your return as soon as we receive it.

If you have any further questions, feel free to ask!

### One-Shot Response:
"Unfortunately, our return policy states that all returned items must have their original packaging and tags attached. If you're unable to return an item with its original packaging, we can offer an exchange or store credit for the item's full value upon receipt of replacement packaging."

---

## Query 18
**Customer Query:** What payment methods do you accept?

### Zero-Shot Response:
At ShopSmart, we accept a variety of payment methods to ensure your purchase experience is smooth and secure. Here are the payment options we currently offer:

1. Visa Credit Card
2. Mastercard Credit/Debit Card
3. American Express Credit/Debit Card
4. PayPal (personal and business accounts)
5. Apple Pay
6. Google Pay

If you have any questions or concerns about a specific payment method, feel free to ask!

### One-Shot Response:
"We accept major credit cards (Visa, Mastercard, Amex), PayPal, and ShopSmart's own payment option, which allows for secure and convenient checkout. We also offer financing options for eligible orders."

---

## Query 19
**Customer Query:** How do I check my order history?

### Zero-Shot Response:
"Hi there! You can easily check your order history on our website by following these steps:

1. Log in to your account at shopsmart.com.
2. Click on the 'Account' dropdown menu at the top right corner of the page.
3. Select 'Order History' from the drop-down menu.
4. You'll see a list of all your past orders, including order dates, totals, and status.

If you have any trouble finding this information or need further assistance, feel free to ask!"

### One-Shot Response:
"Simply log in to your ShopSmart account, click on the 'Order History' tab, and you'll be able to view a list of all your past orders, including details such as order date, product information, and shipping status."

---

## Query 20
**Customer Query:** Can I place an order without creating an account?

### Zero-Shot Response:
Yes, you can place an order on our website without creating an account. Simply proceed to checkout and follow the payment instructions. However, please note that you won't be able to track your order or access any exclusive offers if you don't have an account. Would you like me to guide you through the checkout process?

### One-Shot Response:
"Although we recommend creating an account for a smoother shopping experience, you can still place an order as a guest. However, some benefits like saved payment methods and order history will not be available to you."

---

