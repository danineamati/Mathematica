function [flag] = isLeapYear( year_check )
% setup a row vector to contain the number of days/year
%  from year 1 to year 2500

    AD = 365 .* ones(1,2500);   % start with 365 days/year for 2500 years
    AD(4:4:2500) = 366;         % rule 1: leap year every 4 years
    AD(100:100:2500) = 366;     % rule 2:  but not in century years
    AD(400:400:2500) = 365;     % rule 3:  EXCEPT if a 400th year
    flag = AD(year_check) == 366;     % return TRUE if isLeapYear
    
end

