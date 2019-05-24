function [matrices] = defineMatrices(geom,mat,meshC)
%
K=zeros(meshC.TDof);
dof=meshC.dof;
CM=meshC.CM;
CO=meshC.CO;
%
% 1-D ELEMENTS
%
switch meshC.geom
    case '1d'
        xi=CO(CM(:,1),1);
        xf=CO(CM(:,2),1);
        yi=CO(CM(:,1),2);
        yf=CO(CM(:,2),2);
        L=sqrt((xf-xi).^2 + (yf-yi).^2);
        angle=atan2((yf-yi),(xf-xi));
        for ii=1:meshC.Nelem,
            %loc=[(dof*CM(ii,1)-(dof-1)):(dof*CM(ii,1))  (dof*CM(ii,2)-(dof-1)):(dof*CM(ii,2))];
            loc=[dof*CM(ii,1)-1 dof*CM(ii,1) dof*CM(ii,2)-1 dof*CM(ii,2)];
            KeL=stiffnessBar(geom,mat,L(ii));
            R = RotateDof(angle(ii));
            KeG=R'*KeL*R;
            K(loc,loc)=K(loc,loc) + KeG;
        end
        matrices.K=K;
    case '2d'
        for ii=1:size(CM,1),
            Xel=CO(CM(ii,:),1);
            Yel=CO(CM(ii,:),2);
            for tt=1:size(CM,2),
                loc(ii,(dof*tt-(dof-1)):dof*tt)=[dof*CM(ii,tt)-(dof-1):dof*CM(ii,tt)];
            end
            [Kel,B(:,:,ii)]=stiff_3n(geom.t,mat.nu,mat.E,Xel,Yel);
            K(loc(ii,:),loc(ii,:))=K(loc(ii,:),loc(ii,:))+Kel;
        end
        matrices.K=K;
        matrices.loc=loc;
        matrices.B=B;
end