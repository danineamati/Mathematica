% For this exercise, we will give you algebraic equations and ask you
% to solve for the unknown variable.

% Equation 1.    10 = 2.*apple + Seed;
% Equation 2.    17 = 3.*Banana - apple;
% Equation 3.    Banana = (carrot.^2 - 2)./2;
% Equation 4.    5.*carrot - 1 = sqrt(apple + Banana + dragonFruit);

% First we define the value of a variable.
% Change this variable to test your program.
Seed = 2;

% We solve the first equation for you.
apple = (10 - Seed)./2;

% 1. Solve for Banana (now that we know apple and Seed)
Banana = (17 + apple)./3;

% 2. Solve for carrot
carrot = sqrt(2.*Banana + 2);

% 3. Solve for dragonFruit
dragonFruit = ((5.*carrot -1) ^ 2) - apple - Banana;

% 4. Print the values of apple, Banana, carrot, and dragonFruit
display(apple);
display(Banana);
display(carrot);
display(dragonFruit);
