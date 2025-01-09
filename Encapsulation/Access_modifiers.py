Public Attributes/Methods:
These are freely accessible by any code.
Convention: Use no underscore (attribute, method()).
Example: car.brand


Protected Attributes/Methods:
These are intended to be used inside the class or by subclasses, not by external code.
Convention: Prefix with a single underscore (_attribute, _method()).
Example: car._model


Private Attributes/Methods:
These are strictly for internal use only and are not supposed to be accessed directly.
Convention: Prefix with a double underscore (__attribute, __method()).
Example: car.__year
