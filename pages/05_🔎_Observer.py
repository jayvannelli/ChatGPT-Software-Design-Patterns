import streamlit as st


def main():
    st.title("Observer Design Pattern | Behavioral")
    st.info("""
        The Observer design pattern is a behavioral design pattern that allows an object to 
        subscribe to events and receive notifications when those events occur. It enables a 
        one-to-many dependency between objects, so that when one object changes its state, 
        all of its subscribers are notified and updated automatically.
    """)

    st.subheader("Explanation")

    st.write("""
        In this example, the 'Subject' class generates events and notifies its 
        'Observer' objects when its state changes.
    """)

    st.write("""
        The 'ConcreteObserver' classes implement the 'Observer' interface and 
        provide concrete implementations of the 'update' method to receive 
        notifications from the 'Subject' and react to them.
    """)

    st.write("""
        The 'Client' code uses the 'Subject' class and the 'ConcreteObserver' 
        classes to subscribe to and receive notifications of events.
    """)

    st.write("---")

    st.subheader("Implementation")

    st.code("""
from abc import ABC, abstractmethod

# The Subject class is the class that will generate events and notify its observers.
class Subject:
  def __init__(self):
    self._observers = []
    self._state = None

  def attach(self, observer):
    self._observers.append(observer)

  def detach(self, observer):
    self._observers.remove(observer)

  def notify(self):
    for observer in self._observers:
      observer.update(self)

  @property
  def state(self):
    return self._state

  @state.setter
  def state(self, state):
    self._state = state
    self.notify()

# The Observer interface declares the update method, which is called by the Subject when the Subject's state changes.
class Observer(ABC):
  @abstractmethod
  def update(self, subject):
    pass

# Concrete Observers implement the update method to receive notifications from the Subject and react to them.
class ConcreteObserverA(Observer):
  def update(self, subject):
    if subject.state < 3:
      print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
  def update(self, subject):
    if subject.state == 0 or subject.state >= 2:
      print("ConcreteObserverB: Reacted to the event")

# Client code
subject = Subject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.state = 1
subject.state = 2
subject.detach(observer_a)
subject.state = 3
    """)


if __name__ == "__main__":
    main()
