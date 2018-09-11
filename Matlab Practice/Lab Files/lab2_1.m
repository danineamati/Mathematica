% Make the column vector A
A = (1:5)';

% Replace the middle element in A with the number 4
A(3) = 4;

% Assign the 4th element in A to be the same as the 2nd element in A 
% (This line of code should work for any 5 element matrix. DO
% NOT HARD CODE THE NUMBER) 
A(4) = A(2);

% Assign the 5th element in A to be the same as the 1st element in A 
% (This line of code should work for any 5 element matrix. DO
% NOT HARD CODE THE NUMBER) 
A(5) = A(1);

% Make the row vector B
B = (1:5);

% Replace the last 3 elements in B with the first 3 elements in B (DO NOT
% HARD CODE THE NUMBERS)
B(5) = B(3);
B(4) = B(2);
B(3) = B(1);

% Add the number 2 to the 1st element in B
B(1) = B(1) + 2;

% Make B a column vector
B = B';

% Create a new variable C and store the product of A and B
C = A .* B;

