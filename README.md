### what is yaml?

### yaml structure?

### Datatypes in Yaml?

### Yaml in VScode

### YAML & Python

### Real World Yamls

### YAML Fundamental?

Why learn yaml?

1. `Cloud` 
2. `Devops` 
3. `Server to Server`
4. `App to App`

### Common Language
```
JSON
XML
Yaml
```

Human readability

HTML vs XML vs JSON vs YAML

```
---
address:
  street: :101 Main Street"
  ciry: San Jose
  state: Calinfornia
  zip: 95954
```
> [!TIP]
> indentation is very important, 2 Spaces

Comments `#`

#Yaml Styles

1. `Block Styles`
2. `Flow Styles`

### Block Styles Example
```
---
fruits:
  - banana
  - mango
  - apple
---
```
### Flow Styles Example

---
fruits: [ banana, mango, apple ]
---

Block Styles
---
address:
  street: "101 main street"
  city: San Jose
  state: Calinfornia
  zip: 95035   # Same as dictnory

### Flow Styles
```
---
address: { street: "101 main street", city: San Jose, state: Calinfornia, zip: 95035}
```

### key value pairs
```
city = "New York"
```
City is Key and "new York" is value

#####
# Yaml Datatypes
```
1. Scalars
    a. Strings
    b. Numbers
    c. Booleans

2. Collections
    1. Sequences
       a. Lists
       b. Arrays
    2. Mapping
       a. Hashes
       b. dictionaries
       c. Key-value pairs
```

### Null Value reperent in Yaml
```
var1: 
var1: null
var1: ~
```

Long Strings

You can use `pipe symbol` will preseve the `new line charater`.
```
message: |
```
```
message: >

new line charater are ignored
```

##################
# multi-line strings(Block Scalars)
```
Block Style: | or >

Block chomping indictapr : - Or +

indentation: number

message: >-3
```
