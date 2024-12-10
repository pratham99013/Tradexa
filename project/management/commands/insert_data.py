import threading
from django.core.management.base import BaseCommand
from django.db import transaction
from project.models import User, Order, Product


class Command(BaseCommand):
    help = 'Insert data into models concurrently'

    def insert_users(self):
        user_data = [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
            {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'},
            {'id': 4, 'name': 'David', 'email': 'david@example.com'},
            {'id': 5, 'name': 'Eve', 'email': 'eve@example.com'},
            {'id': 6, 'name': 'Frank', 'email': 'frank@example.com'},
            {'id': 7, 'name': 'Grace', 'email': 'grace@example.com'},
            {'id': 8, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 9, 'name': 'Henry', 'email': 'henry@example.com'},
            {'id': 10, 'name': '', 'email': 'jane@example.com'},
        ]

        for user in user_data:
            if not user['name'] or not user['email']:
                self.stdout.write(self.style.WARNING(f"Skipping invalid user: {user}"))
                continue
            try:
                User.objects.create(id=user['id'], name=user['name'], email=user['email'])
                self.stdout.write(self.style.SUCCESS(f"Inserted User {user['name']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error inserting User {user['name']}: {e}"))

    def insert_products(self):
        product_data = [
            {'id': 1, 'name': 'Laptop', 'price': 1000},
            {'id': 2, 'name': 'Smartphone', 'price': 700},
            {'id': 3, 'name': 'Headphones', 'price': 150},
            {'id': 4, 'name': 'Monitor', 'price': 300},
            {'id': 5, 'name': 'Keyboard', 'price': 50},
            {'id': 6, 'name': 'Mouse', 'price': 30},
            {'id': 7, 'name': 'Laptop', 'price': 1000},
            {'id': 8, 'name': 'SmartWatch', 'price': 250},
            {'id': 9, 'name': 'Gaming Chair', 'price': 500},
            {'id': 10, 'name': 'Earbuds', 'price': -50},
        ]

        for product in product_data:
            if product['price'] <= 0:
                self.stdout.write(self.style.WARNING(f"Skipping invalid product: {product}"))
                continue
            try:
                Product.objects.create(id=product['id'], name=product['name'], price=product['price'])
                self.stdout.write(self.style.SUCCESS(f"Inserted Product {product['name']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error inserting Product {product['name']}: {e}"))

    def insert_orders(self):
        order_data = [
            {'user_id': 1, 'product_id': 1, 'quantity': 2},
            {'user_id': 2, 'product_id': 2, 'quantity': 1},
            {'user_id': 3, 'product_id': 3, 'quantity': 5},
            {'user_id': 4, 'product_id': 4, 'quantity': 1},
            {'user_id': 5, 'product_id': 5, 'quantity': 3},
            {'user_id': 6, 'product_id': 6, 'quantity': 4},
            {'user_id': 7, 'product_id': 7, 'quantity': 2},
            {'user_id': 8, 'product_id': 8, 'quantity': 1},
            {'user_id': 9, 'product_id': 1, 'quantity': -1},
            {'user_id': 10, 'product_id': 11, 'quantity': 2},
        ]

        for order in order_data:
            try:
                if not User.objects.filter(id=order['user_id']).exists():
                    raise Exception(f"User with ID {order['user_id']} does not exist.")
                if not Product.objects.filter(id=order['product_id']).exists():
                    raise Exception(f"Product with ID {order['product_id']} does not exist.")

                Order.objects.create(
                    user_id=order['user_id'],
                    product_id=order['product_id'],
                    quantity=order['quantity']
                )
                self.stdout.write(self.style.SUCCESS(f"Inserted Order for User {order['user_id']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error inserting Order for User {order['user_id']}: {e}"))

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            user_thread = threading.Thread(target=self.insert_users)
            product_thread = threading.Thread(target=self.insert_products)
            order_thread = threading.Thread(target=self.insert_orders)

            user_thread.start()
            product_thread.start()
            order_thread.start()

            user_thread.join()
            product_thread.join()
            order_thread.join()

        self.stdout.write(self.style.SUCCESS('Data insertion completed successfully!'))
