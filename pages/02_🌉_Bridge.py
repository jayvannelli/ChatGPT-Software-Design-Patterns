import streamlit as st


def main():
    st.title("Bridge Design Pattern | Structural")
    st.info("""
        The Bridge design pattern is a structural design pattern that divides an 
        object's implementation into an interface and an implementation class. 
        It allows the implementation class to vary independently from the interface class.
    """)

    st.subheader("Explanation")

    st.write("""
        In this example, the 'Abstraction' class defines the interface for the methods 
        that will be implemented by the 'Implementor' class. The 'ConcreteImplementor' classes 
        provide concrete implementations of the 'Implementor' interface. 
    """)

    st.write("""
        The 'Client' code uses the 'Abstraction' class, which selects the appropriate 
        'ConcreteImplementor' object to use based on its current state.
    """)

    st.write("---")

    st.subheader("Implementation")

    st.code("""
from abc import ABC, abstractmethod

# The Abstraction class is the class that will use the Implementor class.
# It defines the interface for the methods that will be implemented by the Implementor.
class Abstraction:
  def __init__(self, implementor):
    self._implementor = implementor

  def operation(self):
    return self._implementor.operation_implementation()

# The Implementor interface declares the methods that will be implemented by the Concrete Implementors.
class Implementor(ABC):
  @abstractmethod
  def operation_implementation(self):
    pass

# Concrete Implementors provide concrete implementation of the Implementor interface.
class ConcreteImplementorA(Implementor):
  def operation_implementation(self):
    return "Concrete Implementor A"

class ConcreteImplementorB(Implementor):
  def operation_implementation(self):
    return "Concrete Implementor B"

# Client code
def client_code(abstraction):
  print(abstraction.operation())

abstraction = Abstraction(ConcreteImplementorA())
client_code(abstraction)

abstraction.set_implementor(ConcreteImplementorB())
client_code(abstraction)
    """)


if __name__ == "__main__":
    main()
