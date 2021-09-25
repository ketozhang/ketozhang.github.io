---
title: Builder
---

Construct complex objects step by step allowing different object types with the same construction code.

* The different object types does not need to implement the same interface.

```puml
@startuml
Client --> Director
Client --> ConcreteBuilder1
Client --> ConcreteBuilder2
Director o-- Builder
Builder <|.. ConcreteBuilder1
Builder <|.. ConcreteBuilder2
ConcreteBuilder1 <-- Product1
ConcreteBuilder2 <-- Product2

class Client {
  ...
  main()
  set_builder(builder)
}
note right of Client::main
  d = Director()

  builder = ConcreteBuilder1()
  d.make_product(builder)
  product = builder.product

  builder = ConcreteBuilder2()
  d.make_product(builder)
  product = builder.product
end note

class Director {
  builder: Builder
  make_product(builder)
}

note right of Director::make_product
  builder.stepA()
  builder.stepB()
  builder.stepC()
end note

interface Builder {
  reset()
  stepA()
  stepB()
  stepC()
}

class ConcreteBuilder1 {
  product: Product1
  reset()
  stepA()
  stepB()
  stepC()
}

class ConcreteBuilder2 {
  product: Product2
  reset()
  stepA()
  stepB()
  stepC()
}
@enduml
```

## Usage
* Reduce structure with many subclasses
* Reduce constructor with many optional parameters
* Let client build their own object step by step without returning the object until the client calls for the return.