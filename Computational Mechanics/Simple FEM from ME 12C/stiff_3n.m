function [Kel,B] = stiff_3n(t,nu,E,Xel,Yel)

C=E/(1-nu^2)*[1 nu 0;
    nu 1 0;
    0 0 (1-nu)/2];

w=1/2;
r=1/3;
s=1/3;

Hr=[-1;
    1;
    0];

Hs=[-1;
    0;
    1];


for yy=1:length(Xel),
    
    J11(yy,:)=Hr(yy)*Xel(yy); J12(yy,:)=Hr(yy)*Yel(yy);
    J21(yy,:)=Hs(yy)*Xel(yy); J22(yy,:)=Hs(yy)*Yel(yy);
    
end

J=[sum(J11,1) sum(J12,1);
    sum(J21,1) sum(J22,1)];

DetJ=det(J);
Jdet=inv(J)*DetJ; 
j11=Jdet(1,1); j12=Jdet(1,2);   
j21=Jdet(2,1); j22=Jdet(2,2);

for tt=1:length(Xel),
    
    Bb(:,(2*tt-1):2*tt)=[j11*Hr(tt)+j12*Hs(tt) 0;
        0 j21*Hr(tt)+j22*Hs(tt);
        j21*Hr(tt)+j22*Hs(tt) j11*Hr(tt)+j12*Hs(tt)];
    
end


B=Bb/DetJ;
Kel=w*B'*C*B*t*DetJ;
    





