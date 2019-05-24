function [R] = RotateDof(o)
%
% 
R=[cos(o) sin(o) 0 0;
   0 0 cos(o) sin(o)];
