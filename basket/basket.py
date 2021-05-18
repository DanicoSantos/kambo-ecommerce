

from store.models import Product


class Basket():
    """
    A base Basket class, providing some default behaviors that 
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, quantity):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id
        quantity = quantity

        if product_id not in self.basket:
            self.basket[product_id] = {'price': float(
                product.price), 'quantity': quantity}
        else:
            self.basket[product_id]['quantity'] = quantity

        self.save()

    def delete(self, product_id):
        """
        Delete item from session data
        """
        product_id = str(product_id)

        if product_id in self.basket:
            del self.basket[product_id]
        
        self.save()
    
    def update(self, product_id, quantity):
        """
        Update values in session data
        """
        product_id = str(product_id)
        quantity = quantity

        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity

        self.save()
    
    def save(self):
        self.session.modified = True

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database and
        return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        return sum(item.get('quantity') for item in self.basket.values())

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.basket.values())
