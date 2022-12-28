import streamlit as st


def main():
    st.title("Command Design Pattern | Behavioral")
    st.info("""
        The Command design pattern is a behavioral design pattern that allows 
        you to encapsulate a request as an object, separate from the object that 
        actually processes the request. This allows you to parametrize clients with 
        different requests, queue or log requests, and support undoable operations.
    """)

    st.subheader("Explanation")

    st.write("""
        In this example, the 'Command' interface declares a method for executing 
        a command. The 'Receiver' class knows how to perform the operations 
        associated with carrying out a request.
    """)

    st.write("""
        The 'ConcreteCommand' class defines a binding between a 'Receiver' object 
        and an action, and implements the 'Command' interface by calling the 
        corresponding operation(s) on the 'Receiver'.
    """)

    st.write("""
        The 'Invoker' class asks the command to carry out the request. The 
        'Client' code creates a 'Receiver', 'ConcreteCommand', and Invoker object 
        and then invokes the command twice.
    """)

    st.write("---")

    st.subheader("Implementation")

    st.code("""
# The Command interface declares a method for executing a command.
class Command(ABC):
  @abstractmethod
  def execute(self):
    pass

# The Receiver class knows how to perform the operations associated with carrying out a request.
class Receiver:
  def action(self):
    print("Receiver: Performing an action.")

# The ConcreteCommand class defines a binding between a Receiver object and an action.
# The ConcreteCommand implements the Command interface by calling the corresponding operation(s) on the Receiver.
class ConcreteCommand(Command):
  def __init__(self, receiver):
    self._receiver = receiver

  def execute(self):
    self._receiver.action()

# The Invoker class asks the command to carry out the request.
class Invoker:
  def __init__(self, command):
    self._command = command

  def set_command(self, command):
    self._command = command

  def invoke(self):
    self._command.execute()

# Client code
receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker(command)

invoker.invoke()

invoker.set_command(ConcreteCommand(receiver))
invoker.invoke()
    """)


if __name__ == "__main__":
    main()
