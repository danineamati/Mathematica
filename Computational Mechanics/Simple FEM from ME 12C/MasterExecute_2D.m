%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%----------  A SKELETON OF A FINITE ELEMENT PROGRAM --------------------- %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
initialize
%
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
% ---------- DEFINE SPATIAL DIMENSIONS OF SOLID MODEL ------------------- %
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
%
meshC.geom = '2d';
%
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
% ---- DEFINE GEOMETRIC AND MATERIAL PROPERTIES OF THE SOLID MODEL ------ %
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
%
geom.Lx=10;                 % [m] x dimension of 2-D solid model 
geom.Ly=10;                 % [m] y dimension of 2-D solid model 
geom.t= 0.1;                % [m] thickness of 2-D solid model
mat.E = 7.0e10;             %  [GPa]  Young's modulus (Aluminum)
mat.nu = 1/3;               %  Poisson's ratio (Aluminum)
mat.rho = 2700;             % [Kg/m^3] density (Aluminum)
%
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
% ---- DICRETIZE THE SOLID MODEL ---------------------------------------- %
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
%
meshC.Nelemx=10;        % number of elements for discretization in the x direction
meshC.Nelemy=10;        % number of elements for discretization in the x direction
meshC.dof=2;            % number of degrees of freedom per node
meshC.fineness=0.08;    % maximum triangle edge length
%
[meshC] = defineDiscretization(meshC,geom);
%
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
% ---- ASSEMBLE GLOBAL MATRICES: (STIFFNESS, MASS, DAMPING) ------------- %
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
%
[matrices] = defineMatrices(geom,mat,meshC);
%
% --- INSPECT MATRICES:
%
figure
spy(matrices.K);
title('non-zero components of stiffness matrix');
%
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
% ---- SOLVE PROBLEM ---------------------------------------------------- %
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
%
% --- DEFINE BOUNDARY CONDITIONS:
%
kn=find(meshC.CO(:,2)==min(meshC.CO(:,2)));             % nodes at which some/all dofs are known
kdof1=sort([kn*meshC.dof-1; kn*meshC.dof]);   % known dofs. In this case we know displacements in the x and y directions, i.e., 0
kn=find((meshC.CO(:,1)==max(meshC.CO(:,1))));  % nodes at which some/all dofs are known
kdof2=sort(kn*meshC.dof);                   % known dofs. In this case we know displacements in the x and y directions, i.e., 0
udof=1:meshC.TDof;                          % initialize unknown dofs  
kdof=[kdof1' kdof2'];
udof(sort(kdof))=[];                % unknown dofs (mutually exclusive with known dofs)
%
% --- ASSEMBLE NODAL LOAD VECTOR:
%
F=zeros(meshC.TDof,1);
%kf = 4;                     % nodes at which loads are applied
%kdof_f = meshC.dof*kf;      % dof corresponding to applied load
%F(kdof_f,1)=-20e3;          % [N] Weight of the truck
%
% --- SOLVE FOR NODAL DISPLACEMENTS:
%
u=zeros(meshC.TDof,1);  % initialize nodal dof vector
u(kdof1,1)=0;            % trivial in this case.  May be useful is known dofs aren't 0 
u(kdof2,1)=-0.01;       %
u(udof)=matrices.K(udof,udof)\(F(udof,1)-matrices.K(udof,kdof)*u(kdof));
%
% --- COMPUTE REACTION LOADS:
%
F(kdof,1)=matrices.K(kdof,udof)*u(udof)+matrices.K(kdof,kdof)*u(kdof);
%
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
% ---- POST-PROCESS RESULTS --------------------------------------------- %
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %
%
% --- PLOT DEFORMED MODEL:
%
x=meshC.CO(:,1); y=meshC.CO(:,2); z=zeros(size(meshC.CO,1),1);
fact=1e1;
xn=meshC.CO(:,1)+fact*u(1:meshC.dof:end);
yn=meshC.CO(:,2)+fact*u(2:meshC.dof:end);
d=meshC.CM(:,1:3)';
figure
patch(x(d),y(d),z(d),'edgecolor','r','facealpha',1,'facecolor','none'); hold on
patch(xn(d),yn(d),z(d),'edgecolor','k','facecolor','none','facealpha',0); 
set(gcf,'color','w');
xlabel('x, [m]');
ylabel('y, [m]','rotation',0);
title(['deformed model, scale factor = ' num2str(fact)]);
axis equal

%
% --- COMPUTE AND DISPLAY STRESS WITHIN EACH ELEMENT:
%
[stress] = defineStress(mat,meshC,matrices,u);
%
figure
patch(xn(d),yn(d),z(d),(stress/1e6)','EdgeColor','interp'); shading interp
set(gcf,'color','w');
xlabel('x, [m]');
ylabel('y, [m]','rotation',0);
title('Von Mises stress distribution, [MPa]');
colorbar
axis equal
