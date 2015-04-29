%POMDP simulation visualization

belief = belief10x10(:,1:end-1);
[r,c] = size(belief);
gridSize = 10;
start = 1;
stop = 10;
start = 1;
stop = 10;
fps = 3;
saveVideo = 1;
endFrames = 9;
clear M
j=1;
if saveVideo
    writerObj = VideoWriter('10x10.avi');
    writerObj.FrameRate = fps;
    open(writerObj);
end
for i = start:min(stop,r)
    b1 = belief(i,:);
    b1 = b1-min(min(b1));
    b1 = b1/norm(b1);
    bgrid = flipud(vec2mat(b1,gridSize))
    imagesc(bgrid); colormap(flipud(colormap('gray')));
    axis square
    M(j) = getframe;
    
    if saveVideo
        writeVideo(writerObj,M(j));
    end
    j=j+1;
end
if saveVideo
    for i = 1:endFrames
        writeVideo(writerObj,M(j-1));
    end
    close(writerObj);
end
% movie(M,1,fps)

