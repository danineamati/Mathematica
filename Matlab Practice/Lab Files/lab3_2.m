function [ new_grades ] = lab3_2(grades, gsi, curve)
% Fixes the old grades that the graduate student instructors mis-graded.
    % Subtract 3 from students of Amit
    amit_mat = (gsi == 0) .* 3;
    % Add 10 to students of Lizzy and Jason
    liz_jas_mat = (gsi == 5 | gsi == 8) .* 10;
    % Add 5 to all remaining students
    else_mat = not(gsi == 0 | gsi == 5 | gsi == 8) .* 5;
    
    % Create new grades
    new_grades = grades - amit_mat + liz_jas_mat + else_mat + curve;
    
    % Remove failing grades
    failing_grades = (new_grades < 50);
    new_grades = new_grades .* not(failing_grades);
    
    % No grade over 100 is possible
    exceeding_grades = (new_grades > 100);
    new_grades = new_grades .* not(exceeding_grades);
    new_grades = new_grades + (exceeding_grades * 100);
    
end