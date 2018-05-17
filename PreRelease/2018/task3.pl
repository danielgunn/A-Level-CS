character(jim).
character(jenny).

character_type(jim,prince).
character_type(jenny,princess).


skill(fly).
skill(invisibility).


has_skill(jim,fly).
has_skill(jenny,invisibility).
has_skill(X,Y) :- character(X), skill(Y).

pet(jim,horse).
pet(jenny,bird).
animal(horse).
animal(bird).

