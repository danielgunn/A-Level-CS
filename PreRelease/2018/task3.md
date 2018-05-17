# Pre-release Task 3 [30 marks]

## 3.1 [10 marks]
- 1 marks per line [5 total]
- 1 mark for each being in the correct section [4 total]
- 1 mark for syntax
    - "time travel"
    - lowercase atom
    - missing period at the end of a predicate.

```prolog
character(habib).
character_type(habib, explorer).
has_skill(habib, time_travel).
pet(habib, fish).
animal(fish).
```

## 3.2 [4 marks]
- 1 mark per line below
- 1 mark for syntax

```prolog
pet(C, P) :- 
    character(C),
    pet(P).
```

## 3.3 [ 6 marks ]
- 1 mark for each line of different type [5 max]
- 1 for syntax
```prolog
character(daniel).
character_type(daniel, teacher).
has_skill(daniel,python).
pet(daniel, erniu).
animal(dog).
```
## 3.4 [5 marks]
query | answer
-- | --
character(jim). | true.
character_type(jenny,X). |  X = princess.
character_type(X, prince). | X = jim.
has_skill(jenny, X). | X = invisibility.
has_skill(X, fly). | X = jim.

---

## 3.5 [5 marks]

- all Jim's pets
```prolog
pet(jim, X).
```
- all the characters who can fly
```prolog
has_skill(X, fly).
```
- all the skills
```prolog
skill(X).
```
- all the pets of characters who are princesses [2 marks]
```prolog
character_type(X, princess), pet(X, Y).
```