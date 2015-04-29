%POMDP simulation visualization




belief = belief10x10(:,1:end-1);
[r,c] = size(belief);
start = 1900
stop = 1938
clear M
j=1;
for i = start:min(stop,r)
    bgrid = vec2mat(belief(i,:),10);
    bgrid = bgrid-min(min(bgrid));
    bgrid = bgrid/norm(bgrid);
%     figure(i)
    imagesc(bgrid); colormap(flipud(colormap('gray')));
%     x = 1.5:1:c;
%     x = [ x; x; repmat(nan,1,c) ];
%     y = [ 0.5 5.5 nan ].';
%     y = repmat(y,1,4);
%     x = x(:);
%     y = y(:);
%     line(x,y,'linestyle',':','color','k');
%     line(y,x,'linestyle',':','color','k');
    axis square
    M(j) = getframe;
    j=j+1;
end

movie(M,1,5)