function [stress] = defineStress(mat,meshC,matrices,u)
%
dof=meshC.dof;
CM=meshC.CM;
CO=meshC.CO;

switch meshC.geom
    case '1d'
xi=CO(CM(:,1),1);
xf=CO(CM(:,2),1);
yi=CO(CM(:,1),2);
yf=CO(CM(:,2),2);
L=sqrt((xf-xi).^2 + (yf-yi).^2);
angle=atan2((yf-yi),(xf-xi));
%
%
stress=zeros(meshC.Nelem,1);
for ii=1:meshC.Nelem,
    loc=[dof*CM(ii,1)-1 dof*CM(ii,1) dof*CM(ii,2)-1 dof*CM(ii,2)];
    ueG=u(loc,1);
    R = RotateDof(angle(ii));
    ueL=R*ueG;
    B=strainItnterpolMatrix(L(ii));
    stress(ii)=mat.E*B*ueL;
end
    case '2d'
    for ee=1:size(CM,1),
    ue=u(matrices.loc(ee,:));
    Cmat=mat.E/(1-mat.nu^2)*[1 mat.nu 0;mat.nu 1 0; 0 0 (1-mat.nu)/2];
    str=matrices.B(:,:,ee)*ue;
    stress(ee,:)=(Cmat*str)';
    s1=stress(ee,1); s2=stress(ee,2); t12=stress(ee,3);
    von(ee,1)=sqrt(s1^2 + s2^2 -s1*s2 + 3*t12^2);
    end
    stress=[von von von];
end