import streamlit as st


def main():
    st.title("Adapter Design Pattern | Structural")
    st.info("""
        The Adapter design pattern is a structural design pattern that allows you
        to adapt the interface of a class to another interface that clients expect. 
        It allows classes with incompatible interfaces to work together by wrapping 
        an adapter class around the class with the incompatible interface.
    """)

    st.subheader("Explanation")

    st.write("""
        In this example, the 'Target' interface represents the interface that the 
        client expects, and the 'Adaptee' class contains the interface that the 
        client needs to adapt to.
    """)

    st.write("""
        The 'Adapter' class adapts the 'Adaptee' class to the 'Target' interface by 
        implementing the request method and calling the 'specific_request' method 
        on the 'Adaptee' object.
    """)

    st.write("""
        The 'Client' code uses the 'Target' interface and is unaware of the specific 
        type of object it is using.
    """)

    st.write("---")

    st.subheader("Implementation")

    st.code("""
# The Target interface represents the interface that the client expects.
class Target(ABC):
  @abstractmethod
  def request(self):
    pass

# The Adaptee class contains the interface that the client needs to adapt to.
class Adaptee:
  def specific_request(self):
    return ".eetpadA eht fo roivaheb laicepS"

# The Adapter class adapts the Adaptee class to the Target interface.
class Adapter(Target):
  def __init__(self, adaptee):
    self._adaptee = adaptee

  def request(self):
    return self._adaptee.specific_request()[::-1]

# Client code
def client_code(target):
  print(target.request())

adaptee = Adaptee()
client_code(Adapter(adaptee))
    """)


if __name__ == "__main__":
    main()
