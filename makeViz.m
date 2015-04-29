%Generate the X and Y grid arrays using the MESHGRID function.

x = [1:6];

y = [1:4];

[X,Y] = meshgrid(x,y)

%Note that size(Z) is the same as size(x) and size(y)

Z = [1 0 -2 1 2 1;2 -2 0 -1 0 1;1 0 0 -2 2 1;1 1 1 1 1 1];

% create a colormap having RGB values of dark green,

%light green, white, dark red and light red.

map2 = [0 1 0; 0 0.8 0;1 1 1;0.6 0 0;1 0 0 ];

%use the user defined colormap for figure.

colormap(map2);

%plot the figure

pcolor(X,Y,Z);

%set the x and y labels

set(gca,'XTick',[1 2 3 4 5 6],'YTick',[1 2 3 4],'XTicklabel',[' ';'a';'b'; 'c'; 'd';'e'],'YTicklabel',[' ';'f';'g';'h']);

%set the color limits

caxis([-2 2])
