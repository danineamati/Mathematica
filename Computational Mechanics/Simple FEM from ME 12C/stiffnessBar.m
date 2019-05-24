function [Ka]=stiffnessBar(geom,mat,L)
%
%
Ka=(mat.E*geom.b*geom.t/L)*[1 -1;-1 1];                 % Bar element stiffness matrix
%
%