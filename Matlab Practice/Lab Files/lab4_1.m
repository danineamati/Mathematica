% 1. Insert code to clear out every variable in the workspace
clear;
% 2. Load lab4_1_water.mat which contains the Flint Service Line data
load('lab4_1_water.mat');

% 3. Find a logical array for all areas that have ALL 3 of the following
%    properites
%		- have a precinct LESS THAN the average of all precincts
%		- are greater than 0.01 acres in area
%		- are neither in cenblock 3 nor in cenblock 5

target = (Precinct < mean(Precinct)) .* (Acres > 0.01) .* ...
        not(Cenblock == 3) .* not(Cenblock == 5);

% 4. Use the target logical array to find the zipcodes of these areas

zipcodes = Zip .* target;

% 5. Save the workspace variables as lab4_1
save('lab4_1.mat');
