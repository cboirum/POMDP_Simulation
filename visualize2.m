%POMDP simulation visualization
% b1a = [-1009	-1009	-1009	-1009	-1009	-1009	-1009	-1009	-1009	-1009	-1009	-1009	91	-1009	-1009	-1009	-1009];
% 
% 
% b1 = vec2mat(b1a(1:end-1),4);
% b1 = b1-min(min(b1))
% b1b = b1/norm(b1)
% 
% [X,Y] = meshgrid([1:4])
[r,c] = size(belief);
for i = 1:r
    bgrid = vec2mat(belief(i,:),4);
    bgrid = bgrid-min(min(bgrid));
    bgrid = bgrid/norm(bgrid);
%     figure(i)
    imagesc(bgrid); colormap(flipud(colormap('gray')));
    x = 1.5:1:5;
    x = [ x; x; repmat(nan,1,4) ];
    y = [ 0.5 5.5 nan ].';
    y = repmat(y,1,4);
    x = x(:);
    y = y(:);
    line(x,y,'linestyle',':','color','k');
    line(y,x,'linestyle',':','color','k');
    axis square
    M(i) = getframe;

end

movie(M,1,3)