function [meshC] = defineDiscretization(meshC,geom)
%
% CO = nodal coordinates (global coordinates): [x-coord y-coord]
% CM = nodal connectivity (global numbering): [1 node 2 node]
%
switch meshC.geom
    case '1d'
        CO = [linspace(0,geom.L,7)' linspace(0,0,7)';...
            linspace(geom.L/6*cos(pi/3),geom.L*(1-cos(pi/3)/6),6)' linspace(geom.L/6*sin(pi/3),geom.L/6*sin(pi/3),6)'];
        CM = [(1:6)' (2:7)'; 1 8; 8 2; 2 9; 9 3;...
            3 10;10 4;4 11;11 5;5 12;12 6;6 13;13 7;...
            (8:12)' (9:13)'];
        meshC.CO=CO;
        meshC.CM=CM;
        meshC.TDof=size(CO,1)*meshC.dof;
        x=CO(:,1); y=CO(:,2);
        d=CM(:,1:2)';
        figure
        plot(x(d),y(d),'k','linewidth',2);
        set(gca,'visible','off');
        set(gcf,'color','w');
        axis equal
    case '2d'
       gTM = [
       % Segment type: 1 arc, 2 line
       2 2 2 2 2 2 2 1 2 1
       0 1 1 2 2 0 0.3 0.7 0.7 0.3      
       1 1 2 2 0 0 0.7 0.7 0.3 0.3    
       0 0 1 1 1.5 1.5 0.8 0.8 1.0 1.0
       0 1 1 1.5 1.5 0 0.8 1.0 1.0 0.8
       1 1 1 1 1 1 0 0 0 0  
       0 0 0 0 0 0 1 1 1 1
       0 0 0 0 0 0 0 0.7 0 0.3 
       0 0 0 0 0 0 0 0.9 0 0.9
       0 0 0 0 0 0 0 0.1 0 0.1];
        %plotting geometry
        figure
        pdegplot(gTM); 
        set(gcf,'color','w');
        xlabel('x, [m]');
        ylabel('y, [m]','rotation',0);
        title('solid model');
        axis equal
        [CO,eTM,CMt] = initmesh(gTM,'Hmax',meshC.fineness,'Hgrad',1.2);
        CO=CO'; CM=CMt(1:3,:)';
%         figure
%         triplot(CM,CO(:,1),CO(:,2));
%         axis equal
        %plotting mesh
        figure
        pdemesh(CO',eTM,CMt);
        set(gcf,'color','w');
        title('meshed model');
        set(gca,'visible','off');
        axis equal
        meshC.CO=CO;
        meshC.CM=CM;
        meshC.TDof=size(CO,1)*meshC.dof;
    
end