import streamlit as st


def main():
    st.subheader("Coupling")

    st.info("""
        In software development, coupling refers to the degree to which one module 
        or component in a system depends on or is connected to other modules or 
        components.
        """)

    st.write("""
        High coupling means that a module is heavily dependent on other 
        modules, while low coupling means that a module is more independent and can 
        function more independently of other parts of the system.
        """)

    st.write("---")

    st.subheader("Example of code with HIGH Coupling")

    st.code("""
class A:
    def __init__(self):
        self.b = B()

    def do_something(self):
        self.b.do_something_else()

class B:
    def do_something_else(self):
        print("Doing something else")
    """)

    st.write("""
        In this example, class A is tightly coupled to class B because it creates an 
        instance of B in its constructor and depends on it to perform the 
        'do_something_else' method. This means that if the implementation of class B 
        changes, it will likely affect the behavior of class A as well.
    """)

    st.write("---")

    st.subheader("Example of code with LOW Coupling")

    st.code("""
class A:
    def __init__(self, b):
        self.b = b

    def do_something(self):
        self.b.do_something_else()

class B:
    def do_something_else(self):
        print("Doing something else")

b = B()
a = A(b)
a.do_something()
    """)

    st.write("""
        In this example, class A is not tightly coupled to class B because it receives 
        an instance of B as an argument in its constructor, rather than creating one 
        itself. This means that class A is less dependent on class B and can function 
        independently of it to some degree. If the implementation of class B changes, 
        it may not necessarily affect the behavior of class A.
    """)

    st.write("""
        It is generally considered good software design to aim for low coupling, 
        as it can make a system more flexible and easier to maintain. High coupling 
        can make it more difficult to make changes to a system without affecting other 
        parts of the system.
    """)


if __name__ == "__main__":
    main()
