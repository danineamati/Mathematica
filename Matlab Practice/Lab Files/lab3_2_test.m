% Create a random gsi and grades matrix
rng(15);
gsi = floor(rand(10)*9);
grades = rand(10)*100;
curve = 10;

% Call the function to adjust grades
new_grades = lab3_2(grades, gsi, curve);

