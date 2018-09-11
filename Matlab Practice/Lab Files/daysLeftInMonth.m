function [ daysLeft ] = daysLeftInMonth( month, day, year)
    %Set all months to 30 days
    daysInMonth = 30 .* ones(1,12);
    
    %Change months that have 31 days
    daysInMonth([1, 3, 5, 8, 10, 12]) = 31;
    
    %Check for leap year
    leapYear = isLeapYear(year);
    
    %Change February if leap year
    daysInMonth(2) = 28 + leapYear;
    
    daysLeft = daysInMonth(month) - day;
end

