import streamlit as st


def main():
    st.title("Factory Design Pattern | Creational")
    st.info("""
        The Factory design pattern is a creational design pattern that provides 
        an interface for creating objects in a super class, but allows subclasses 
        to alter the type of objects that will be created. It enables the creation 
        of objects without specifying the exact class of object that will be created.
    """)

    st.subheader("Explanation")

    st.write("""
        In this example, the 'Product' interface declares the operations that 
        all concrete products must implement. The 'ConcreteProduct' classes provide 
        various implementations of the 'Product' interface.
    """)

    st.write("""
        The 'Creator' class declares the factory method that is supposed to return an 
        object of type 'Product', but the implementation of this method is provided 
        by the 'ConcreteCreator' classes.
    """)

    st.write("""
        The 'Client' code uses the 'Creator' class and the 'ConcreteCreator' classes, 
        but is unaware of the specific type of 'Product' that will be created.
    """)

    st.write("---")

    st.subheader("Implementation")

    st.code("""
from abc import ABC, abstractmethod

# The Product interface declares the operations that all concrete products must implement.
class Product(ABC):
  @abstractmethod
  def operation(self):
    pass

# Concrete Products provide various implementations of the Product interface.
class ConcreteProductA(Product):
  def operation(self):
    return "Result of the ConcreteProductA operation"

class ConcreteProductB(Product):
  def operation(self):
    return "Result of the ConcreteProductB operation"

# The Creator class declares the factory method that is supposed to return an object of type Product.
# The Creator's subclasses usually provide the implementation of this method.
class Creator(ABC):
  @abstractmethod
  def factory_method(self):
    pass

  def some_operation(self):
    # Call the factory method to create a Product object.
    product = self.factory_method()
    # Now, use the product.
    result = product.operation()
    return result

# Concrete Creators override the factory method to change the resulting product's type.
class ConcreteCreatorA(Creator):
  def factory_method(self):
    return ConcreteProductA()

class ConcreteCreatorB(Creator):
  def factory_method(self):
    return ConcreteProductB()

# Client code
def client_code(creator):
  print(f"Client: Im not aware of the creator's class, but it still works."
        f"{creator.some_operation()}")

client_code(ConcreteCreatorA())
client_code(ConcreteCreatorB())
    """)


if __name__ == "__main__":
    main()