---
title: Template Method
---

Defines commons steps of an algorithm in a superclass but allows subclasses to override specific steps of the algorithm without changing its structure.

1. Extract out common steps into a abstract base class as implemented methods.
2. Extract out different steps into abstract base class as abstract methods.
3. Move all calls to these method into a **template method**.

```puml
@startuml
AbstractClass <|-- ConcreteClass1
AbstractClass <|-- ConcreteClass2
abstract AbstractClass {
  ...
  template_method()
  common_step()
  {abstract} abstract_step()
}
note right of AbstractClass::template_method
common_step()
abstract_step()
end note

class ConcreteClass1 {
  abstract_step()
}

class ConcreteClass2 {
  abstract_step()
}
@enduml
```

# Usage

* Several functionalities with identical algorithms and some minor differences.
* Limit extensions to the class to only the abstract methods.