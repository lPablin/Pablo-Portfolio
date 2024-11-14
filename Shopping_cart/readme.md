
# 🛒 Shopping Cart System with Object-Oriented Programming 
This project implements a basic shopping system in Python, designed to simulate the process of purchasing products with limited stock. The system allows users to manage a shopping cart, control product stock, and calculate the total cost of items in the cart.

## 🧑‍💻 Project Overview:

The system includes the following core features:

- Creating a shopping cart: Users can create a cart to begin adding items.
- Adding products to the cart: Products can be selected from a store's inventory and added to the cart.
- Controlling product stock: The stock is tracked, and the system prevents users from exceeding available stock for any product.
- Removing products from the cart: Users can remove items partially or entirely from the cart.
- Cart details: The cart displays a list of products, cost per item, total cost, and more.

## 🏷️ Key Classes:

- Product: The class representing each product, with attributes like name, available quantity (stock), and price.
- Store: A class to manage the inventory of products. The store is only accessible for modifications by the owner.
- Cart: Represents the customer's shopping cart, where items are added, removed, and stock is controlled.
- Shopping System: The main system integrating all classes to allow users to interact with the store, add items to their cart, check stock, and perform checkout operations.

## 🔒 Access Control:

Customers can only interact with the Shopping System class, which integrates the functionality of the products and cart. This ensures proper access control and security in managing the cart and inventory.

