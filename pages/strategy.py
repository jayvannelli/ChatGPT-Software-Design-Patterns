import streamlit as st


def main():
    st.title("Strategy Design Pattern | Behavioral")
    st.info("""
        The strategy design pattern is a behavioral design pattern that allows 
        you to define a set of interchangeable algorithms or behaviors, and 
        make them interchangeable within an object.
    """)

    st.subheader("Explanation")

    st.write("""
        In this example, the 'Strategy' interface defines the 'execute()' method, 
        which is implemented by the concrete strategies 'ConcreteStrategyA' and 
        'ConcreteStrategyB'.
    """)

    st.write("""
        The 'Context' class holds a reference to a strategy object and allows the 
        client code to change the strategy at runtime by calling the 'set_strategy()' 
        method. The client code can then execute the selected strategy by calling 
        the 'execute_strategy()' method.
    """)

    st.write("---")

    st.subheader("Implementation")

    st.code("""
from abc import ABC, abstractmethod

# Create an interface for the strategy
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete strategies
class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")

# Context class
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

# Client code
context = Context(ConcreteStrategyA())
context.execute_strategy()  # Output: "Executing strategy A"

context.set_strategy(ConcreteStrategyB())
context.execute_strategy()  # Output: "Executing strategy B"
    """)


if __name__ == "__main__":
    main()
